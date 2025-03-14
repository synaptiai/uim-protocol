# tests/test_crud.py

import pytest
from app.crud.service import create_service, get_service_by_name
from app.crud.intent import create_intent, get_intent_by_uid
from app.schemas.service import ServiceCreate
from app.schemas.intent import IntentCreate

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

    # Create a test intent
    intent_data = IntentCreate(
        intent_uid="testservice.com:TestIntent:v1",
        intent_name="TestIntent",
        description="A test intent",
        input_parameters=[],
        output_parameters=[],
        endpoint="https://testservice.com/api/execute/TestIntent",
        tags=["test", "intent"]
    )
    create_intent(db_session, intent_data, service.id)

    # Commit the changes
    db_session.commit()

def test_create_service(db_session):
    """Test creating a service using CRUD operations."""
    service_data = ServiceCreate(
        name="newservice.com",
        description="A new test service",
        service_url="https://newservice.com",
        service_logo_url=None,
        service_terms_of_service_url=None,
        service_privacy_policy_url=None
    )
    service = create_service(db_session, service_data)
    assert service.id is not None
    assert service.name == "newservice.com"

def test_get_service_by_name(db_session, setup_data):
    """Test retrieving a service by name."""
    service = get_service_by_name(db_session, "testservice.com")
    assert service is not None
    assert service.name == "testservice.com"

def test_create_intent(db_session, setup_data):
    """Test creating an intent using CRUD operations."""
    service = get_service_by_name(db_session, "testservice.com")
    assert service is not None, "Service not found in test database."
    
    intent_data = IntentCreate(
        intent_uid="testservice.com:NewTestIntent:v1",
        intent_name="NewTestIntent",
        description="A new test intent",
        input_parameters=[],
        output_parameters=[],
        endpoint="https://testservice.com/api/execute/NewTestIntent",
        tags=["test", "new"]
    )
    intent = create_intent(db_session, intent_data, service.id)
    db_session.commit()
    assert intent.id is not None
    assert intent.intent_name == "NewTestIntent"
    assert len(intent.tags) == 2
    tag_names = [tag.name for tag in intent.tags]
    assert "test" in tag_names
    assert "new" in tag_names

def test_get_intent_by_uid(db_session, setup_data):
    """Test retrieving an intent by UID."""
    intent = get_intent_by_uid(db_session, "testservice.com:TestIntent:v1")
    assert intent is not None
    assert intent.intent_name == "TestIntent"
    assert intent.description == "A test intent"

# Additional test to verify updating a service
def test_update_service(db_session, setup_data):
    """Test updating a service."""
    service = get_service_by_name(db_session, "testservice.com")
    assert service is not None
    service.description = "An updated test service"
    db_session.commit()

    updated_service = get_service_by_name(db_session, "testservice.com")
    assert updated_service.description == "An updated test service"

# Additional test to verify deleting an intent
def test_delete_intent(db_session, setup_data):
    """Test deleting an intent."""
    intent = get_intent_by_uid(db_session, "testservice.com:TestIntent:v1")
    assert intent is not None

    # Delete the intent
    db_session.delete(intent)
    db_session.commit()

    deleted_intent = get_intent_by_uid(db_session, "testservice.com:TestIntent:v1")
    assert deleted_intent is None