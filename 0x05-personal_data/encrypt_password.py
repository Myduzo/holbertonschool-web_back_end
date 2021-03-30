#!/usr/bin/env python3
"""5. Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Implement a hash_password function that expects
    one string argument name password and returns a salted,
    hashed password, which is a byte string."""
    passwd = password.encode()
    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(passwd, salt)
    return hashed

def is_valid(hashed_password: bytes, password:str) -> bool:
    pwd = password.encode()
    if bcrypt.checkpw(pwd, hashed_password):
        return True
    return False
