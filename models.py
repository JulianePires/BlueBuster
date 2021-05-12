from main import Directors, Genders, Movies, Users


def insert_director(nome_completo):
    return Directors().insert([nome_completo])


def insert_gender(nome):
    return Genders().insert([nome])


def insert_movie(titulo, ano, classificacao, preco, diretores_id, generos_id):
    return Movies().insert([titulo, ano, classificacao, preco, diretores_id, generos_id])


def insert_user(nome_completo, CPF):
    return Users().insert([nome_completo, CPF])


def update_director(key_value, novo_nome):
    Directors().update(key_value, novo_nome)


def update_gender(key_value, novo_nome):
    Genders().update(key_value, novo_nome)


def update_movie(key_value, titulo, ano, classificacao, preco, diretores_id, generos_id):
    Movies().update(key_value, [titulo, ano, classificacao, preco, diretores_id, generos_id])


def update_user(key_value, nome_completo, CPF):
    Users().update(key_value, [nome_completo, CPF])


def delete_director(key_value):
    Directors().delete(key_value)


def delete_gender(key_value):
    Genders().delete(key_value)


def delete_movie(key_value):
    Movies().delete(key_value)


def delete_user(key_value):
    Users().delete(key_value)


def get_director(key_value):
    return Directors().select(key_value)[0]


def get_gender(key_value):
    return Genders().select(key_value)[0]


def get_movie(key_value):
    return Movies().select(key_value)[0]


def get_user(key_value):
    return Users().select(key_value)[0]


def get_director_all():
    return Directors().select_all()


def get_gender_all():
    return Genders().select_all()


def get_movie_all():
    return Movies().select_all()


def get_user_all():
    return Users().select_all()


def get_director_by_name(nome_completo):
    return Directors().select_like("nome_completo", nome_completo)


def get_gender_by_name(nome):
    return Genders().select_like("nome", nome)


def get_movie_by_title(titulo):
    return Movies().select_like("titulo", titulo)


def get_user_by_name(nome_completo):
    return Users().select_like("nome_completo", nome_completo)