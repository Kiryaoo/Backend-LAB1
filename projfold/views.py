from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/healthcheck")
def healthcheck():
    return jsonify({"status": "ok"}), 200