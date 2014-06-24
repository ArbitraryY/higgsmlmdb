'''
This program reads the HiggsML data set from a CSV file and populates
it into its respective MongoDB (higgsml_training | higgsml_test)

start MongoDB 
mongod --config=/Applications/mongodb-2.6.1/mongod.conf
 
@author: ArbitraryY(+)
'''

from pymongo import MongoClient
import csv
import sys

def usage():
    print "\n    hml_to_mdb.py <test | training | random_submission>\n"
    sys.exit()

if len(sys.argv) != 2:
    print usage()
 
#Get the database name from the command line?
dbuse = str(sys.argv[1])
csv_file = dbuse + ".csv"
#Create a mongo client to connect to the MongoDB
client = MongoClient('localhost', 27017)

if dbuse == "training":
    db = client.higgsml_training
elif dbuse == "test":
    db = client.higgsml_test
elif dbuse == "random_submission":
    db = client.higgsml_random_submission
    
#create the collection
events = db.events

#Open the csv data sets for reading
f = open(csv_file,"r")
try:
    #Creates a dictionary obj from the csv file
    reader = csv.DictReader(f)
    #Create a dictionary from each row in the CSV file
    for row in reader:
        #initialize new event dict
        event = {}
        #For each row in the CSV file, insert the heading and value 
        #into the dictionary as a key/value pair
        for key in row:
            if key == 'EventId':
                event["_id"] = row[key]
            else:
                event[key] = row[key]
        print ("\n======= Inserting: " + row["EventId"] + "===========")
        print(event)
        #Insert the dictionary as a document into the collection
        event_id = events.insert(event)
       
finally:
    f.close()