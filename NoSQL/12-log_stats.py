#!/usr/bin/env python3
"""
This script defines a function for retrieving schools by a specific topic from a MongoDB collection.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Retrieve schools from a MongoDB collection that match a specific topic.

    Returns:
        pymongo.cursor.Cursor: A cursor containing the results of the search query.
    """
    # Use the find method to query the collection for documents with the specified topic.
    return mongo_collection.find({"topics": topic})
