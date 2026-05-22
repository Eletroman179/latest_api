from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

FILE = "latest.json"

def load():
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)
    return {}

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

@app.route("/send", methods=["POST"])
def send():
    data = request.json or {}

    save(data)

    return {"saved": True}

@app.route("/latest")
def latest():
    return jsonify(load())