def valida_director(nome_completo):
    if len(nome_completo) == 0:
        return False
    return True

def valida_gender(nome):
    if len(nome) == 0:
        return False
    return True

def valida_movie(titulo, ano, classificacao, preco, diretores_id, generos_id):
    if len(titulo) == 0:
        return False
    if len(ano) != 4 and ano < 1895 and ano > 2021:
        return False
    if classificacao > 18 and classificacao < 0:
        return False
    if preco == 0:
        return False
    if diretores_id < 1:
        return False
    if generos_id < 1:
        return False
    return True

def valida_user(nome_completo, CPF):
    if len(nome_completo) == 0:
        return False

    if len(CPF) != 14:
        return False

    return True