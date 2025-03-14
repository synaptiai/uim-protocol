# app/services/crawler.py

import asyncio
import aiohttp
import logging
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from app.crud.service import create_service, get_service_by_name
from app.crud.intent import create_intent
from app.schemas.service import ServiceCreate
from app.schemas.intent import IntentCreate
from app.models import Service, Intent
from app.config import settings
import dns.asyncresolver

logger = logging.getLogger(__name__)

class Crawler:
    def __init__(self, domains: List[str], db_session: Session):
        self.domains = domains
        self.db_session = db_session

    async def start(self):
        tasks = [self.process_domain(domain) for domain in self.domains]
        await asyncio.gather(*tasks)

    async def process_domain(self, domain: str):
        agents_json_url = await get_agents_json_url_from_dns(domain)
        if not agents_json_url:
            agents_json_url = f"https://{domain}/agents.json"

        agents_json_data = await self.fetch_agents_json(agents_json_url)
        if agents_json_data:
            self.process_agents_json(agents_json_data)

    async def fetch_agents_json(self, url: str) -> Dict[str, Any]:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        logger.error(f"Failed to fetch {url}, status code: {response.status}")
                        return None
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            return None

    def process_agents_json(self, agents_json_data: Dict[str, Any]):
        """Process the agents.json data."""
        try:
            service_info = agents_json_data['service_info']
            service_data = ServiceCreate(**service_info)
            service = get_service_by_name(self.db_session, service_info['name'])
            if not service:
                service = create_service(self.db_session, service_data)
            for intent_data in agents_json_data['intents']:
                create_intent(self.db_session, IntentCreate(**intent_data), service.id)
            self.db_session.commit()
        except Exception as e:
            logger.error(f"Error saving agents.json data: {e}")
            self.db_session.rollback()

async def get_agents_json_url_from_dns(domain: str) -> str:
    """Fetch the agents.json URL from DNS TXT records."""
    try:
        resolver = dns.asyncresolver.Resolver()
        answers = await resolver.resolve(domain, 'TXT')
        for rdata in answers:
            for txt_string in rdata.strings:
                if txt_string.startswith(b"agents_json_url="):
                    return txt_string.decode().split("=", 1)[1]
        return None
    except Exception as e:
        logger.error(f"Error fetching DNS TXT records for {domain}: {e}")
        return None

async def start_crawler(domains: List[str], db_session: Session):
    """Start the crawler for a list of domains."""
    crawler = Crawler(domains=domains, db_session=db_session)
    await crawler.start()