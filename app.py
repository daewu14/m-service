from flask import Flask, jsonify, request
from src.ucase.hello_world import HelloWorldCase
from pkg.app.ucase import serve

app = Flask(__name__)


# A simple route to return a welcome message
@app.route('/')
def home():
    return serve(HelloWorldCase)


# A route to add two numbers
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    result = num1 + num2
    return jsonify({"result": result})


# A route to subtract two numbers
@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    result = num1 - num2
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
