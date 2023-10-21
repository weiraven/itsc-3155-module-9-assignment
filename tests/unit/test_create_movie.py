# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository

def test_create_movie():
    movie = get_movie_repository()
    movie.create_movie('Kung Fu Hustle','Stephen Chow', 5)
    movies = list(movie.get_all_movies().values())


    assert movies[0].title == 'Kung Fu Hustle'
    assert movies[0].director == 'Stephen Chow'
    assert movies[0].rating == 5