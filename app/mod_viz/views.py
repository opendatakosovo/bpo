from flask import Blueprint, render_template, url_for, request
from bson.json_util import dumps

mod_viz = Blueprint('viz', __name__, url_prefix='/viz')


@mod_viz.route('/', methods=['GET'])
def index():
    ''' Renders the Vizualizer index page.
    :return:
    '''

    return render_template('mod_viz/index.html')
