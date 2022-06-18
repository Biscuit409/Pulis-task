from flask import Flask, jsonify, request


app = Flask(__name__)

apiresponse = {"status": "ok"}

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/healthcheck", methods=['GET', 'POST'])
def apireturn():
    return jsonify(apiresponse)

