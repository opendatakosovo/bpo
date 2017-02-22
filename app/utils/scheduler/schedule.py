from datetime import datetime
import urllib
import subprocess
import os.path
# from utils.importer.import_idams import parse

class ImporterScheduler(object):
    def __init__(self, scheduler):
        self.scheduler = scheduler

    def start(self):
        try:
            # This is here to simulate application activity (which keeps the main thread alive).
            self.scheduler.daemonic = True  # non daemon thread
            self.scheduler.add_job(self.some_job, 'interval', seconds=30)
            self.scheduler.start()
        except:
            # Not strictly necessary if daemonic mode is enabled but should be done if possible
            self.scheduler.shutdown()

    def some_job(self):
        print "File downloaded & importer started..."
        # path = os.getcwd().split('/')
        # path_to_output_file = '/'.join(path) + '/utils/importer/idams/incidents.json'
        # urllib.urlretrieve("http://0.0.0.0:5050/api/get-latest-incidents/2016-11-01", path_to_output_file)
        # parse()
        print "Got my job done..."
