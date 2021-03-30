#!/usr/bin/env python3
"""5. Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Implement a hash_password function that expects
    one string argument name password and returns a salted,
    hashed password, which is a byte string."""
    passwd = b'$2b$12$'

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passwd, salt)
    return hashed
