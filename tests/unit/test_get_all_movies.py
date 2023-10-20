# TODO: Feature 1
import pytest
from flask.testing import FlaskClient
from app import app


@pytest.fixture()
def test_app():
    return app.test_client()


def test_get_all_movies(test_app: FlaskClient) -> None:
    response = test_app.get("/movies")
    assert response.status_code == 200


def test_get_movie_not_found(test_app: FlaskClient) -> None:
    response = test_app.get("/movies/9999")
    assert response.status_code == 404
