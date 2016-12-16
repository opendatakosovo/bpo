from bson import json_util
from flask import Blueprint, render_template
from flask import Response
from datetime import datetime

from app import mongo

mod_api = Blueprint('api', __name__, url_prefix='/api')


@mod_api.route('/', methods=['GET'])
def index():
    ''' Renders the App index page.
    :return:
    '''

    return render_template('mod_importer/index.html')

@mod_api.route('/results/<int:level>/<string:name>/<string:violence_type>/<string:date>', methods=['GET'])
def get_results(name, level, violence_type, date, ):
    match_field = ""
    group_by_location = ""

    violence_type = violence_type.replace('-', '/')

    from_date = datetime.strptime(date.split('---')[0], '%m-%d-%Y')
    to_date = datetime.strptime(date.split('---')[1], '%m-%d-%Y')

    level_json = {
        0: "division",
        1: "district",
        2: "upazilla",
        3: "state"
    }

    match = {
        "$match": {
            level_json[level-1]: {"$in": [str(name)]},
            "violence_type": {
                "$in": [
                    str(violence_type)
                ]
            }
        }
    }
    group = {
        "$group": {
            "_id": {
                level_json[level]: '$' + level_json[level]
            },
            "incidents": {
                "$sum": 1
            },
            'total_injury': {
                '$sum': '$injuries_count'
            },
            'total_property': {
                '$sum': '$property_destroyed_count'
            },
            'total_death': {
                '$sum': '$deaths_count'
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
            'name': "$_id." + level_json[level],
            "incidents": "$incidents",
            'injuries': "$total_injury",
            'property': "$total_property",
            'death': "$total_death"
        }
    }
    aggregation = [match, group, sort, project]
    result = mongo.db.mgr.aggregate(aggregation)
    resp = Response(
        response=json_util.dumps(result['result']),
        mimetype='application/json')
    return resp


@mod_api.route('/incidents/monthly/<string:name>/<int:level>/<string:date>/<string:violence_type>/<string:quarterly>')
def monthly_incidents(name, level, date, quarterly,violence_type=None):
    violence_type = violence_type.replace('-', '/')
    from_date = datetime.strptime(date.split('---')[0], '%m-%d-%Y')
    to_date = datetime.strptime(date.split('---')[1], '%m-%d-%Y')

    level_json = {
        0: "division",
        1: "district",
        2: "upazilla",
        3: "state"
    }
    match_location = None
    if name == 'Bangladesh':
        level_json[level] = 'state'
        match_location = {
            "$nin": [
                ""
            ],
            "$in": [
                'Bangladesh'
            ]
        }
    else:
        match_location = {
            "$nin": [
                ""
            ],
            "$in": [
                str(name)
            ]
        }
    match = None
    json_result = {}
    match = {
        "$match": {
            level_json[level]: match_location,
            'violence_month': {
                "$nin": [
                    ""
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

    data = None

    # If we are requesting monthly data
    if quarterly == 'monthly':
        group = {
                 '$group': {
                     '_id': {
                         'month': {
                             '$substr': ['$incident_date', 5, 2]
                         }
                     },
                     'total_injury': {
                         '$sum': '$injuries_count'
                     },
                     'total_property': {
                         '$sum': '$property_destroyed_count'
                     },
                     'total_death': {
                         '$sum': '$deaths_count'
                     }
                 }
             }
        sort = {
                 "$sort": {
                     "_id.month": 1
                 }
             }
        project = {
                 "$project": {
                     "_id": 0,
                     'month': "$_id.month",
                     'injuries': "$total_injury",
                     'property': "$total_property",
                     'death': "$total_death"

                 }
             }
        data = mongo.db.mgr.aggregate([match, group, sort, project])
    else:
        data = mongo.db.mgr.aggregate([
            match,
           {
              "$project":{
                 "incident_date":1,
                 'year':{
                    "$year":"$incident_date"
                 },
                 'injuries_count':1,
                 'property_destroyed_count':1,
                 'deaths_count':1,
                 "quarter":{
                    "$cond":[
                       {
                          "$lte":[
                             {
                                "$month":"$incident_date"
                             },
                             3
                          ]
                       },
                       1,
                       {
                          "$cond":[
                             {
                                "$lte":[
                                   {
                                      "$month":"$incident_date"
                                   },
                                   6
                                ]
                             },
                             2,
                             {
                                "$cond":[
                                   {
                                      "$lte":[
                                         {
                                            "$month":"$incident_date"
                                         },
                                         9
                                      ]
                                   },
                                   3,
                                   4
                                ]
                             }
                          ]
                       }
                    ]
                 }
              }
           },
           {
              "$group":{
                 "_id":{
                    "quarter":"$quarter",
                    "year":"$year"
                 },
                 "incidents":{
                    "$sum":1
                 },
                 'total_injury':{
                    '$sum':'$injuries_count'
                 },
                 'total_property':{
                    '$sum':'$property_destroyed_count'
                 },
                 'total_death':{
                    '$sum':'$deaths_count'
                 }
              }
           },
           {
              "$project":{
                 "_id":0,
                 "quarter":"$_id.quarter",
                 "year":"$_id.year",
                 "incidents":"$incidents",
                 'injuries':"$total_injury",
                 'property':"$total_property",
                 'death':"$total_death"
              }
           },
            {
                "$sort": {
                    "year": 1
                }
            }

        ])
    json_result['incidents'] = data['result']
    resp = Response(
        response=json_util.dumps(json_result),
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
    if name == 'division':
        group = {
            "$group": {
                "_id": {
                    'district': '$district'
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
                type: "$" + type
            },
            "victims": {
                "$sum": 1
            },
            'total_injury': {
                '$sum': '$injuries_count'
            },
            'total_property': {
                '$sum': '$property_destroyed_count'
            },
            'total_death': {
                '$sum': '$deaths_count'
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
            'name': "$_id." + type,
            "victims": "$victims",
            'injuries': "$total_injury",
            'property': "$total_property",
            'death': "$total_death"
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
    violence_types = mongo.db.mgr.distinct('violence_type')
    resp = Response(
        response=json_util.dumps(violence_types),
        mimetype='application/json')
    return resp


@mod_api.route('/top-3/<int:level>/<string:name>/<string:violence_type>/<string:date>', methods=['GET'])
def get_top(level, name, violence_type, date):
    violence_type = violence_type.replace('-', '/')
    from_date = date.split('---')[0]
    from_date_object = datetime.strptime(from_date, '%m-%d-%Y')
    to_date = date.split('---')[1]
    to_date_object = datetime.strptime(to_date, '%m-%d-%Y')
    level_json = {
        0: "division",
        1: "district",
        2: "upazilla",
        3: "state"
    }
    match = {}
    if name == 'Bangladesh':
        level_json[level] = 'state'
        match = {
            "$in": [
                'Bangladesh'
            ]
        }
    else:
        match = {
            "$nin": [
                None
            ],
            "$in": [name]
        }

    casualties = mongo.db.mgr.aggregate([
        {
            "$unwind": "$responders"
        },
        {
            "$match": {
                level_json[level]: match,
                "responders": {
                    "$nin": [None]
                },
                'violence_type': {
                    "$in": [violence_type]
                },
                "incident_date": {"$gte": from_date_object, "$lte": to_date_object}
            }
        },
        {
            "$group": {
                "_id": {
                    'casualties': "$responders"
                },
                "casualties_count": {
                    "$sum": 1
                }

            }
        },
        {
            "$sort": {
                "casualties_count": -1,
            }
        },
        {
            "$project": {
                "_id": 0,
                "casualty": "$_id.casualties",
                "count": "$casualties_count"

            }
        },
        {
            "$limit": 3
        }]
    )['result']

    property = mongo.db.mgr.aggregate([
        {
            "$unwind": "$property_destroyed_type"
        },
        {
            "$match": {
                level_json[level]: match,
                "property_destroyed_type": {
                    "$nin": [None]
                },
                'violence_type': {
                    "$in": [violence_type]
                },
                "incident_date": {"$gte": from_date_object, "$lte": to_date_object}
            }
        },
        {
            "$group": {
                "_id": {
                    'property': "$property_destroyed_type"
                },
                "property_count": {
                    "$sum": 1
                }

            }
        },
        {
            "$sort": {
                "property_count": -1,
            }
        },
        {
            "$project": {
                "_id": 0,
                "property": "$_id.property",
                "count": "$property_count"

            }
        },
        {
            "$limit": 3
        }]
    )['result']

    perpetrator = mongo.db.mgr.aggregate([ \
        {
            "$unwind": "$violence_actor"
        },
        {
            "$match": {
                level_json[level]: match,
                "violence_actor": {
                    "$nin": [None]
                },
                'violence_type': {
                    "$in": [violence_type]
                },
                "incident_date": {"$gte": from_date_object, "$lte": to_date_object}
            }
        },
        {
            "$group": {
                "_id": {
                    'perpetrator': "$violence_actor"
                },
                "perpetrator_count": {
                    "$sum": 1
                }

            }
        },
        {
            "$sort": {
                "perpetrator_count": -1,
            }
        },
        {
            "$project": {
                "_id": 0,
                "perpetrator": "$_id.perpetrator",
                "count": "$perpetrator_count"

            }
        },
        {
            "$limit": 3
        }]
    )['result']
    result = {
        "casualties": casualties,
        "property": property,
        "perpetrator": perpetrator
    }
    resp = Response(
        response=json_util.dumps(result),
        mimetype='application/json')
    return resp
