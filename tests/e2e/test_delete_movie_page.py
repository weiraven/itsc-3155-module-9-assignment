import pytest
from flask.testing import FlaskClient
from app import app
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture()
def test_app():
    return app.test_client()

def clear_movie_cache():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()

def test_movie_input(test_app: FlaskClient) -> int:
    clear_movie_cache()

    data = {
        'movie': 'The Godfather',
        'director': 'Francis Ford Coppola',
        'rating': 5
    }

    response = test_app.post('/movies', data=data, follow_redirects=True)
    assert response.status_code == 200

    movie_List = list(get_movie_repository().get_all_movies().values())
    assert movie_List[0].title == 'The Godfather'
    assert movie_List[0].director == 'Francis Ford Coppola'
    assert movie_List[0].rating == 5

    return movie_List[0].movie_id

def test_delete_movie(test_app: FlaskClient) -> None:
    
    movie_id = test_movie_input(test_app)
    response = test_app.post(f'/movies/{movie_id}/delete')
    
    assert response.status_code == 302
