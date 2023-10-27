# TODO: Feature 6
from src.repositories.movie_repository import get_movie_repository

def test_delete_movie():
    movies_db_copy = get_movie_repository()
    movies_db_copy.clear_db()
    # Check that movie is not in database before addition
    assert (movies_db_copy.get_movie_by_title('The Godfather') == None)
    movies_db_copy.create_movie('The Godfather', 'Francis Ford Coppola', 5)
    new_id = movies_db_copy.get_movie_by_title('The Godfather').movie_id
    # Check that movie is within database by two parameters
    assert (movies_db_copy.get_movie_by_title('The Godfather') == movies_db_copy.get_movie_by_id(new_id))
    movies_db_copy.delete_movie(new_id)
    # Check that movie is not in database after deletion
    assert (movies_db_copy.get_movie_by_title('The Godfather') == None)