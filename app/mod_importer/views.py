from flask import Blueprint, render_template, url_for
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
