#!/usr/bin/env python3

from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'])
def hello_world():
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def Register():
    """If the user does not exist, the end-point
    should register it and respond"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": "<registered email>",
                        "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
