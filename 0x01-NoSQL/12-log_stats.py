#!/usr/bin/env python3
"""Log stats in Python"""


import pymongo
from pymongo import MongoClient

# Connect to MongoDB

client = MongoClient('mongodb://localhost:27017/')
db = client['logs']
collection = db['nginx']

# Get total number of logs

total_logs = collection.count_documents({})
print(f'Total logs: {total_logs}')

# Get methods

methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

for method in methods:
    count = collection.count_documents({'method': method})
    print(f'\t{method}: {count}')

# Get GET requests for /status

get_status_count = collection.count_documents({
    'method': 'GET', 'path': '/status'})
print(f'GET requests for /status: {get_status_count}')
