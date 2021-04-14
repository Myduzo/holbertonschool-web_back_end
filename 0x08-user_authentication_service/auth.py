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
        """ Instance method that returns the sessionID
        as a string.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        sessionId = _generate_uuid()
        self._db.update_user(user.id, sessionId=sessionId)
        return sessionId


def _generate_uuid() -> str:
    """ Private method that returns
    a string representation of a new UUID.
    """
    return uuid4()
