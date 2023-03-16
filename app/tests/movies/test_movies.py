import pytest

from app.movies.models import Movies



@pytest.mark.django_db
def test_movie_model():
    movie = Movies(title="Raising Arizona", genre="comedy", year="1987")
    movie.save()

    # movie = Movies.objects.create(title="Raising Arizona", genre="comedy", year="1987")

    assert movie.title == "Raising Arizona"
    assert movie.genre == "comedy"
    assert movie.year == "1987"
    assert movie.created_date
    assert movie.updated_date
    assert str(movie) == movie.title


