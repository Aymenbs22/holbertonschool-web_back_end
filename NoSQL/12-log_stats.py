#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    school_collection = client.logs.nginx
    print(school_collection)
