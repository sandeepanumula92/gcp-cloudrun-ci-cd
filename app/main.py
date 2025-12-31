from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(service="devops-cloudrun-app", status="running")

@app.route("/health")
def health():
    return jsonify(status="healthy")
