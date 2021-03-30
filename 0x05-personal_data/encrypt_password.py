#!/usr/bin/env python3
"""5. Encrypting passwords
"""
import bcrypt


def hash_password(password):
    passwd = b'$2b$12$'

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passwd, salt)
    return hashed
