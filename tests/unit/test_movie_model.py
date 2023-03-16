from src.models.movie import Movie


def test_movie_model():
    movie = Movie(123, 'Star Wars', 'George Lucas', 5)

    assert type(movie) == Movie
    assert movie.movie_id == 123
    assert movie.title == 'Star Wars'
    assert movie.director == 'George Lucas'
    assert movie.rating == 5
