# TODO: Feature 2
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
    movie_repository.clear_db()
    response = test_app.get("/movies")
    test_insert_data(test_app)

    
def test_insert_data(test_app: FlaskClient) -> None:
    data = {
        'movie': 'Kung Fu Hustle',
        'director': 'Stephen Chow',
        'rating': 5
    }

    response = test_app.post('/movies', data=data, follow_redirects=True)

    assert response.status_code == 200  
    
    data = response.data.decode()
    movies = list(get_movie_repository().get_all_movies().values())
    assert "Kung Fu Hustle" in data
    assert movies[0].title == 'Kung Fu Hustle'
    assert movies[0].director == 'Stephen Chow'
    assert movies[0].rating == 5