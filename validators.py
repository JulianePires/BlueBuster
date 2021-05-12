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
    if len(ano) != 4 and 1895 > ano > 2021:
        return False
    if 18 < classificacao < 0:
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


def valida_location(data_inicio, data_fim, filmes_id, usuarios_id):
    if filmes_id < 1:
        return False
    if usuarios_id < 1:
        return False
    if data_fim < data_inicio:
        return False
    return True


def valida_payment(tipo, status, codigo_pagamento, valor, locacoes_id):
    if len(tipo) == 0 and tipo != "debito" and tipo != "credito" and tipo != "paypal":
        return False
    if len(status) == 0 and status != "aprovado" and status != "em analise" and status != "reprovado":
        return False
    if len(codigo_pagamento) == 0:
        return False
    if valor < 2.0:
        return False
    if locacoes_id < 1:
        return False
    return True