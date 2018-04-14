import pytest
from .context import backend

@pytest.fixture
def test_client():
    return backend.app.test_client()


def test_available_ratings(test_client):
    response = test_client.get('/api/availableRatings')

    assert response.status_code == 200


def test_available_ratings_filtered(test_client):
    response = test_client.get('/api/availableRatings?typeOfDay=Wochentag')
    assert response.status_code == 200


def test_available_days(test_client):
    response = test_client.get('/api/availableDays')
    assert response.status_code == 200


def test_get_rating(test_client):
    response = test_client.get('/api/rating/0')
    assert response.status_code == 200


def test_get_rating_nonexistent(test_client):
    response = test_client.get('/api/rating/1000')
    assert response.status_code == 404