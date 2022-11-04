import numpy as np
import pandas as pd
import pymongo
from pymongo import MongoClient
from auth import *
import logging

logging.basicConfig(level=logging.INFO)

# To not show username and password the variables MONGODB_USERNAME and MONGODB_PASSWORD
# are stored in a separate file that are not push remotely

def connect_cluster_mongodb(cluster_name, username, password):
    '''
    Opens connections with a MongoDB cluster
    
    Args:
        - cluster_name (str): name of the cluster 
        - username (str): username used ofr authentication
        - password (str): password used for authentication
        
    Returns:
        - client (MongoClient): client we use to comunicate with the database
    '''
    connection_string = f"mongodb+srv://{username}:{password}@{cluster_name}.bhcapcy.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_string)
    
    return client

def connect_database(client, database_name):
    '''
    Returns a specific database of a MongoDB cluster
    
    Args:
        - client (MongoClient): client object  
        - database_name (str): name of the databse we want to connect to
        
    Returns:
        - database (MongoDatabase): database object
    '''
    #If databse doen't exist in the cluster it creates automatically
    if database_name not in client.list_database_names():
        logging.info(f"The {database_name} database doesn't exist so MongoDB is going to create it automatically.")
    database = client[database_name]
    
    return database

def connect_collection(database, collection_name):
    '''
    Returns a specific collection of a MongoDB database
    
    Args:
        - database (pymongo.database.Database): database object 
        - collection_name (str): name of the collection we want to connect to
        
    Returns:
        - collection (pymongo.collection.Collection): collection object
    '''
    #If collection doen't exist in the database it creates automatically
    if collection_name not in database.list_collection_names():
        logging.info(f"The {collection_name} collection doesn't exist in the {database.name} database so MongoDB is going to create it automatically.") 
    collection = database[collection_name]
    
    return collection

def store_collection_into_db(cluster_name, database_name, collection_name, data):
    '''
    Inserts a list of MongoDB documents (dictionaries) into a specific collection of a database of a cluster.
    
    Args:
        - cluster_name (str): Name of the cluster
        - database_name (str): Name of the database
        - collection_name (str): Name of the collection
        - data (List): List of dictionaries, where every dictionary represents a row (document) in the collection
        
    Returns:
        - None
    '''
    client = connect_cluster_mongodb(cluster_name, MONGODB_USERNAME, MONGODB_PASSWORD)
    database = connect_database(client, database_name)
    collection = connect_collection(database, collection_name)
    collection.insert_many(data)
    
    
    
def main():
    students = [
        {'name':'William', 'age':149},
        {'name':'Willidsfam', 'age':194},
        {'name':'Willsdiam', 'age':129},
        {'name':'Willcdciam', 'age':169},
    ]
    cluster_name = "daps2022"
    db_name = "test_db4"
    col_name = "students" 
    store_collection_into_db(cluster_name, db_name, col_name, students)
    
if __name__=="__main__":
    main()