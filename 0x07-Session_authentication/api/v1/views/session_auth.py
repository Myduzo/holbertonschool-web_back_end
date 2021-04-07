#!/usr/bin/env python3
""" Session authentication views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ Create a route POST /auth_session/login
    """
    email = request.form.get('email')
    if email is None:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if password is None:
        return jsonify({"error": "password missing"}), 400

    try:
        db_user = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not db_user:
        return jsonify({"error": "no user found for this email"}), 404

    for user in db_user:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    user = db_user[0]
    sessionID = auth.create_session(user.id)

    SESSION_NAME = getenv('SESSION_NAME')

    response = jsonify(user.to_json())
    response.set_cookie(SESSION_NAME, sessionID)
    return response
