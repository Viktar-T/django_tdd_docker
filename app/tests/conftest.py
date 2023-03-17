import pytest

from movies.models import Movies


@pytest.fixture(scope="function")
def add_movie():
    def _add_movie(title, genre, year):
        movie = Movies.objects.create(title=title, genre=genre, year=year)
        return movie

    return _add_movie
