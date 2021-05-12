from MySQLdb import InternalError
from main import execute, query, bd_configurations

bd_configurations = ""
bd_configurations = {
    "host": "localhost",
    "user": "root",
    "password": "Polinomio110501",
    "database": "locadora"
}


def test_execute():
    try:
        execute("""CREATE TABLE teste (id int primary key auto_increment)""")
        execute("""DROP TABLE teste""")
        assert True
    except:
        assert False
    try:
        execute("""SHOW tables""")
        assert False
    except InternalError:
        assert True
