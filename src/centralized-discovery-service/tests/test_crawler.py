# tests/test_crawler.py

import pytest
import asyncio
import aiohttp
from unittest.mock import patch, AsyncMock, MagicMock
from app.services.crawler import Crawler, get_agents_json_url_from_dns
from app.models import Service, Intent
from sqlalchemy.orm import Session

@pytest.fixture
def mock_agents_json():
    return {
        "service_info": {
            "name": "testservice.com",
            "description": "A test service",
            "service_url": "https://testservice.com",
            "service_logo_url": "https://testservice.com/logo.png",
            "service_terms_of_service_url": "https://testservice.com/terms",
            "service_privacy_policy_url": "https://testservice.com/privacy"
        },
        "intents": [
            {
                "intent_uid": "testservice.com:TestIntent:v1",
                "intent_name": "TestIntent",
                "description": "A test intent",
                "input_parameters": [],
                "output_parameters": [],
                "endpoint": "https://testservice.com/api/execute/TestIntent",
                "tags": ["test", "intent"]
            }
        ]
    }

@pytest.mark.asyncio
async def test_crawler_fetch_agents_json(mock_agents_json):
    """Test the crawler's fetch_agents_json method."""
    # Create a mock db_session (since it's required but not used in this method)
    db_session = MagicMock(spec=Session)
    crawler = Crawler(domains=[], db_session=db_session)
    url = "https://testservice.com/agents.json"

    # Mock aiohttp ClientSession.get
    with patch('aiohttp.ClientSession.get') as mock_get:
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.json.return_value = mock_agents_json
        mock_get.return_value.__aenter__.return_value = mock_response

        data = await crawler.fetch_agents_json(url)

    assert data == mock_agents_json

@pytest.mark.asyncio
async def test_crawler_process_domain(db_session, mock_agents_json):
    """Test the crawler's process_domain method."""
    # Mock get_agents_json_url_from_dns
    with patch('app.services.crawler.get_agents_json_url_from_dns', return_value=None):
        # Mock fetch_agents_json
        with patch.object(Crawler, 'fetch_agents_json', return_value=mock_agents_json):
            crawler = Crawler(domains=["testservice.com"], db_session=db_session)
            await crawler.process_domain("testservice.com")

    # Verify data in the database
    service = db_session.query(Service).filter_by(name="testservice.com").first()
    assert service is not None
    assert service.description == "A test service"

    intent = db_session.query(Intent).filter_by(intent_uid="testservice.com:TestIntent:v1").first()
    assert intent is not None
    assert intent.intent_name == "TestIntent"

@pytest.mark.asyncio
async def test_crawler_start(db_session, mock_agents_json):
    """Test the crawler's start method."""
    domains = ["testservice.com", "example.com"]

    # Mock process_domain to avoid actual network calls and database operations
    with patch.object(Crawler, 'process_domain', new_callable=AsyncMock) as mock_process_domain:
        crawler = Crawler(domains=domains, db_session=db_session)
        await crawler.start()

        # Ensure process_domain was called for each domain
        assert mock_process_domain.call_count == len(domains)
        mock_process_domain.assert_any_call("testservice.com")
        mock_process_domain.assert_any_call("example.com")

# Additional test for process_agents_json method
def test_crawler_process_agents_json(db_session, mock_agents_json):
    """Test the crawler's process_agents_json method."""
    crawler = Crawler(domains=[], db_session=db_session)
    crawler.process_agents_json(mock_agents_json)

    # Verify data in the database
    service = db_session.query(Service).filter_by(name="testservice.com").first()
    assert service is not None
    assert service.description == "A test service"

    intent = db_session.query(Intent).filter_by(intent_uid="testservice.com:TestIntent:v1").first()
    assert intent is not None
    assert intent.intent_name == "TestIntent"