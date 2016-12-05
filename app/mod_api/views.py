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


@mod_api.route('/bd/victims', methods=['GET'])
def get_victims():
    match = {
        "$match": {
            "EventLocationDistrict": {
                "$nin": [
                    None
                ]
            }
        }
    }
    group = {
        "$group": {
            "_id": {
                "District": "$EventLocationDistrict"
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
    result = mongo.db.mgr.aggregate(aggregation)
    resp = Response(
        response=json_util.dumps(result['result']),
        mimetype='application/json')
    return resp

@mod_api.route('/<string:dataset>/get/violence-types', methods=['GET', 'POST'])
def get_violence_types(dataset):
    violence_types = mongo.db.mgr.distinct('ViolenceType1')
    violence_types1 = mongo.db.mgr.distinct('ViolenceType2')
    violence_types2 = mongo.db.mgr.distinct('ViolenceType3')
    violence_types_array = set(map(str, violence_types) + map(str, violence_types1) + map(str, violence_types2))
    resp = Response(
        response= json_util.dumps(violence_types_array),
        mimetype='application/json')
    return resp
