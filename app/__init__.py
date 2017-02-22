from flask import Flask, g, Response
import os
import ConfigParser
from logging.handlers import RotatingFileHandler
from flask.ext.pymongo import PyMongo
from app.utils.mongo.mongo_utils import MongoUtils
from apscheduler.schedulers.background import BackgroundScheduler
from app.utils.scheduler.schedule import ImporterScheduler
import logging

scheduler = BackgroundScheduler()

# schedule = ImporterScheduler(scheduler)

# Create MongoDB database object.
mongo = PyMongo()

utils = MongoUtils(mongo)

def create_app():
    # Here we  create flask instance
    app = Flask(__name__)

    # Load application configurations
    load_config(app)

    # Configure logging.
    configure_logging(app)

    # Init modules
    init_modules(app)

    # Initialize the app to work with MongoDB
    mongo.init_app(app, config_prefix='MONGO')

    # Init scheduler
    # schedule.start()
    # logging.basicConfig()

    return app


def load_config(app):
    ''' Reads the config file and loads configuration properties into the Flask app.
    :param app: The Flask app object.
    '''
    # Get the path to the application directory, that's where the config file resides.
    par_dir = os.path.join(__file__, os.pardir)
    par_dir_abs_path = os.path.abspath(par_dir)
    app_dir = os.path.dirname(par_dir_abs_path)

    # Read config file
    config = ConfigParser.RawConfigParser()
    config_filepath = app_dir + '/config.cfg'
    config.read(config_filepath)

    app.config['SERVER_PORT'] = config.get('Application', 'SERVER_PORT')
    app.config['HOST'] = config.get('Application', 'HOST')
    app.config['MONGO_DBNAME'] = config.get('Mongo', 'DB_NAME')
    app.config['MONGO_HOST'] = config.get('Application', 'HOST')
    app.config['SECRET_KEY'] = config.get('Application', 'SECURITY_KEY')

    # Logging path might be relative or starts from the root.
    # If it's relative then be sure to prepend the path with the application's root directory path.
    log_path = config.get('Logging', 'PATH')
    if log_path.startswith('/'):
        app.config['LOG_PATH'] = log_path
    else:
        app.config['LOG_PATH'] = app_dir + '/' + log_path

    app.config['LOG_LEVEL'] = config.get('Logging', 'LEVEL').upper()

def configure_logging(app):
    """ Configure the app's logging.
     param app: The Flask app object
    """

    log_path = app.config['LOG_PATH']
    log_level = app.config['LOG_LEVEL']

    # If path directory doesn't exist, create it.
    log_dir = os.path.dirname(log_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create and register the log file handler.
    log_handler = RotatingFileHandler(log_path, maxBytes=250000, backupCount=5)
    log_handler.setLevel(log_level)
    app.logger.addHandler(log_handler)

    # First log informs where we are logging to.
    # Bit silly but serves  as a confirmation that logging works.
    app.logger.info('Logging to: %s', log_path)


def init_modules(app):
    # Import blueprint modules
    from app.mod_main.views import mod_main
    app.register_blueprint(mod_main)

    # Register visualizer blueprint
    from app.mod_viz.views import mod_viz
    app.register_blueprint(mod_viz)

    # Register importer blueprint
    from app.mod_importer.views import mod_importer
    app.register_blueprint(mod_importer)

    # Register importer blueprint
    from app.mod_api.views import mod_api
    app.register_blueprint(mod_api)