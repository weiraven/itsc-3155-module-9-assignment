class Movie:
    """A movie holds a title, director, and rating"""

    def __init__(self, movie_id: int, title: str, director: str, rating: int) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.rating = rating
