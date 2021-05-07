from flask import Flask, jsonify, request
import models
import serializers
from validators import valida_user, valida_movie, valida_gender, valida_director

app = Flask(__name__)

@app.route("/directors", methods=["GET"])
def get_director():
    nome_completo = serializers.directors_from_web(**request.args)
    directors = models.get_director(nome_completo)
    director_from_db = [serializers.directors_from_db(director) for director in directors]
    return jsonify(director_from_db)

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
def delete_user(id):
    try:
        models.delete_director(id)
        return None, 204
    except:
        return jsonify({"erro": "Diretor possui itens conectados a ele"})

@app.route("/genders", methods=["GET"])
def get_gender():
    nome = serializers.genders_from_web(**request.args)
    genders = models.get_gender(nome)
    gender_from_db = [serializers.genders_from_db(gender) for gender in genders]
    return jsonify(gender_from_db)

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
    titulo = serializers.movies_from_web(**request.args)
    movies = models.get_movie(titulo)
    movie_from_db = [serializers.movies_from_db(movie) for movie in movies]
    return jsonify(movie_from_db)

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
        return None, 204
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

@app.route("/usuarios", methods=["GET"])
def get_user():
    nome_completo = serializers.users_from_web(**request.args)
    users = models.get_user(nome_completo)
    users_from_db = [serializers.users_from_db(user) for user in users]
    return jsonify(users_from_db)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
