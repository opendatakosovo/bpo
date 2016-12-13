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
@mod_api.route('/bd/victims/<string:name>/<int:level>/<string:violence_type>', methods=['GET'])
def get_results(name, level, violence_type=None):
    match_field = ""
    group_by_location = ""
    match = None
    if level == 0:
        match_field = "division"
        group_by_location = "district"
    elif level == 1:
        match_field = "district"
        group_by_location = "upazilla"
    elif level == 2:
        match_field = "upazilla"
        group_by_location = "upazilla"

    if violence_type == None:
        match = {
            "$match": {
                match_field: {
                    "$nin": [
                        ""
                    ],
                    "$in": [
                        name, 'multiple'
                    ]
                }
            }
        }
    else:
        match = {
            "$match": {
                match_field: {
                    "$nin": [
                        "",'multiple'
                    ],
                    "$in": [
                        name
                    ]
                },
                "violence_type_1": {
                    "$in": [
                        violence_type
                    ]
                }
            }
        }
    group = {
        "$group": {
            "_id": {
                group_by_location: '$' + group_by_location
            },
            "incidents": {
                "$sum": 1
            },
            'total_injury_a': {
                '$sum': '$total_number_of_wounded_reported_actor_a'
            },
            'total_injury_b': {
                '$sum': '$total_number_of_wounded_reported_actor_b'
            },
            'total_injury_b': {
                '$sum': '$total_number_of_wounded_reported_actor_b'
            },
            'total_property_a': {
                '$sum': '$number_of_property_destroyed_1'
            },
            'total_property_b': {
                '$sum': '$number_of_property_destroyed_3'
            },
            'total_property_c': {
                '$sum': '$number_of_property_destroyed_1_1'
            },
            'total_death_a': {
                '$sum': '$total_number_of_casualties_reported_actor_a'
            },
            'total_death_b': {
                '$sum': '$total_number_of_casualties_reported_actor_b'
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
            'name': "$_id." + group_by_location,
            "incidents": "$incidents",
            'injuries': {'$add': ['$total_injury_b', '$total_injury_b']},
            'property': {'$add': ['$total_property_a', '$total_property_b', '$total_property_c']},
            'death': {'$add': ['$total_death_a', '$total_death_a']}
        }
    }
    aggregation = [match, group, sort, project]
    result = mongo.db.mgr.aggregate(aggregation)
    resp = Response(
        response=json_util.dumps(result['result']),
        mimetype='application/json')
    return resp


@mod_api.route('/incidents/monthly/<string:name>/<int:level>')
@mod_api.route('/incidents/monthly/<string:name>/<int:level>/<string:violence_type>')
def monthly_incidents(name, level, violence_type=None):
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
                name
            ]
        }
    match = None
    json_result = {}
    if violence_type == None:
        match = {
            "$match": {
                level_json[level]: match_location ,
                'violence_month': {
                    "$nin": [
                        ""
                    ]
                }
            }
        }
    else:
        match = {
            "$match": {
                level_json[level]: match_location,
                'violence_month': {
                    "$nin": [
                        ""
                    ]
                },
                'violence_type_1': {
                    "$in": [
                        violence_type
                    ]
                }
            }
        }

    data = mongo.db.mgr.aggregate(
        [match
            ,
         {
             '$group': {
                 '_id': {
                     'month': {
                         '$substr': ['$incident_date', 5, 2]
                     }
                 },
                 'total_injury_a': {
                     '$sum': '$total_number_of_wounded_reported_actor_a'
                 },
                 'total_injury_b': {
                     '$sum': '$total_number_of_wounded_reported_actor_b'
                 },
                 'total_injury_b': {
                     '$sum': '$total_number_of_wounded_reported_actor_b'
                 },
                 'total_property_a': {
                     '$sum': '$number_of_property_destroyed_1'
                 },
                 'total_property_b': {
                     '$sum': '$number_of_property_destroyed_3'
                 },
                 'total_property_c': {
                     '$sum': '$number_of_property_destroyed_1_1'
                 },
                 'total_death_a': {
                     '$sum': '$total_number_of_casualties_reported_actor_a'
                 },
                 'total_death_b': {
                     '$sum': '$total_number_of_casualties_reported_actor_b'
                 }
             }
         },
         {
             "$sort": {
                 "_id.month": 1
             }
         },
         {
             "$project": {
                 "_id": 0,
                 'month': "$_id.month",
                 'injuries': {'$add': ['$total_injury_b', '$total_injury_b']},
                 'property': {'$add': ['$total_property_a', '$total_property_b', '$total_property_c']},
                 'death': {'$add': ['$total_death_a', '$total_death_a']}

             }
         }
         ]
    )
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
            'total_injury_a': {
                '$sum': '$total_number_of_wounded_reported_actor_a'
            },
            'total_injury_b': {
                '$sum': '$total_number_of_wounded_reported_actor_b'
            },
            'total_injury_b': {
                '$sum': '$total_number_of_wounded_reported_actor_b'
            },
            'total_property_a': {
                '$sum': '$number_of_property_destroyed_1'
            },
            'total_property_b': {
                '$sum': '$number_of_property_destroyed_3'
            },
            'total_property_c': {
                '$sum': '$number_of_property_destroyed_1_1'
            },
            'total_death_a': {
                '$sum': '$total_number_of_casualties_reported_actor_a'
            },
            'total_death_b': {
                '$sum': '$total_number_of_casualties_reported_actor_b'
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
            'injuries': {'$add': ['$total_injury_b', '$total_injury_b']},
            'property': {'$add': ['$total_property_a', '$total_property_b', '$total_property_c']},
            'death': {'$add': ['$total_death_a', '$total_death_a']}
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
        response=json_util.dumps(violence_types_array),
        mimetype='application/json')
    return resp


@mod_api.route('/top-3/<int:level>/<string:name>/<string:violence_type>', methods=['GET'])
def get_top(level, name, violence_type):
    violence_type = violence_type.replace('-','/')
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
                    "$in": [name, 'multiple']
                }

    violence_type_match = ''
    if violence_type == 'all':
        violence_type_match = [{"violence_type_1":{
            "$nin": [
                        None
                    ]
            }
        }]
    else:
        violence_type_match = [{"violence_type_1": violence_type}, {"violence_type_2": violence_type}, {"violence_type_3": violence_type}]
    casualties = mongo.db.mgr.aggregate([
        {
            "$match": {
                level_json[level]: match,
                "violence_target_group_1": {
                    "$nin": [None]
                },
                '$or': violence_type_match
            }
        },
        {
            "$group": {
                "_id": {
                    'casualties': "$violence_target_group_1"
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
            "$match": {
                level_json[level]: match,
                "destruction_of_property_1": {
                    "$nin": [None]
                },
                '$or': violence_type_match
            }
        },
        {
            "$group": {
                "_id": {
                    'property': "$destruction_of_property_1"
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

    perpetrator = mongo.db.mgr.aggregate([
        {
            "$match": {
                level_json[level]: match,
                "violence_actor_1": {
                    "$nin": [None]
                },
                '$or': violence_type_match

            }
        },
        {
            "$group": {
                "_id": {
                    'perpetrator': "$violence_actor_1"
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
