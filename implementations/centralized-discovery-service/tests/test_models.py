# tests/test_models.py

import pytest
from app.models import Service, Intent, Tag

def test_service_model(db_session):
    """Test creating a Service model instance."""
    service = Service(
        name="testservice.com",
        description="A test service",
        service_url="https://testservice.com"
    )
    db_session.add(service)
    db_session.commit()
    db_session.refresh(service)
    assert service.id is not None
    assert service.name == "testservice.com"

def test_intent_model(db_session):
    """Test creating an Intent model instance."""
    service = Service(
        name="testservice.com",
        description="A test service",
        service_url="https://testservice.com"
    )
    db_session.add(service)
    db_session.commit()
    db_session.refresh(service)

    intent = Intent(
        service_id=service.id,
        intent_uid="testservice.com:TestIntent:v1",
        intent_name="TestIntent",
        description="A test intent",
        input_parameters=[],
        output_parameters=[],
        endpoint="https://testservice.com/api/execute/TestIntent"
    )
    db_session.add(intent)
    db_session.commit()
    db_session.refresh(intent)
    assert intent.id is not None
    assert intent.intent_name == "TestIntent"

def test_tag_model(db_session):
    """Test creating a Tag model instance and associating it with an Intent."""
    tag = Tag(name="test")
    db_session.add(tag)
    db_session.commit()
    db_session.refresh(tag)
    assert tag.id is not None
    assert tag.name == "test"

    service = Service(
        name="testservice.com",
        description="A test service",
        service_url="https://testservice.com"
    )
    db_session.add(service)
    db_session.commit()
    db_session.refresh(service)

    intent = Intent(
        service_id=service.id,
        intent_uid="testservice.com:TestIntent:v1",
        intent_name="TestIntent",
        description="A test intent",
        input_parameters=[],
        output_parameters=[],
        endpoint="https://testservice.com/api/execute/TestIntent"
    )
    intent.tags.append(tag)
    db_session.add(intent)
    db_session.commit()
    db_session.refresh(intent)
    assert len(intent.tags) == 1
    assert intent.tags[0].name == "test"