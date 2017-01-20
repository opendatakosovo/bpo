from bson import json_util
from flask import Blueprint, render_template, request
from flask import Response
from datetime import datetime

from app import mongo
from app import utils
import json
mod_api = Blueprint('api', __name__, url_prefix='/api')


@mod_api.route('/', methods=['GET'])
def index():
    ''' Renders the App index page.
    :return:
    '''

    return render_template('mod_importer/index.html')


@mod_api.route('/search', methods=['POST'])
def search():
     
    params = request.json

    # Format date
    if 'date' in params:
        params['to_date'] = datetime.strptime(params['date'].split('---')[1], '%m-%d-%Y')
        params['from_date'] = datetime.strptime(params['date'].split('---')[0], '%m-%d-%Y')

    result = {}
    result['stats'] = utils.get_stats(params)
    result['monthly-stats'] = utils.get_monthly_incidents_stats(params)
    result['quarterly-stats'] = utils.get_quarterly_incidents_stats(params)
    result['rank-stats'] = utils.get_rank_stats(params)
    result['incident-stats'] = utils.get_incidents_stats(params)
    result['violence-types'] = utils.get_violence_types(params)
    result['daily-stats'] = utils.get_incident_types_by_time(params)
    result['top-3'] = utils.get_top_3_stats(params)
    result['map-victims-count'] = utils.get_map_victims_count(params)
    resp = Response(
        response=json_util.dumps(result),
        mimetype='application/json')
    return resp




# @mod_api.route('/bd/victims/<string:type>', methods=['GET'])
@mod_api.route('/get_total_victims_number/<string:type>/<string:date>/<string:violence_type>/<string:name>', methods=['GET'])
def get_victims(type, date=None, violence_type=None, name=None):
    if violence_type:
        violence_type = violence_type.replace('-', '/')
    if date:
        from_date = datetime.strptime(date.split('---')[0], '%m-%d-%Y')
        to_date = datetime.strptime(date.split('---')[1], '%m-%d-%Y')

    match = None
    group = None
    if name != 'Bangladesh':
        match = {
            "$match": {
                type: {
                    "$nin": [
                        ""
                    ],
                    "$in": [
                        name
                    ]
                },
                'violence_type': {
                    "$in": [
                        str(violence_type)
                    ]
                },
                "incident_date": {"$gte": from_date, "$lte": to_date}
            }
        }
    else:
        match = {
            "$match": {
                type: {
                    "$nin": [
                        ""
                    ]
                },
                "incident_date": {"$gte": from_date, "$lte": to_date}
            }
        }

    if type == 'division':
        group = {
            "$group": {
                "_id": {
                    'division': '$district'
                },
                "incidents": {
                    "$sum": 1
                }
            }
        }
    else:
        group = {
            "$group": {
                "_id": {
                    type: '$' + type
                },
                "incidents": {
                    "$sum": 1
                }
            }
        }

    sort = {
        "$sort": {
            "incidents": -1
        }
    }

    project = {
        "$project": {
            "_id": 0,
            type: "$_id." + type,
            "incidents": "$incidents"
        }
    }
    aggregation = [match, group, sort, project]
    result = mongo.db.mgr.aggregate(aggregation)
    resp = Response(
        response=json_util.dumps(result['result']),
        mimetype='application/json')
    return resp


@mod_api.route('/<string:dataset>/get/violence-types', methods=['GET', 'POST'])
def get_violence_types(dataset):
    violence_types = mongo.db[dataset].distinct('violence_type')
    resp = Response(
        response=json_util.dumps(violence_types),
        mimetype='application/json')
    return resp

@mod_api.route('/census/<string:name>/<int:level>', methods=['GET', 'POST'])
def get_census_info(name, level):
    census_info = None
    if level == 0:
        census_info = mongo.db.census.find_one({"division": name})
    elif level == 1:
        census_info = mongo.db.census.find_one({"district": name})
    elif level == 2:
        census_info = mongo.db.census.find_one({"upazila": name})
    resp = Response(
        response=json_util.dumps(census_info),
        mimetype='application/json')
    return resp