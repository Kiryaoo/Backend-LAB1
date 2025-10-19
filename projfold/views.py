from flask import Flask, jsonify
from projfold import app

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/healthcheck")
def healthcheck():
    return jsonify({"status": "ok"}), 200