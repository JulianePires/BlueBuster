from flask import Flask, jsonify, request
from main import query, execute
from decimal import Decimal

app = Flask(__name__)



if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)