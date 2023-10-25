from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/movies")
def list_all_movies():
    # TODO: Feature 1
    # Gets all movie from the repository
    movies = movie_repository.get_all_movies().values()
    return render_template(
        "list_all_movies.html", list_movies_active=True, movies=movies
    )

@app.get("/movies/new")
def create_movies_form():
    return render_template("create_movies_form.html", create_rating_active=True)

@app.post("/movies")
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    title = request.form['movie']
    director = request.form['director']
    rating = int(request.form['rating'])
    movie_repository.create_movie(title,director,rating)
    return redirect('/movies')

@app.get("/movies/search")
def search_movies():
    # TODO: Feature 3
    return render_template("search_movies.html", search_active=True)

@app.get("/movies/<int:movie_id>")
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    # Fetch movie from the movie_repository
    movie = movie_repository.get_movie_by_id(movie_id)
    if movie is None:
        # If the movie isn't found, redirect to the list all movies page
        return redirect('/movies')
    # Pass the movie to the page
    return render_template("get_single_movie.html", movie=movie)

@app.get("/movies/<int:movie_id>/edit")
def get_edit_movies_page(movie_id: int):
 # Retrieve the movie from the repository
    movie = movie_repository.get_movie_by_id(movie_id)
    
    if movie is None:
        # If the movie isn't found, redirect to the list all movies page
        return redirect('/movies')
    
    return render_template("edit_movies_form.html", movie=movie)

@app.post("/movies/<int:movie_id>/update")
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    
    # Retrieve the movie from the repository
    movie = movie_repository.get_movie_by_id(movie_id)
    
    if movie is None:
        # If the movie isn't found, redirect to the list all movies page
        return redirect('/movies')

    # Update the movie details
    movie.title = request.form['title']
    movie.director = request.form['director']
    movie.rating = int(request.form['rating'])

    # Save the updated movie back to the repository
    movie_repository.update_movie(movie_id, movie.title, movie.director, movie.rating)
    
    return redirect('/movies')

@app.post("/movies/<int:movie_id>/delete")
def delete_movie(movie_id: int):
    # TODO: Feature 6
    # Deletes the movie from the database by its id then returns to movie page
    movie_repository.delete_movie(movie_id)
    return redirect('/movies')