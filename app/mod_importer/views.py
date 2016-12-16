from flask import Blueprint, render_template, url_for, Response
from urllib2 import urlopen
import json

mod_importer = Blueprint('importer', __name__, url_prefix='/importer')


@mod_importer.route('/', methods=['GET'])
def index():
    ''' Renders the IMPORTER index page.
    :return:
    '''

    url = "http://0.0.0.0:5005" + url_for('static', filename='data/mgr-2014.json')
    response = urlopen(url)
    json_obj = json.load(response)

    print response

    return render_template('mod_importer/index.html')

@mod_importer.route('/update_idams', methods=['GET'])
def update_idams():
    import urllib, json
    url = "http://assemblio.com/saiis/api/incident/AVg5Mvj4-aobE9urD8hx"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    json = {
        "_id" : "584f416c9d1fa2fa4a4181a6",
        "violence_non_participants" : "",
        "total_number_of_arrested_reported_target" : None,
        "violent_event_tag_trigger" : None,
        "violence_target_group_3" : None,
        "total_number_of_casualties_reported_target" : " ",
        "total_number_of_wounded_reported_actor_b" : 10,
        "total_number_of_wounded_reported_actor_a" : 0,
        "report_date" : "5-Jul-15",
        "trigger_of_violence_1" : "Internal feud (non-specified)",
        "trigger_of_violence_2" : None,
        "total_number_of_wounded_reported_target" : None,
        "violence_target_group_2" : None,
        "violence_source" : "Prothom Alu",
        "violence_reference" : 15070522,
        "total_number_of_arrested_reported_actor_a" : None,
        "district" : "Narsingdi",
        "destruction_of_property_1" : "Other*",
        "destruction_of_property_2" : None,
        "destruction_of_property_3" : None,
        "violence_day" : 3,
        "casualties_non_participant" : None,
        "violent_event_hartal" : 0,
        "arrested_averaged" : None,
        "state" : "Bangladesh",
        "violence_actor_b_1" : 221,
        "violence_report_multiple_events" : 0,
        "violence_actor_b_3" : None,
        "violence_actor_b_2" : None,
        "violence_type_1" : "Armed battle/clashes",
        "violence_type_2" : None,
        "violence_type_3" : None,
        "number_of_property_destroyed_1" : 1,
        "number_of_property_destroyed_3" : 0,
        "division" : "Dhaka",
        "violence_month" : 7,
        "violence_year" : 2015,
        "upazilla" : "Palash",
        "conflicting_trigger_of_violence" : "No",
        "violence_actor_1" : "Local Leader (Unspecified)",
        "violence_actor_2" : None,
        "violence_actor_3" : None,
        "total_number_of_arrested_reported_actor_b" : None,
        "violence_number" : 2,
        "casualties_averaged" : None,
        "total_number_of_casualties_reported_actor_b" : 0,
        "wounded_averaged" : 0,
        "arrested_non_participant" : None,
        "violent_event_continuation" : 0,
        "violent_event_tag_multiple" : None,
        "violence_target_group_1" : None,
        "violence_police_role" : "Police arrives after the violent event",
        "incident_date" : None ,
        "woundednon_participant" : "",
        "violent_event_tag_continuation" : None,
        "violent_event_time_precision" : 1,
        "total_number_of_casualties_reported_actor_a" : None
    }

    for item in data:
        json['division'] =  item['_source']['location_and_source']['division']
        json['district'] = item['_source']['location_and_source']['district']
        json['upazila'] = item['_source']['location_and_source']['upazila']
        json['incident_date'] = item['_source']['summary']['date']
        json['violence_type'] = item['_source']['summary']['incident_type']
        json['consequence'] = {}
        json['consequence']['instigator'] = item['_source']['victims_and_perpetrators'][0]['perpetrators']['who'][0]
        json['consequence']['responder'] = item['_source']['victims_and_perpetrators'][0]['victims']['who'][0]
        json['consequence']['type'] = item['_source']['victims_and_perpetrators'][0]['consequence']

    print json
    return render_template('mod_importer/idams_data.html', data=data)
