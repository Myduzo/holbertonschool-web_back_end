#!/usr/bin/env python3
""" List all documents in Python
"""


def list_all(mongo_collection):
    """ Function that lists all documents in a collection
    """
    mdb = mongo_collection.find()
    return mdb if mdb else []
