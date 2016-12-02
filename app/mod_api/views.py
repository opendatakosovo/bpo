from flask import Blueprint, render_template, Response, jsonify
from app import utils

mod_api = Blueprint('api', __name__, url_prefix='/api')


@mod_api.route('/', methods=['GET'])
def index():
    ''' Renders the App index page.
    :return:
    '''

    return render_template('mod_importer/index.html')

@mod_api.route('/get/<string:field>/<string:key>', methods=['GET'])
def get(field, key):
    doc = utils.get(field, key)

    resp = Response(response=doc,
        status=200, \
        mimetype="application/json")
    return(resp)