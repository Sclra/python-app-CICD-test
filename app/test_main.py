import pytest
from main import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_items(client):
    response = client.get("/items")
    assert response.status_code == 200
    assert "items" in response.json
