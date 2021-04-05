#!/usr/bin/env python3
"""Basic auth
"""
from typing import TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User


class BasicAuth(Auth):
    """BasicAuth class
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header
        for a Basic Authentication
        """
        auth = authorization_header

        if auth is None or not isinstance(auth, str):
            return None

        if not auth.startswith('Basic '):
            return None

        return auth[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string
        base64_authorization_header
        """
        base_auth = base64_authorization_header

        if base_auth is None or not isinstance(base_auth, str):
            return None

        try:
            return base64.b64decode(base_auth).decode('utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and password from the Base64 decoded value.
        """
        decode_base_auth = decoded_base64_authorization_header

        if decode_base_auth is None or not isinstance(decode_base_auth, str):
            return None

        if ':' not in decode_base_auth:
            return None

        data = decode_base_auth.split(':', 1)

        return data[0], data[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            db_user = User.search({'email': user_email})
        except Exception as e:
            return None

        for user in db_user:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request.
        API is fully protected by a Basic Authentication.
        """
        authHeader = self.authorization_header(request)

        if not authHeader:
            return None

        encoded = self.extract_base64_authorization_header(authHeader)
        
        if not encoded:
            return None

        decoded = self.decode_base64_authorization_header(encoded)
        
        if not decoded:
            return None

        email, pwd = self.extract_user_credentials(decoded)
        
        if not email or not pwd:
            return None

        user = self.user_object_from_credentials(email, pwd)

        return user
