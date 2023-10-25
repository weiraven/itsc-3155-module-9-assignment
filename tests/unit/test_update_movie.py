from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository


def test_update_movie():

    movie = get_movie_repository()
    movie.clear_db

    movie.create_movie('Star Wars', 'George Lucas', 5)
    movies = list(movie.get_all_movies().values())
    id = int(movies[0].movie_id)

    get_movie_repository().update_movie(id, 'The Goonies', 'Richard Donner', 4)
    assert movies[0].title == 'The Goonies'
    assert movies[0].director == 'Richard Donner'
    assert movies[0].rating == 4

    
