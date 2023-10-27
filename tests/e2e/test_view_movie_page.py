# TODO: Feature 4
import pytest
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository
from app import app, movie_repository

@pytest.fixture()
def test_app() -> FlaskClient:
    return app.test_client()

def test_get_single_movie_exists(test_app: FlaskClient) -> None:
    movie = get_movie_repository()
    movie.clear_db()
    movie.create_movie('Kung Fu Hustle','Stephen Chow', 5)
    movies = list(movie.get_all_movies().values())
    response = test_app.get('/movies/' + str(movies[0].movie_id))
    assert response.status_code == 200
    assert b'Kung Fu Hustle' in response.data  # check if movie title is in the response

def test_get_single_movie_not_found(test_app: FlaskClient) -> None:
    response = test_app.get('/movies/999999')  # assuming 999999 does not exist in your repository
    assert response.status_code == 302  # check if it's a redirect
    assert '/movies' in response.location  # check if it redirects to the correct URL