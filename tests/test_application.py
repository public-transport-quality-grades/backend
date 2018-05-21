import pytest
from .context import backend


@pytest.fixture
def test_client():
    return backend.app.test_client()


def test_available_gradings(test_client):
    response = test_client.get('/api/gradings')
    assert response.status_code == 200


def test_available_gradings_filtered(test_client):
    response = test_client.get('/api/gradings?typeOfDay=Saturday')
    assert response.status_code == 200


def test_available_days(test_client):
    response = test_client.get('/api/typesOfDays')
    assert response.status_code == 200


def test_get_grading_nonexistent(test_client):
    response = test_client.get('/api/rating/1000')
    assert response.status_code == 404
