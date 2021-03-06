from mysql.connector import connect

show_schemas = "SHOW SCHEMAS"

bd_configurations = {
    "host": "localhost",
    "user": "root",
    "password": "Polinomio110501",
    "database": "locadora"
}


def execute(sql, params=None):
    with connect(**bd_configurations) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            conn.commit()
            return cursor.lastrowid


def query(sql, params=None):
    with connect(**bd_configurations) as conn:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()


class Table:

    def create_table(self):
        execute(f"""CREATE TABLE {self.name} (
            {", ".join([f"{column} {typeof}" for column, typeof in self.columns])}""")

    def insert(self, values):
        return execute(f"""INSERT INTO {self.name} (
            {",".join(self.columns)}) VALUES ({", ".join(["%s" for value in values])})""", values)

    def delete(self, key_value):
        execute(f"""DELETE FROM {self.name} WHERE id = %s""", key_value)

    def update(self, key_value, values):
        sets = [f"{column} = %s" for column in self.columns]
        execute(f"""UPDATE {self.name} SET {",".join(sets)} WHERE id = %s""", values + [key_value])

    def select(self, key_value=1, limit=1000, offset=0):
        return query(f"""SELECT * FROM {self.name} WHERE id = %s LIMIT {limit} offset {offset}""", (key_value,))

    def select_all(self):
        return query(f"""SELECT * FROM {self.name} LIMIT 1000 offset 0""")

    def select_like(self, column, value):
        return query(f"""SELECT * FROM {self.name} WHERE {column} LIKE %s""", value)

    def select_location_by_id(self, key_value):
        return query(f""""SELECT 
                            usuarios.nome_completo, 
                            filmes.titulo, 
                            date_format(data_inicio, 
                            "%d%m/%Y") data_locacao, 
                            pagamento.status
                        FROM locacoes 
                        INNER JOIN usuarios ON locacoes.usuarios_id = usuarios.id 
                        INNER JOIN filmes ON locacoes.filmes_id = filmes.id
                        INNER JOIN pagamento ON locacoes.id = pagamento.locacoes_id
                        WHERE locacoes.id = %s""", key_value)

    def select_location_by_userid(self, key_value):
        return query(f""""SELECT 
                            usuarios.nome_completo, 
                            filmes.titulo, 
                            date_format(data_inicio, 
                            "%d%m/%Y") data_locacao, 
                        FROM locacoes 
                        INNER JOIN usuarios ON locacoes.usuarios_id = %s 
                        INNER JOIN filmes ON locacoes.filmes_id = filmes.id
                        INNER JOIN pagamento ON locacoes.id = pagamento.locacoes_id
                        """, key_value)

    def select_location_by_movieid(self, key_value):
        return query(f""""SELECT 
                            usuarios.nome_completo, 
                            filmes.titulo, 
                            date_format(data_inicio, 
                            "%d%m/%Y") data_locacao, 
                        FROM locacoes 
                        INNER JOIN usuarios ON locacoes.usuarios_id = usuarios.id
                        INNER JOIN filmes ON locacoes.filmes_id = %s
                        INNER JOIN pagamento ON locacoes.id = pagamento.locacoes_id
                        """, key_value)

class Users(Table):
    name = "usuarios"
    columns = ("nome_completo", "CPF")


class Payments(Table):
    name = "pagamento"
    columns = ("tipo", "status", "codigo_pagamento", "valor", "data", "locacoes_id")


class Locations(Table):
    name = "locacoes"
    columns = ("data_inicio", "data_fim", "filmes_id", "usuarios_id")

class Genders(Table):
    name = "generos"
    columns = ("nome",)


class Movies(Table):
    name = "filmes"
    columns = ("titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id")


class Directors(Table):
    name = "diretores"
    columns = ("nome_completo",)
