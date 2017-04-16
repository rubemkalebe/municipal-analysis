'''
Created on 15 de abr de 2017

@author: rubemkalebe
'''
from pymongo import MongoClient

MONGO_INSTANCE = 'localhost:27017'

def connect():
    db = None
    try:
        client = MongoClient(MONGO_INSTANCE)
        db = client.municipal_analysis_2014
    except Exception as e:
        print('Connection ERROR: ' + str(e))
    return db