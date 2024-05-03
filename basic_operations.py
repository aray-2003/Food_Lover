import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient

#loading config from the .env file
load_dotenv()
MONGODM_URI = os.environ['MONGODB_URI']

client = MongoClient(MONGODM_URI)

#list all databases in our cluster
for db_info in client.list_database_names():
    print(db_info)
