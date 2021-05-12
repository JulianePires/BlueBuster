import random

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
        return None, 204
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
        return None, 204
    except:
        return jsonify({"erro": "Usuário possui itens conectados a ele"})


@app.route("/users", methods=["GET"])
def get_user():
    users = models.get_user_all()
    return jsonify(users)


@app.route("/directors/name", methods=["GET"])
def get_director_by_name():
    nome_completo = serializers.directors_from_web(**request.json)
    directors = models.get_director_by_name(nome_completo)
    directors_from_db = [serializers.directors_from_db(director) for director in directors]
    return jsonify(directors_from_db)


@app.route("/genders/name", methods=["GET"])
def get_gender_by_name():
    nome = serializers.genders_from_web(**request.json)
    genders = models.get_gender_by_name(nome)
    genders_from_db = [serializers.genders_from_db(gender) for gender in genders]
    return jsonify(genders_from_db)


@app.route("/users/name", methods=["GET"])
def get_user_by_name():
    nome_completo = serializers.users_from_web(**request.json)
    users = models.get_user_by_name(nome_completo)
    users_from_db = [serializers.users_from_db(user) for user in users]
    return jsonify(users_from_db)


@app.route("/movies/name", methods=["GET"])
def get_movie_by_name():
    titulo = serializers.movies_from_web(**request.json)
    movies = models.get_movie_by_title(titulo)
    movies_from_db = [serializers.movies_from_db(movie) for movie in movies]
    return jsonify(movies_from_db)


@app.route("/locations", methods=["POST"])
def create_new_location():
    location = serializers.new_location_from_web(**request.json)
    usuarios_id = location["usuarios_id"]
    filmes_id = location["filmes_id"]
    tipo_pagamento = location["tipo_pagamento"]
    char = "1234567890abcdefghijklmnopqrstuvwxyz"
    key = random.choice(char) + random.choice(char) + random.choice(char) + random.choice(char) + random.choice(char)
    status = "em analise"
    movie = models.get_movie(filmes_id)
    id_location = models.make_location(usuarios_id, filmes_id)
    id_payment = models.create_payment(tipo_pagamento, status, key, movie["preco"], "now()", id_location)
    new_location = models.get_location_by_id(id_location)
    new_payment = models.get_payment_by_id(id_payment)
    return jsonify(serializers.locations_from_db(new_location)), jsonify(serializers.payments_from_db(new_payment))


@app.route("/locations/<int:id>", methods=["GET"])
def get_location_by_id(id):
    locations = models.get_location_by_id(id)
    location_from_db = [serializers.locations_from_db(location) for location in locations]
    return jsonify(location_from_db)


@app.route("/locations/<int:usuarios_id>", methods=["GET"])
def get_location_by_user_id(usuarios_id):
    locations = models.check_locations(usuarios_id)
    return jsonify(locations)


@app.route("/locations/<int:movie_id>", methods=["GET"])
def get_location_by_movie_id(movie_id):
    locations = models.get_locations_from_movie(movie_id)
    return jsonify(locations)


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
