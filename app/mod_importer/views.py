from flask import Blueprint, render_template

mod_importer = Blueprint('importer', __name__, url_prefix='/api')


@mod_importer.route('/', methods=['GET'])
def index():
    ''' Renders the IMPORTER index page.
    :return:
    '''

    return render_template('mod_importer/index.html')
