from flask import Flask, jsonify, request


app = Flask(__name__)

apiresponse = [
    {"status": "ok"}
]

@app.get("/healthcheck")
def apireturn():
    return jsonify(apiresponse)