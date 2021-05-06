from main import Directors, Genders, Movies, Users

def insert_director(nome_completo):
    Directors.insert("nome_completo", nome_completo)

def insert_gender(nome):
    Genders.insert("nome", nome)

def insert_movie(titulo, ano, classificacao, preco, diretores_id, generos_id):
    Movies.insert(["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"], [titulo, ano, classificacao, preco, diretores_id, generos_id])

def insert_user(nome_completo, CPF):
    Users.insert(["nome_completo", "CPF"], [nome_completo, CPF])

def update_director(key_value, novo_nome):
    Directors.update(key_value, "nome_completo", novo_nome)

def update_gender(key_value, novo_nome):
    Genders.update(key_value, "nome", novo_nome)

def update_movie(key_value, titulo, ano, classificacao, preco, diretores_id, generos_id):
    Movies.update(key_value, ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"], [titulo, ano, classificacao, preco, diretores_id, generos_id])

def update_user(key_value, nome_completo, CPF):
    Users.update(key_value, ["nome_completo", "CPF"], [nome_completo, CPF])

def delete_director(nome_completo):
    Directors.delete("nome_completo", nome_completo)

def delete_gender(nome):
    Genders.delete("nome", nome)

def delete_movie(column, value):
    Movies.delete(column, value)

def delete_user(column, value):
    Users.delete(column, value)

def select_director(key_value):
    Directors.select(key_value)

def select_gender(key_value):
    Genders.select(key_value)

def select_movie(key_value):
    Movies.select(key_value)

def select_user(key_value):
    Users.select(key_value)