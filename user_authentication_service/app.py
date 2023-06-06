#!/usr/bin/env python3

from flask import Flask, jsonify, request, abort, make_response
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
        return jsonify({"email": email,
                        "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'])
def Login():
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return None
    if not password:
        return None
    valid_login = AUTH.valid_login(email, password)
    if valid_login:
        newses = AUTH.create_session(email)
        response = make_response()
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", newses)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")