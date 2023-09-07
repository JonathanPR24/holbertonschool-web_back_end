#!/usr/bin/env python3
"""
Python function that returns the list of schools having a specific topic.
"""

import pymongo

def schools_by_topic(mongo_collection, topic: str) -> list:
    """
    Retrieve a list of schools from a MongoDB collection that match a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of schools that have the specified topic.
    """

    sch: list = []
    query = {"topics": topic}

    for school in mongo_collection.find(query):
        sch.append(school)

    return sch
