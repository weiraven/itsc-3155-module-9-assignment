# TODO: Feature 1
import pytest
from flask.testing import FlaskClient
from app import app


@pytest.fixture()
def test_app() -> FlaskClient:
    return app.test_client()


def test_endpoint_movies(test_app: FlaskClient) -> None:
    response = test_app.get("/movies")
    assert response.status_code == 200
