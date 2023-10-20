# TODO: Feature 1
from app import app
import pytest

@pytest.fixture()
def test_app():
    return app.test_client()

def test_endpoint_movies(test_app):
    response = test_app.get('/movies')
    assert response.status_code == 200