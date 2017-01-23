# -*- coding: UTF-8 -*-
import csv
import os
import re
from datetime import datetime
from pymongo import MongoClient
import json

# Connect to defualt local instance of MongoClient
client = MongoClient()

# Get database and collection
db = client.bpo
collection = db.census


def parse():
    # collection.remove({})

    print "Importing Data"
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for filename in os.listdir(dir_path + '/data/'):

        if (filename.endswith(".csv")):
            with open(dir_path + '/data/' + filename, 'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                document = {}
                upazila = ""
                for row in reader:
                    if row[1] != '' and row[1] != "Upazila/Thana":
                        upazila = row[1]
                        document[upazila] = {}
                    else:
                        # print upazila
                        # print row
                        if row[2] == ' Muslim':
                            document[upazila]["Muslim"] = int(row[5])
                        elif row[2] == ' Hindu':
                            document[upazila]["Hindu"] = int(row[5])
                        elif row[2] == ' Christian':
                            document[upazila]["Christian"] = int(row[5])
                        elif row[2] == ' Buddhist':
                            document[upazila]["Buddhist"] = int(row[5])
                        elif row[2] == ' Other':
                            document[upazila]["Other"] = int(row[5])

                for upazila in document:
                    # print upazila
                    # print document[upazila]
                    # print dict(collection.find({'upazila': upazila}))
                    collection.update({'upazila': upazila},{"$set": document[upazila]})
                    # collection.insert(doc)

parse()