#!/usr/bin/env python3
"""
Python function that changes all topics of a school document based on the name.
"""

import pymongo

def update_topics(mongo_collection, name, topics):
    """
    Changes the topics of school documents with the given name.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to set for the school.
    """
    # Define the query to match school documents by name
    query = {"name": name}

    # Use update_many to update all matching documents with the new topics
    mongo_collection.update_many(query, {"$set": {"topics": topics}})
