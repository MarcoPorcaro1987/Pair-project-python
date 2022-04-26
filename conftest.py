import pytest
import app
from controllers import movies

@pytest.fixture
def api(monkeypatch):
    test_movies = [
        {'id': 1, 'title': 'Test Film 1', 'year': 1247},
        {'id': 2, 'title': 'Test Film 2', 'year': 3634}
    ]
    monkeypatch.setattr(movies, "movies", test_movies)
    api = app.app.test_client()
    return api
