import pytest
from flask.testing import FlaskClient
from app import app
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture()
def test_app() -> FlaskClient:
    return app.test_client()

def test_edit_movie_page(test_app: FlaskClient) -> None:
    # Get the movie repository and create a temporary movie for testing
    movie = get_movie_repository()
    movie.clear_db()
    temp_movie = movie.create_movie('Temporary Movie', 'Temporary Director', 3)
    
    # Make a GET request to the edit movie page for the temporary movie
    response = test_app.get(f'/movies/{temp_movie.movie_id}/edit', follow_redirects=True)

    # Check that the response status code is 200 after following the redirect
    assert response.status_code == 200
    test_insert_data(test_app)
 
def test_insert_data(test_app: FlaskClient) -> None:
    data = {
        'title': 'Kung Fu Hustle',
        'director': 'Stephen Chow',
        'rating': 5
    }

    movie = get_movie_repository()
    movie.clear_db()
    temp_movie = movie.create_movie('Temporary Movie', 'Temporary Director', 3)

    response = test_app.post(f'/movies/{temp_movie.movie_id}/update', data=data, follow_redirects=True)

    assert response.status_code == 200  
    
    data = response.data.decode()
    movies = list(get_movie_repository().get_all_movies().values())
    assert "Kung Fu Hustle" in data
    assert movies[0].title == 'Kung Fu Hustle'
    assert movies[0].director == 'Stephen Chow'
    assert movies[0].rating == 5
