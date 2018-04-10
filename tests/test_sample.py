import pytest
from .context import backend

@pytest.fixture
def test_client():
    from backend.application import app
    return app.test_client()

def test_hello_world(test_client):
    response = test_client.get('/')
    assert response.data == b'Hello, World!'