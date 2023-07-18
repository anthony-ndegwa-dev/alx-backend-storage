#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB:

    Database: logs
    Collection: nginx
    Display (same as the example):
        first line: x logs where x is number of documents in this collection
        second line: Methods:
        5 lines with the number of documents with the
        method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
        one line with the number of documents with:
            method=GET
            path=/status

You can use this dump as data sample: dump.zip

The output of your script must be exactly the same as the example
"""
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """ Nginx request logs"""
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def run():
    """Provide some stats about Nginx logs stored in MongoDB."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
