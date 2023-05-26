# Import some necessary modules
# pip install kafka-python
# pip install pymongo
# pip install "pymongo[srv]"
from kafka import KafkaConsumer
from pymongo import MongoClient
from pymongo.server_api import ServerApi

import json

uri = 'mongodb+srv://ozielan2101:sTuVR6aL6t756bx4@cluster0.y0llox8.mongodb.net/?retryWrites=true&w=majority'

# Create a new client and connect to the server
#client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection

#try:
#    client.admin.command('ping')
#    print("Pinged your deployment. You successfully connected to MongoDB!")
#except Exception as e:
#    print(e)

# Connect to MongoDB and pizza_data database

try:
    client = MongoClient(uri)
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    db = client.comics
    print("MongoDB Connected successfully!")
except:
    print("Could not connect to MongoDB")

consumer = KafkaConsumer('test',bootstrap_servers=['my-kafka-0.my-kafka-headless.d3mon5oul06.svc.cluster.local:9092'])
# Parse received data from Kafka
for msg in consumer:
    record = json.loads(msg.value)
    print(record)
    name = record['name']

    # Create dictionary and ingest data into MongoDB
    try:
       comics_id = {'name':name }
       print (Centenito)
       comics_id = db.Centenito.insert_one(comics)
       print("Data inserted with record ids", comics_id)
    except:
       print("Could not insert into MongoDB")
