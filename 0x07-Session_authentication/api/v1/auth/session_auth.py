#!/usr/bin/env python3
"""Session authentication file
"""
from api.v1.auth.auth import Auth
import uuid
import os
from models.user import User
from flask import Flask, request, jsonify


class SessionAuth(Auth):
    """ SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ instance method that creates a Session ID
        for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        SessionID = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id.update({SessionID: user_id})

        return SessionID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ instance method that returns the value (the User ID)
        for the key session_id in the dictionary user_id_by_session_id.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ instance method that returns
        a User instance based on a cookie value.
        """
        cookieValue = self.session_cookie(request)
        if cookieValue is None:
            return None

        UserID = self.user_id_for_session_id(cookieValue)
        return User.get(UserID)
