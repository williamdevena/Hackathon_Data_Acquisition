"""
This module contains the functions to read data from a MongoDB database
"""

import sys

sys.path.append("./src/")

from storing import *
from costants import *


def read_collection(cluster_name, database_name, collection_name, condition={}):
    """
    Reads from a MongoDB database a certain collection and if given querys with certain conditions.

    Args:
        - cluster_name (str): Name of the MongoDB cluster
        - database_name (str): Name of the MongoDB database
        - collection_name (str): Name of the MongoDB collection
        - condition (dict): Dictionary containing the conditions of the query.
        (EX: condition = {'name' : 'William'} gets all the documents of the collection that have 'name'='William')

    Returns:
        - A MongoDB collection object
    """
    client = connect_cluster_mongodb(cluster_name, MONGODB_USERNAME, MONGODB_PASSWORD)
    database = connect_database(client, database_name)
    collection = connect_collection(database, collection_name)

    return collection.find(condition)


def main():
    condition = {"commit.message": {"$regex": "macOS"}}
    result = read_collection(
        CLUSTER_NAME, DATABASE_NAME, COLLECTION_NAME_JAX, condition
    )
    result = list(result)
    print(result)
    print(result[0]["commit"]["message"])
    print(len(result))


if __name__ == "__main__":
    main()
