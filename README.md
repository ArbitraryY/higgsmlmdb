# README #

The Higgs Machine Learning Challenge is put on by CERN to help improve the discovery methods of the Higgs Boson. 

From the challenge website: http://higgsml.lal.in2p3.fr/...

This script takes the HiggsML test, training, and random_submission datasets (CSV files) from the HiggsML challenge and imports them into MongoDB instances
* Version - 0.1
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
    * MongoDB - http://docs.mongodb.org/manual/installation/
    * pymongo - http://api.mongodb.org/python/current/installation.html
    * HiggsML Data sets - https://www.kaggle.com/c/higgs-boson/data
* Database configuration
    * to start mongodb (using the default configuration and install guidelines from the MongoDB install guide above) run 
        * <path to mongo>/bin/mongod --conf=<path to mongod.conf>
* Deployment instructions
    * Start up mongo as shown above
    * Copy the script hml_to_mdb.py to a directory on your hard drive.  Place the dataset files, test.csv, training.csv, and random_submission.csv into this same directory.  
    * Run python hml_to_mdb.py <test | training | random_submission>.  This creates a test, training, or random_submission database called higgsml_test (training, random_submission).  Each row in the .csv file is put into an "events" collection and each row in the .csv file becomes a document in the events collection with "_id" being replaced by "EventId".

### Contribution guidelines ###

* Do what you wish...

### Who do I talk to? ###

* syntax@arbitraryy.com