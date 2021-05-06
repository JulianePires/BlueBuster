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

def update_movie(key_value, columns, values):
    Movies.update(key_value, columns, values)

def update_user(key_value, columns, values):
    Users.update(key_value, columns, values)