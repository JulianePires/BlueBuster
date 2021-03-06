def directors_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
    }


def directors_from_db(director):
    return {
        "nome_completo": director["nome_completo"],
    }


def genders_from_web(**kwargs):
    return {
        "nome": kwargs["nome"] if "nome" in kwargs else "",
    }


def genders_from_db(gender):
    return {
        "nome": gender["nome"],
    }


def movies_from_web(**kwargs):
    return {
        "titulo": kwargs["titulo"] if "titulo" in kwargs else "",
        "ano": kwargs["ano"] if "ano" in kwargs else "",
        "classificacao": kwargs["classificacao"] if "classificacao" in kwargs else "",
        "preco": kwargs["preco"] if "preco" in kwargs else "",
        "diretores_id": kwargs["diretores_id"] if "diretores_id" in kwargs else "",
        "generos_id": kwargs["generos_id"] if "generos_id" in kwargs else ""
    }


def movies_from_db(movie):
    return {
        "titulo": movie["titulo"],
        "ano": movie["ano"],
        "classificacao": movie["classificacao"],
        "preco": str(movie["preco"]),
        "diretores_id": movie["diretores_id"],
        "generos_id": movie["generos_id"]
    }


def users_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "CPF": kwargs["CPF"] if "CPF" in kwargs else "",
    }


def users_from_db(user):
    return {
        "nome_completo": user["nome_completo"],
        "CPF": user["CPF"]
    }


def new_location_from_web(**kwargs):
    return {
        "usuarios_id": kwargs["usuarios_id"] if "usuarios_id" in kwargs else "",
        "filmes_id": kwargs["filmes_id"] if "filmes_id" in kwargs else "",
        "tipo_pagamento": kwargs["status_pagamento"] if "status_pagamento" in kwargs else "",
    }


def locations_from_db(location):
    return {
        "data_inicio": location["data_inicio"],
        "data_fim": location["data_fim"],
        "filmes_id": location["filmes_id"],
        "usuarios_id": location["usuarios_id"],
    }


def payments_from_db(payment):
    return {
        "tipo": payment["tipo"],
        "status": payment["status"],
        "codigo_pagamento": payment["codigo_pagamento"],
        "valor": str(payment["valor"]),
        "data": (payment["data"]).strftime('%d-%m-%Y %H:%M:%S'),
        "locacoes_id": payment["locacoes_id"]
    }