from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
url="mongodb+srv://pratik21:12345@cluster0.avl5l.mongodb.net/?retryWrites=true&w=majority"

#create a new client and connectt to server
client = MongoClient(url)

#create database name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME='waferfault'

df=pd.read_csv("C:\Users\Pratik\Data-Science\Sensor Fault Detection Project\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)