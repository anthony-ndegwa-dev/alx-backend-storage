#!/usr/bin/env python3
"""Python function that inserts a new document in a collection based on kwargs:

    Prototype: def insert_school(mongo_collection, **kwargs):
    mongo_collection will be the pymongo collection object
    Returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection"""
    item = mongo_collection.insert_one(kwargs)
    return item.inserted_id
