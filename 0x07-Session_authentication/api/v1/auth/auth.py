#!/usr/bin/env python3
"""Authentication File
"""
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth public method
        - returns False - path and excluded_paths
        will be used later, now, you don’t need to take care of them
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if path[-1] == '/' and path in excluded_paths:
            return False

        if path[-1] != '/' and path + '/' in excluded_paths:
            return False

        if path not in excluded_paths:
            return True

        if path in excluded_paths or excluded_paths == ["/api/v1/status/"]:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header public method
        - returns None - request will be the Flask request object
        """
        if request is None or 'Authorization' not in request.headers:
            return None

        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user public method
        - returns None - request will be the Flask request object
        """
        return None

    def session_cookie(self, request=None):
        """ instance method that returns
        a cookie value from a request.
        """
        if request is None:
            return None

        cookieKey = os.getenv('SESSION_NAME')
        return request.cookies.get(cookieKey)
