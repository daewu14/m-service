from flask import Flask, jsonify, request, Blueprint
from src.ucase.hello_world import HelloWorldCase
from pkg.app.ucase import serve

app = Flask(__name__)
apiV1 = "/api/v1"

@app.route("/api/v1/", methods=['GET'])
def home(): return serve(HelloWorldCase)