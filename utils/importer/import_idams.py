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
    count = 0
    other_v_count = 0
    for filename in os.listdir(dir_path + '/idams/'):
        print filename
        json_obj = None
        if (filename.endswith(".json")):
            with open(dir_path + '/idams/' + filename, 'rb') as jsonfile:
                json_obj = json.load(jsonfile)

        for elem in json_obj:
            new_json = {}


            if 'actors' in elem['_source']:
                if len(elem['_source']['smart_tags']['smart_tags']) > 0 and \
                                elem['_source']['smart_tags']['smart_tags'][0] != '' and elem['_source']['smart_tags']['smart_tags'][0] =='Terrorism':
                    new_json['incident_date'] = datetime.strptime(elem['_source']['summary']['date'], '%Y-%m-%d')
                    new_json['violence_actor'] = elem['_source']['actors']['instigators']
                    new_json['violence_type'] = 'Terrorism and radicalism'
                    new_json['responders'] = elem['_source']['actors']['responders']
                    new_json['causes'] = elem['_source']['causes_of_incident']['causes']
                    new_json['property_destroyed_type'] = []
                    new_json['injuries_count'] = 0
                    new_json['deaths_count'] = 0
                    new_json['property_destroyed_count'] = 0
                    if 'victims_and_perpetrators' in elem['_source']:
                        if len(elem['_source']['victims_and_perpetrators']) > 0:
                            if elem['_source']['victims_and_perpetrators'][0]['consequence'] == 'Death':
                                new_json['deaths_count'] = elem['_source']['victims_and_perpetrators'][0]['victims'][
                                    'count']
                            elif elem['_source']['victims_and_perpetrators'][0]['consequence'] == 'Injury':
                                new_json['injuries_count'] = elem['_source']['victims_and_perpetrators'][0]['victims'][
                                    'count']
                            elif elem['_source']['victims_and_perpetrators'][0][
                                'consequence'] == 'Private property damaged' or \
                                            elem['_source']['victims_and_perpetrators'][0][
                                                'consequence'] == 'Public property damaged':
                                new_json['property_destroyed_count'] = \
                                elem['_source']['victims_and_perpetrators'][0]['victims']['count']

                    new_json['division'] = elem['_source']['location_and_source']['division']
                    new_json['district'] = elem['_source']['location_and_source']['district']
                    new_json['upazila'] = elem['_source']['location_and_source']['upazila']
                    count = count + 1
                elif elem['_source']['summary']['incident_type'] in ['Political dispute', 'Border incident', 'IED Attack', 'Arson attack', 'Mob Violence']:
                    new_json['incident_date'] = datetime.strptime(elem['_source']['summary']['date'], '%Y-%m-%d')
                    new_json['violence_actor'] = elem['_source']['actors']['instigators']
                    new_json['violence_type'] = elem['_source']['summary']['incident_type']
                    new_json['responders'] = elem['_source']['actors']['responders']
                    new_json['causes'] = elem['_source']['causes_of_incident']['causes']
                    new_json['property_destroyed_type'] = []
                    new_json['injuries_count'] = 0
                    new_json['deaths_count'] = 0
                    new_json['property_destroyed_count'] = 0
                    if 'victims_and_perpetrators' in elem['_source']:
                        if len(elem['_source']['victims_and_perpetrators']) > 0:
                            if elem['_source']['victims_and_perpetrators'][0]['consequence'] == 'Death':
                                new_json['deaths_count'] = elem['_source']['victims_and_perpetrators'][0]['victims'][
                                    'count']
                            elif elem['_source']['victims_and_perpetrators'][0]['consequence'] == 'Injury':
                                new_json['injuries_count'] = elem['_source']['victims_and_perpetrators'][0]['victims']['count']
                            elif elem['_source']['victims_and_perpetrators'][0]['consequence']=='Private property damaged' or elem['_source']['victims_and_perpetrators'][0]['consequence']=='Public property damaged':
                                new_json['property_destroyed_count'] = elem['_source']['victims_and_perpetrators'][0]['victims']['count']

                    new_json['division'] = elem['_source']['location_and_source']['division']
                    new_json['district'] = elem['_source']['location_and_source']['district']
                    new_json['upazila'] = elem['_source']['location_and_source']['upazila']
                    other_v_count = other_v_count + 1
                else:
                    pass
            if new_json:
                collection.insert(new_json)

    print count
    print other_v_count

parse()