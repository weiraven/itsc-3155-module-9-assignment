# TODO: Feature 3

from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

def test_search_movie():

    title = 'Shrek'
    director = 'Will Smith'
    rating = 5

    movie_repo = get_movie_repository()
    movie_repo.clear_db()

    movie_repo.create_movie(title, director, rating)

    found = movie_repo.get_movie_by_title(title)
    miss = movie_repo.get_movie_by_title('This is not a movie' + title)

    assert found.director == director
    assert found.rating == rating
    assert miss == None