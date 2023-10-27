# TODO: Feature 1
import pytest
from flask.testing import FlaskClient
from app import app
from src.repositories.movie_repository import get_movie_repository


@pytest.fixture()
def test_app():
    return app.test_client()


def test_no_movies_in_view(test_app: FlaskClient) -> None:
    response = test_app.get("/movies")
    data = response.data.decode()
    assert "No movies have been registered yet.</h2>" in data
    assert response.status_code == 200


def test_movies_in_view(test_app: FlaskClient) -> None:
    movie_repository = get_movie_repository()
    movie_repository.create_movie("dookie", "cheesee", 10)
    response = test_app.get("/movies")
    data = response.data.decode()
    assert "dookie</td>" in data
    assert response.status_code == 200
    movie_repository.clear_db()
