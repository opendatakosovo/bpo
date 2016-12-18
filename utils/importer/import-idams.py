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
collection = db.idams


def parse():
    collection.remove({})

    print "Importing Data"
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for filename in os.listdir(dir_path + '/idams/'):
        print filename
        json_obj = None
        if (filename.endswith(".json")):
            with open(dir_path + '/idams/' + filename, 'rb') as jsonfile:
                json_obj = json.load(jsonfile)

        for elem in json_obj:
            new_json = {}


            if 'actors' in elem['_source']:
                new_json['incident_date'] = datetime.strptime(elem['_source']['summary']['date'], '%Y-%m-%d')
                new_json['violence_actor'] = elem['_source']['actors']['instigators']
                new_json['violence_type'] = elem['_source']['summary']['incident_type']
                new_json['responders'] = elem['_source']['actors']['responders']
                new_json['property_destroyed_type'] = []
                new_json['injuries_count'] = 0
                new_json['deaths_count'] = 0
                new_json['property_destroyed_count'] = 0
                if 'victims_and_perpetrators' in elem['_source']:
                    if len(elem['_source']['victims_and_perpetrators']) > 0:
                        new_json['injuries_count'] = elem['_source']['victims_and_perpetrators'][0]['victims']['count']
                        new_json['deaths_count'] = elem['_source']['victims_and_perpetrators'][0]['victims']['count']
                        new_json['property_destroyed_count'] = elem['_source']['victims_and_perpetrators'][0]['victims']['count']

                new_json['division'] = elem['_source']['location_and_source']['division']
                new_json['district'] = elem['_source']['location_and_source']['district']
                new_json['upazila'] = elem['_source']['location_and_source']['upazila']

            collection.insert(new_json)
parse()