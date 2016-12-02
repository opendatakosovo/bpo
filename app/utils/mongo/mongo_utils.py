import datetime
from bson.objectid import ObjectId
from bson import json_util

class MongoUtils(object):
    def __init__(self, mongo):
        self.mongo = mongo
        self.mgr_collection = 'mgr'

    def get(self, field_name, field_key):
        document = self.mongo.db[self.mgr_collection] \
            .find({field_name: field_key})
        return json_util.dumps(document)

