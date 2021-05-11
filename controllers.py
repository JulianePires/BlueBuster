from flask import Flask, jsonify, request
import models
import serializers
from validators import valida_user, valida_movie, valida_gender, valida_director

app = Flask(__name__)


@app.route("/directors", methods=["GET"])
def get_director():
    directors = models.get_director_all()
    return jsonify(directors)


@app.route("/directors", methods=["POST"])
def insert_director():
    director = serializers.directors_from_web(**request.json)
    if valida_director(**director):
        id_director = models.insert_director(**director)
        inserted_director = models.get_director(id_director)
        return jsonify(serializers.directors_from_db(inserted_director))
    else:
        return jsonify({"erro": "Diretor inválido"})


@app.route("/directors/<int:id>", methods=["PUT", "PATCH"])
def update_directors(id):
    director = serializers.directors_from_web(**request.json)
    if valida_director(**director):
        models.update_director(id, **director)
        inserted_director = models.get_director(id)
        return jsonify(serializers.directors_from_db(inserted_director))
    else:
        return jsonify({"erro": "Diretor inválido"})


@app.route("/directors/<int:id>", methods=["DELETE"])
def delete_director(id):
    try:
        models.delete_director(id)
        return "", 204
    except:
        return jsonify({"erro": "Diretor possui itens conectados a ele"})


@app.route("/genders", methods=["GET"])
def get_gender():
    genders = models.get_gender_all()
    return jsonify(genders)


@app.route("/genders", methods=["POST"])
def insert_gender():
    gender = serializers.genders_from_web(**request.json)
    if valida_gender(**gender):
        id_gender = models.insert_gender(**gender)
        inserted_gender = models.get_gender(id_gender)
        return jsonify(serializers.genders_from_db(inserted_gender))
    else:
        return jsonify({"erro": "Gênero inválido"})


@app.route("/genders/<int:id>", methods=["PUT", "PATCH"])
def update_genders(id):
    gender = serializers.genders_from_web(**request.json)
    if valida_gender(**gender):
        models.update_gender(id, **gender)
        inserted_gender = models.get_gender(id)
        return jsonify(serializers.genders_from_db(inserted_gender))
    else:
        return jsonify({"erro": "Gênero inválido"})


@app.route("/genders/<int:id>", methods=["DELETE"])
def delete_gender(id):
    try:
        models.delete_gender(id)
        return "", 204
    except:
        return jsonify({"erro": "Gênero possui itens conectados a ele"})


@app.route("/movies", methods=["GET"])
def get_movie():
    movies = models.get_movie_all()
    return jsonify(movies)


@app.route("/movies", methods=["POST"])
def insert_movie():
    movie = serializers.movies_from_web(**request.json)
    if valida_movie(**movie):
        id_movie = models.insert_movie(**movie)
        inserted_movie = models.get_movie(id_movie)
        return jsonify(serializers.movies_from_db(inserted_movie))
    else:
        return jsonify({"erro": "Filme inválido"})


@app.route("/movies/<int:id>", methods=["PUT", "PATCH"])
def update_movie(id):
    movie = serializers.movies_from_web(**request.json)
    if valida_movie(**movie):
        models.update_movie(id, **movie)
        inserted_movie = models.get_movie(id)
        return jsonify(serializers.movies_from_db(inserted_movie))
    else:
        return jsonify({"erro": "Filme inválido"})


@app.route("/movies/<int:id>", methods=["DELETE"])
def delete_movie(id):
    try:
        models.delete_movie(id)
        return "", 204
    except:
        return jsonify({"erro": "Filme possui itens conectados a ele"})


@app.route("/users", methods=["POST"])
def insert_user():
    user = serializers.users_from_web(**request.json)
    if valida_user(**user):
        id_usuario = models.insert_user(**user)
        inserted_user = models.get_user(id_usuario)
        return jsonify(serializers.users_from_db(inserted_user))
    else:
        return jsonify({"erro": "Usuário inválido"})


@app.route("/users/<int:id>", methods=["PUT", "PATCH"])
def update_users(id):
    user = serializers.users_from_web(**request.json)
    if valida_user(**user):
        models.update_user(id, **user)
        inserted_user = models.get_user(id)
        return jsonify(serializers.users_from_db(inserted_user))
    else:
        return jsonify({"erro": "Usuário inválido"})


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    try:
        models.delete_user(id)
        return "", 204
    except:
        return jsonify({"erro": "Usuário possui itens conectados a ele"})


@app.route("/usuarios", methods=["GET"])
def get_user():
    users = models.get_user_all()
    return jsonify(users)


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
