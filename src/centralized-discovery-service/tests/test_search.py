# tests/test_search.py

import pytest
from app.models import Service, Intent

@pytest.fixture
def setup_data(db_session):
    """Set up test data in the database."""
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
        description="A test intent that searches for properties",
        input_parameters=[],
        output_parameters=[],
        endpoint="https://testservice.com/api/execute/TestIntent"
    )
    db_session.add(intent)
    db_session.commit()

@pytest.mark.parametrize("query,expected_count", [
    ("searches for properties", 1),
    ("test intent", 1),
    ("nonexistent query", 0),
])
def test_search_intents_by_query(client, setup_data, query, expected_count):
    """Test searching intents using natural language queries."""
    response = client.get("/api/search/", params={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == expected_count