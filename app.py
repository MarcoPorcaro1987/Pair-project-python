from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
# from controllers import movies
from werkzeug import exceptions
import urllib.request, json
import os 

app = Flask(__name__)
CORS(app)



@app.route('/', methods=['GET'])
def home():
    # return jsonify({'message': 'Hello, Welcome!'}), 200
    url = "https://api.themoviedb.org/3/discover/movie?api_key=50141624ddf0cbc57d2265f68b3291e9"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("movies.html", movies=dict["results"] )
  

@app.route("/movies", methods=['GET'])
def get_movies_list():
    url = "https://api.themoviedb.org/3/movie/popular?api_key=50141624ddf0cbc57d2265f68b3291e9"

    response = urllib.request.urlopen(url)
    data = response.read()
    jsondata = json.loads(data)

    movie_json = []
    
    for movie in jsondata["results"]:
        movie = {
            "title": movie["title"],
            "overview": movie["overview"],
        }
        
        movie_json.append(movie)
    print(movie_json)
    return {"movie title": movie_json}

@app.route("/movies/<movie_name>", methods=[])
def search_movies(movie_name):
    movie_name = request.args['movie_name']
    url = "https://api.themoviedb.org/3/search/movie?api_key=50141624ddf0cbc57d2265f68b3291e9&language=en-US&page=1&include_adult=false&query="

    response = urllib.request.urlopen(url)
    data = response.read()
    jsondata = json.loads(data)

    movie_json = []
    
    for movie in jsondata["results"]:
        movie = {
            "title": movie["title"],
            "overview": movie["overview"],
        }
        
        movie_json.append(movie)
    print(movie_json)
    return 



@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == '__main__':
    app.run(debug=True)




# @app.route("/api/movies", methods=["GET", "POST"])
# def movies_handler():
#     fns = {
#         "GET": movies.index,
#         'POST': movies.create
#     }
#     resp, code = fns[request.method](request)
#     return jsonify(resp), code
#     # return render_template("index.html", title=f"The title of the movie is{}" )

# @app.route('/api/movies/<int:movie_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
# def movie_handler(movie_id):
#     fns = {
#         'GET': movies.show,
#         'PATCH': movies.update,
#         'PUT': movies.update,
#         'DELETE': movies.destroy
#     }
#     resp, code = fns[request.method](request, movie_id)
#     return jsonify(resp), code

