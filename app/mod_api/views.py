from bson import json_util
from flask import Blueprint, render_template
from flask import Response

from app import mongo

mod_api = Blueprint('api', __name__, url_prefix='/api')


@mod_api.route('/', methods=['GET'])
def index():
    ''' Renders the App index page.
    :return:
    '''

    return render_template('mod_importer/index.html')

@mod_api.route('/bd/victims/<string:name>/<int:level>', methods=['GET'])
def get_results(name, level):
    level_json = {
        0: "division",
        1: "district",
        2: "upazilla"
    }

    match = {
        "$match": {
            level_json[level]: {
                "$nin": [
                    ""
                ],
                "$in": [
                    name
                ]
            }
        }
    }
    group = {
        "$group": {
            "_id": {
                level_json[level+1]: '$' + level_json[level+1]
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
            level_json[level + 1]: "$_id." + level_json[level+1],
            "incidents": "$incidents"
        }
    }
    aggregation = [match, group, sort, project]
    result = mongo.db.mgr.aggregate(aggregation)
    resp = Response(
        response=json_util.dumps(result['result']),
        mimetype='application/json')
    return resp

@mod_api.route('/bd/victims/<string:type>', methods=['GET'])
@mod_api.route('/bd/victims/<string:type>/<string:name>', methods=['GET'])
def get_victims(type, name=None):
    match = None
    group = None
    if name:
        match = {
            "$match": {
                type: {
                    "$nin": [
                        ""
                    ],
                    "$in": [
                        name
                    ]
                }
            }
        }
    else:
        match = {
            "$match": {
                type: {
                    "$nin": [
                        ""
                    ]
                }
            }
        }
    if name =='division':
        group = {
            "$group": {
                "_id": {
                    'district': '$' + 'district'
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
                    type: '$'+type
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

@mod_api.route('/bd/rank/<string:type>', methods=['GET'])
def get_rank(type):

    match = {
        "$match": {
            type: {
                "$nin": [
                    None
                ]
            }
        }
    }
    group = {
        "$group": {
            "_id": {
                type: "$"+type
            },
            "victims": {
                "$sum": 1
            }
        }
    }

    sort = {
        "$sort": {
            "victims": -1
        }
    }

    project = {
        "$project": {
            "_id": 0,
            type: "$_id."+type,
            "victims": "$victims"
        }
    }
    aggregation = [match, group, sort, project]
    result = mongo.db.mgr.aggregate(aggregation)['result']

    index = 1
    for item in result:
        item['rank'] = index
        index = index + 1
    rendered_result = json_util.dumps(result)
    resp = Response(
        response=rendered_result,
        mimetype='application/json')
    return resp

@mod_api.route('/rank/division', methods=['GET'])
@mod_api.route('/rank/division/<string:name>', methods=['GET'])
def get_division_rank(name=None):
    match = {
        "$match": {
            "District": {
                "$nin": [
                    None
                ]
            }
        }
    }
    group = {
        "$group": {
            "_id": {
                "District": "$District"
            },
            "victims": {
                "$sum": 1
            }
        }
    }

    sort = {
        "$sort": {
            "victims": -1
        }
    }

    project = {
        "$project": {
            "_id": 0,
            "district": "$_id.District",
            "victims": "$victims"
        }
    }
    aggregation = [match, group, sort, project]
    result = mongo.db.mgr.aggregate(aggregation)['result']

    index = 1
    for item in result:
        item['rank'] = index
        index = index + 1
    rendered_result = json_util.dumps(result)
    resp = Response(
        response=rendered_result,
        mimetype='application/json')
    return resp

@mod_api.route('/<string:dataset>/get/violence-types', methods=['GET', 'POST'])
def get_violence_types(dataset):
    violence_types = mongo.db.mgr.distinct('violence_type_1')
    violence_types1 = mongo.db.mgr.distinct('violence_type_2')
    violence_types2 = mongo.db.mgr.distinct('violence_type_3')
    violence_types_array = set(map(str, violence_types) + map(str, violence_types1) + map(str, violence_types2))
    resp = Response(
        response= json_util.dumps(violence_types_array),
        mimetype='application/json')
    return resp
