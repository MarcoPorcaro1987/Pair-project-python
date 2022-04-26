from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from controllers import movies
from werkzeug import exceptions
# from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
# mongo = PyMongo(app)


@app.route('/')
def home():
    return jsonify({'message': 'Hello, Welcome!'}), 200
      # online_users = mongo.db.users.find({"online": True})
    # return render_template("index.html",
    #     online_users=online_users)


@app.route("/api/movies", methods=["GET", "POST"])
def movies_handler():
    fns = {
        "GET": movies.index,
        'POST': movies.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code
    

@app.route('/api/movies/<int:movie_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def movie_handler(movie_id):
    fns = {
        'GET': movies.show,
        'PATCH': movies.update,
        'PUT': movies.update,
        'DELETE': movies.destroy
    }
    resp, code = fns[request.method](request, movie_id)
    return jsonify(resp), code

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
