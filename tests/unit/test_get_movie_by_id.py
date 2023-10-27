# TODO: Feature 4
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_id():
    movie = get_movie_repository()
    movie.clear_db()
    movie.create_movie('Everything Everywhere All At Once','Daniel Kwan', 5)
    movies = list(movie.get_all_movies().values())
    movie = movie.get_movie_by_id(movies[0].movie_id)

    assert movie.title == 'Everything Everywhere All At Once'
    assert movie.director == 'Daniel Kwan'
    assert movie.rating == 5