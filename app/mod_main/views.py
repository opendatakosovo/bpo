from flask import Blueprint, render_template, url_for, request
from bson.json_util import dumps

mod_main = Blueprint('main', __name__)



@mod_main.route('/', methods=['GET'])
def index():
    ''' Renders the App index page.
    :return:
    '''

    return render_template('mod_main/index.html')


@mod_main.route('/disclaimer', methods=['GET'])
def data_disclaimer():
    ''' Renders the Data Disclaimer page.
    :return:
    '''

    return render_template('mod_main/disclaimer.html')


@mod_main.route('/about', methods=['GET'])
def about():
    ''' Renders the App index page.
    :return:
    '''

    return render_template('mod_main/about.html')
