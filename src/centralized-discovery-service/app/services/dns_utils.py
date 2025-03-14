# app/services/dns_utils.py

import dns.resolver
from functools import lru_cache
import logging

logger = logging.getLogger(__name__)

@lru_cache(maxsize=1024)
def get_agents_json_url_from_dns(domain):
    """Retrieve agents.json URL from DNS TXT records."""
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            txt_record = rdata.to_text().strip('"')
            if 'uim-agents-file=' in txt_record:
                return txt_record.split('=')[1]
    except Exception as e:
        logger.error(f"DNS lookup failed for {domain}: {e}")
    return None