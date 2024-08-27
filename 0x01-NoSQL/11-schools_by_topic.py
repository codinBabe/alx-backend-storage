#!/usr/bin/env python3
"""Schools by topic"""


from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """Schools by topic"""
    return mongo_collection.find({"topics": topic})
