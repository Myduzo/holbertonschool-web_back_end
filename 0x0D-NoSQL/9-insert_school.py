#!/usr/bin/env python3
""" Insert a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """ Function that inserts a new document in a collection based on kwargs
    """
    mdb = mongo_collection.insert_one(kwargs)
    return mdb.inserted_id
