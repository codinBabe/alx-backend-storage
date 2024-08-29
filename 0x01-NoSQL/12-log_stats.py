#!/usr/bin/env python3
"""Log stats in Python"""


import pymongo
from pymongo import MongoClient


def log_nginx_stats(mongo_collection):
    """Provides statistics about Nginx logs."""
    print(f"{mongo_collection.estimated_document_count()} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tMethod {method}: {count}")

    number_of_gets = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"Status checks: {number_of_gets}")


if __name__ == "__main__":
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_nginx_stats(mongo_collection)
