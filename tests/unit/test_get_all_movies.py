# TODO: Feature 1
from app import list_all_movies
import pytest


def test_endpoint_movies(test_app):
    response = test_app.get("/movies")
    assert response.status_code == 200
