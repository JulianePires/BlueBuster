from mysql.connector import connect

show_schemas = "SHOW SCHEMAS"

configuracoes_bd = {
    "host": "localhost",
    "user": "root",
    "password": "Polinomio110501",
    "database": "locadora"
}

def execute(sql, params=None):
    with connect(**configuracoes_bd) as conn:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            conn.commit()
            return cursor.lastrowid

def query(sql, params=None):
    with connect(**configuracoes_bd) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()

class Table:
    def create_table(self):
        execute(f"""CREATE TABLE {self.name} (
            {", ".join([f"{column} {typeof}" for column, typeof in self.columns.items()])}""")
    def insert(self, columns, values):
       return execute(f"""INSERT IGNORE INTO {self.nome} (
            {",".join(columns)}) VALUES ({",".join(['%s' for value in values])})""", values)
    def delete(self, column, value):
        execute(f"""DELETE FROM {self.name} WHERE {column} = %s""", (value,))
    def update(self, key_value, columns, values):
        sets = [f"{column} = %s" for column in columns]
        execute(f"""UPDATE {self.name} SET {",".join(sets)} WHERE id = %s""", values + [key_value])
    def select(self, key_value=1, limit=100, offset=0):
        return query(f"""SELECT * FROM {self.name} WHERE id = %s LIMIT {limit} offset {offset}""", (key_value,))

class Users(Table):
    name: "usuarios"

class Payments(Table):
    name: "pagamento"

class Locations(Table):
    name: "locacoes"

class Genders(Table):
    name: "generos"

class Movies(Table):
    name: "filmes"

class Directors(Table):
    name: "diretores"