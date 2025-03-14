# tests/test_discovery.py

import pytest
from starlette.testclient import TestClient
from app.main import create_app
from app.dependencies import get_db
from sqlalchemy.orm import Session
from app.crud.service import create_service
from app.crud.intent import create_intent
from app.schemas.service import ServiceCreate
from app.schemas.intent import IntentCreate
from app.schemas.tag import TagCreate

@pytest.fixture
def client(db_session):
    """Create a TestClient with the database session overridden."""
    app = create_app()

    # Override the dependency for the database session
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture
def setup_data(db_session):
    """Set up test data in the database."""
    # Create a test service
    service_data = ServiceCreate(
        name="testservice.com",
        description="A test service",
        service_url="https://testservice.com",
        service_logo_url=None,
        service_terms_of_service_url=None,
        service_privacy_policy_url=None
    )
    service = create_service(db_session, service_data)

    # Create test intents
    intents_data = [
        IntentCreate(
            intent_uid="testservice.com:TestIntent:v1",
            intent_name="TestIntent",
            description="A test intent",
            input_parameters=[],
            output_parameters=[],
            endpoint="https://testservice.com/api/execute/TestIntent",
            tags=[TagCreate(name="test"), TagCreate(name="intent")]
        ),
        IntentCreate(
            intent_uid="testservice.com:AnotherIntent:v1",
            intent_name="AnotherIntent",
            description="Another test intent",
            input_parameters=[],
            output_parameters=[],
            endpoint="https://testservice.com/api/execute/AnotherIntent",
            tags=[TagCreate(name="test"), TagCreate(name="another")]
        )
    ]
    for intent_data in intents_data:
        create_intent(db_session, intent_data, service.id)

    # Commit the changes
    db_session.commit()

def test_get_intent_by_uid(client, setup_data):
    """Test retrieving an intent by UID."""
    response = client.get("/api/intents/testservice.com:TestIntent:v1")
    assert response.status_code == 200
    data = response.json()
    assert data["intent_uid"] == "testservice.com:TestIntent:v1"
    assert data["intent_name"] == "TestIntent"

@pytest.mark.parametrize("query_params,expected_count", [
    ({"intent_name": "TestIntent"}, 1),
    ({"intent_name": "NonExistent"}, 0),
    ({"tags": "test"}, 2),
    ({"tags": "nonexistent"}, 0),
    ({"description": "test intent"}, 1),
    ({"description": "unknown"}, 0),
])
def test_search_intents(client, setup_data, query_params, expected_count):
    """Test searching intents with various parameters."""
    response = client.get("/api/intents/search", params=query_params)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == expected_count