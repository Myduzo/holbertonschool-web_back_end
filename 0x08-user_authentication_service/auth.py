#!/usr/bin/env python3
""" Authentication file
"""

from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from flask import request
from uuid import uuid4


def _hash_password(password: str) -> str:
    """ Instance method that takes in a password string
    arguments and returns a salted hash of the input password,
    hashed with bcrypt.hashpw.
    """
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Assigning variables
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Instance method that saves the user to the database
        using self._db and return the User object.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashedPW = _hash_password(password)
            return self._db.add_user(email, hashedPW)

        else:
            raise ValueError("User {} already exists.".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """ Instance method that returns True if the pwd matches,
        in any other case False.
        """
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ Instance method that returns the session_id
        as a string.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Instance method that takes a single session_id
        string argument and returns the corresponding User or None.
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ The method takes a single user_id
        integer argument and returns None.
        """
        self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """ The method generates a UUID and updates the user’s
        reset_token database field. Returns the token.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        
        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """ Updates the password and the reset_token to None
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError

        hashed_password = _hash_password(password)
        self._db.update_user(user.id,
                             hashed_password=hashed_password,
                             reset_token=None)


def _generate_uuid() -> str:
    """ Private method that returns
    a string representation of a new UUID.
    """
    return str(uuid4())
