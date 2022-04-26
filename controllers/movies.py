from werkzeug.exceptions import BadRequest

movies = [
    {"id":1, "title": "Once upon a time in America", "year": 1984},
    {"id":2, "title": "She's a man", "year": 2006}
]

def index(req):
    return [c for c in movies], 200

def show(req, uid):
    return find_by_uid(uid), 200


def create(req):
    new_movie = req.get_json()
    new_movie['id'] = sorted([c['id'] for c in movies])[-1] + 1
    movies.append(new_movie)
    return new_movie, 201

def update(req, uid):
    movie = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        movie[key] = val
    return movie, 200

def destroy(req, uid):
    movie = find_by_uid(uid)
    movies.remove(movie)
    return movie, 204

def find_by_uid(uid):
    try:
        return next(movie for movie in movies if movie['id'] == uid)
    except:
        raise BadRequest(f"We don't have a movie with id {uid}!")

