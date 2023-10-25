# TODO: Feature 4
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_id():
    movie = get_movie_repository()
    movie.clear_db()
    movie.create_movie('Everything Everywhere All At Once','Daniel Kwan', 5)
    movies = list(movie.get_all_movies().values())
    id = movie.get_movie_by_id(movies[0].movie_id)

    assert movies[0].title == 'Everything Everywhere All At Once'
    assert movies[0].director == 'Daniel Kwan'
    assert movies[0].rating == 5
    assert movies[0] == id