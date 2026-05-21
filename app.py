from flask import Flask, request, jsonify

app = Flask(__name__)

latest = {}

@app.route("/send", methods=["POST"])
def send():
    global latest

    latest = request.json or {}

    return {"saved": True}

@app.route("/latest")
def get_latest():
    return jsonify(latest)
