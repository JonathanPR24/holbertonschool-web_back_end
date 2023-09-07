#!/usr/bin/env python3
"""
    Python function that changes all topics of
      a school document based on the name:
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document based on the school's name.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to set for the school.
    """
    # Find the school document by name and update its topics field
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
