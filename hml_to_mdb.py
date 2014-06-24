'''
This program reads the HiggsML data set from a CSV file and populates
it into its respective MongoDB (higgsml_training | higgsml_test)

start MongoDB daemon:

mongod --config=/Applications/mongodb-2.6.1/mongod.conf
 
@author: ArbitraryY(+)
'''
 
from pymongo import MongoClient
import csv
 
#Which dataset do we want to consider?
dbuse = "training"
client = MongoClient('localhost', 27017)
 
if dbuse == "training":
    db = client.higgsml_training
    csv_file = "training.csv"
elif dbuse == "test":
    db = client.higgsml_test
    csv_file = "test.csv"
 
#create the collection
events = db.events
 
f = open(csv_file,"r")
try:
    reader = csv.DictReader(f)
    for row in reader:
        #initialize new event dict
        event = {}
        for key in row:
            if key == 'EventId':
                event["_id"] = row[key]
            else:
                event[key] = row[key]
        print(event)
        print ("inserting: " + row["EventId"])
        event_id = events.insert(event)
        #time.sleep(2)
       
finally:
    f.close()