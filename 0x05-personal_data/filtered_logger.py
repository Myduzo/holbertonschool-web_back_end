#!/usr/bin/env python3
"""Personal data PII and non PII
"""
from typing import List
import re
import logging
import os
import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor method"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Log formatter"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record),
                            self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Regex-ing"""
    for field in fields:
        message = re.sub(f'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """Create logger"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)

    logger.propagate = False
    formatter = RedactingFormatter(PII_FIELDS)

    file_handler = logging.StreamHandler()
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to secure database"""
    cnn = mysql.connector.connection.MySQLConnection(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME'))
    return cnn


def main():
    """The function will obtain a database connection using
    get_db and retrieve all rows in the users table and
    display each row under a filtered format"""

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    result = cursor.fetchall()

    logger = get_logger()

    for x in result:
        data = "name={}; email={}; phone={}; ".format(x[0], x[1], x[2])
        data += "ssn={}; password={}; ip={}; ".format(x[3], x[4], x[5])
        data += "last_login={}; user_agent={};".format(x[6], x[7])
        logger.info(data)
        
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()

