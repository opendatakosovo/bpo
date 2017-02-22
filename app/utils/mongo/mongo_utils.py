import datetime
from bson.objectid import ObjectId
from bson import json_util
from datetime import datetime


class MongoUtils(object):
    def __init__(self, mongo):
        self.mongo = mongo

    def get_raw_incidents(self, params):
        match = self.build_match(params)
        group = {
            '$group': {
                '_id': {
                    'date': '$date',
                    'division': '$division',
                    'upazila': '$upazila',
                    'district': '$district'
                },
                'total_injury': {
                    '$sum': '$injuries_count'
                },
                'total_property': {
                    '$sum': '$property_destroyed_count'
                },
                'total_death': {
                    '$sum': '$deaths_count'
                },
                'incidents': {
                    '$sum': 1
                }
            }
        }
        project = {
            '$project': {
                '_id': 0,
                'date': '$_id.date',
                'division': '$_id.division',
                'district': '$_id.district',
                'upazila': '$_id.upazila',
                'death': '$total_death',
                'incidents': '$incidents',
                'property': '$total_property',
                'injuries': '$total_injury'
            }
        }
        sort = {
            '$sort': {
                'date': 1
            }
        }
        data = self.mongo.db[params['dataset']].aggregate([match, group, project, sort])
        rendered_result = data['result']
        return rendered_result
    def get_stats(self, params):
        field_match = ''
        value_match = ''
        result = {}

        if params['division'] != '' and params['district'] != '' and params['upazila'] != '':
            return self.get_upazila_stats(params)
        elif params['division'] != '' and params['district'] != '' and params['upazila'] == '':
            return self.get_district_stats(params)
        elif params['division'] != '' and params['district'] == '' and params['upazila'] == '':
            return self.get_division_stats(params)
        return result

    def get_district_stats(self, params):
        field_match = 'district'
        value_match = params['district']
        match_by_property = {
            "$match": {
                field_match: {
                    "$nin": [
                        None
                    ]
                },
                'property_destroyed_count': {
                    "$ne": [0]
                },
                'violence_type': {
                    "$in": [
                        str(params['violence_type'])
                    ]
                },
                "incident_date": {"$gte": params['from_date'], "$lte": params['to_date']},
            }
        }
        match_by_death = {
            "$match": {
                field_match: {
                    "$nin": [
                        None
                    ]
                },
                'deaths_count': {
                    "$ne": [0]
                },
                'violence_type': {
                    "$in": [
                        str(params['violence_type'])
                    ]
                },
                "incident_date": {"$gte": params['from_date'], "$lte": params['to_date']},
            }
        }

        match_by_injuries = {
            "$match": {
                field_match: {
                    "$nin": [
                        None
                    ]
                },
                'injuries_count': {
                    "$ne": [0]
                },
                'violence_type': {
                    "$in": [
                        str(params['violence_type'])
                    ]
                },
                "incident_date": {"$gte": params['from_date'], "$lte": params['to_date']},

            }
        }
        group_by_death = {
            "$group": {
                "_id": {
                    field_match: "$" + field_match
                },
                'total': {
                    '$sum': '$deaths_count'
                },
                'incidents':{
                    '$sum': 1
                }
            }
        }
        group_by_property = {
            "$group": {
                "_id": {
                    field_match: "$" + field_match
                },
                'total': {
                    '$sum': '$property_destroyed_count'
                },
                'incidents':{
                    '$sum': 1
                }
            }
        }
        group_by_injuries = {
            "$group": {
                "_id": {
                    field_match: "$" + field_match
                },
                'total': {
                    '$sum': '$injuries_count'
                },
                'incidents':{
                    '$sum': 1
                }
            }
        }

        sort = {
            "$sort": {
                "total": -1
            }
        }

        project = {
            "$project": {
                "_id": 0,
                'name': "$_id." + field_match,
                "total": "$total",
                "incidents": "$incidents"
            }
        }
        aggregation_by_death = [match_by_death, group_by_death, sort, project]
        aggregation_by_injury = [match_by_injuries, group_by_injuries, sort, project]
        aggregation_by_property = [match_by_property, group_by_property, sort, project]
        result_death = self.mongo.db[params['dataset']].aggregate(aggregation_by_death)['result']
        result_injury = self.mongo.db[params['dataset']].aggregate(aggregation_by_injury)['result']
        result_property = self.mongo.db[params['dataset']].aggregate(aggregation_by_property)['result']

        index = 1
        for item in result_death:
            item['rank'] = index
            index = index + 1
        index = 1
        for item in result_injury:
            item['rank'] = index
            index = index + 1
        index = 1
        for item in result_property:
            item['rank'] = index
            index = index + 1

        json_result = {}
        json_result['death'] = result_death
        json_result['injury'] = result_injury
        json_result['property'] = result_property

        rendered_result = json_result
        return rendered_result

    def get_upazila_stats(self, params):
        field_match = 'upazila'
        value_match = params['upazila']
        match_by_property = {
            "$match": {
                field_match: {
                    "$nin": [
                        None
                    ]
                },
                'property_destroyed_count': {
                    "$ne": [0]
                },
                'violence_type': {
                    "$in": [
                        str(params['violence_type'])
                    ]
                },
                "incident_date": {"$gte": params['from_date'], "$lte": params['to_date']},
            }
        }
        match_by_death = {
            "$match": {
                field_match: {
                    "$nin": [
                        None
                    ]
                },
                'deaths_count': {
                    "$ne": [0]
                },
                'violence_type': {
                    "$in": [
                        str(params['violence_type'])
                    ]
                },
                "incident_date": {"$gte": params['from_date'], "$lte": params['to_date']},

            }
        }

        match_by_injuries = {
            "$match": {
                field_match: {
                    "$nin": [
                        None
                    ]
                },
                'injuries_count': {
                    "$ne": [0]
                },
                'violence_type': {
                    "$in": [
                        str(params['violence_type'])
                    ]
                },
                "incident_date": {"$gte": params['from_date'], "$lte": params['to_date']},

            }
        }
        group_by_death = {
            "$group": {
                "_id": {
                    field_match: "$" + field_match
                },
                'total': {
                    '$sum': '$deaths_count'
                },
                'incidents':{
                    '$sum': 1
                }
            }
        }
        group_by_property = {
            "$group": {
                "_id": {
                    field_match: "$" + field_match
                },
                'total': {
                    '$sum': '$property_destroyed_count'
                },
                'incidents':{
                    '$sum': 1
                }
            }
        }
        group_by_injuries = {
            "$group": {
                "_id": {
                    field_match: "$" + field_match
                },
                'total': {
                    '$sum': '$injuries_count'
                },
                'incidents':{
                    '$sum': 1
                }
            }
        }

        sort = {
            "$sort": {
                "total": -1
            }
        }

        project = {
            "$project": {
                "_id": 0,
                'name': "$_id." + field_match,
                "total": "$total",
                "incidents": "$incidents"
            }
        }

        project_match = {
            "$match": {
                "total": {"$gte": 0}
            }
        }
        aggregation_by_death = [match_by_death, group_by_death, sort, project, project_match]
        aggregation_by_injury = [match_by_injuries, group_by_injuries, sort, project, project_match]
        aggregation_by_property = [match_by_property, group_by_property, sort, project, project_match]
        result_death = self.mongo.db[params['dataset']].aggregate(aggregation_by_death)['result']
        result_injury = self.mongo.db[params['dataset']].aggregate(aggregation_by_injury)['result']
        result_property = self.mongo.db[params['dataset']].aggregate(aggregation_by_property)['result']

        index = 1
        for item in result_death:
            item['rank'] = index
            index = index + 1
        index = 1
        for item in result_injury:
            item['rank'] = index
            index = index + 1
        index = 1
        for item in result_property:
            item['rank'] = index
            index = index + 1

        json_result = {}
        json_result['death'] = result_death
        json_result['injury'] = result_injury
        json_result['property'] = result_property

        rendered_result = json_result
        return rendered_result

    def get_division_stats(self, params):
        field_match = 'division'
        value_match = params['division']
        match_by_property = {
            "$match": {
                field_match: {
                    "$nin": [
                        None
                    ]
                },
                'property_destroyed_count': {
                    "$ne": [0]
                },
                'violence_type': {
                    "$in": [
                        str(params['violence_type'])
                    ]
                },
                "incident_date": {"$gte": params['from_date'], "$lte": params['to_date']},

            }
        }
        match_by_death = {
            "$match": {
                field_match: {
                    "$nin": [
                        None
                    ]
                },
                'deaths_count': {
                    "$ne": [0]
                },
                'violence_type': {
                    "$in": [
                        str(params['violence_type'])
                    ]
                },
                "incident_date": {"$gte": params['from_date'], "$lte": params['to_date']},

            }
        }

        match_by_injuries = {
            "$match": {
                field_match: {
                    "$nin": [
                        None
                    ]
                },
                'injuries_count': {
                    "$ne": [0]
                },
                'violence_type': {
                    "$in": [
                        str(params['violence_type'])
                    ]
                },
                "incident_date": {"$gte": params['from_date'], "$lte": params['to_date']},

            }
        }
        group_by_death = {
            "$group": {
                "_id": {
                    field_match: "$" + field_match
                },
                'total': {
                    '$sum': '$deaths_count'
                },
                'incidents':{
                    '$sum': 1
                }
            }
        }
        group_by_property = {
            "$group": {
                "_id": {
                    field_match: "$" + field_match
                },
                'total': {
                    '$sum': '$property_destroyed_count'
                },
                'incidents':{
                    '$sum': 1
                }
            }
        }
        group_by_injuries = {
            "$group": {
                "_id": {
                    field_match: "$" + field_match
                },
                'total': {
                    '$sum': '$injuries_count'
                },
                'incidents':{
                    '$sum': 1
                }
            }
        }

        sort = {
            "$sort": {
                "total": -1
            }
        }

        project = {
            "$project": {
                "_id": 0,
                'name': "$_id." + field_match,
                "total": "$total",
                "incidents": "$incidents"
            }
        }
        aggregation_by_death = [match_by_death, group_by_death, sort, project]
        aggregation_by_injury = [match_by_injuries, group_by_injuries, sort, project]
        aggregation_by_property = [match_by_property, group_by_property, sort, project]
        result_death = self.mongo.db[params['dataset']].aggregate(aggregation_by_death)['result']
        result_injury = self.mongo.db[params['dataset']].aggregate(aggregation_by_injury)['result']
        result_property = self.mongo.db[params['dataset']].aggregate(aggregation_by_property)['result']

        index = 1
        for item in result_death:
            item['rank'] = index
            index = index + 1
        index = 1
        for item in result_injury:
            item['rank'] = index
            index = index + 1
        index = 1
        for item in result_property:
            item['rank'] = index
            index = index + 1

        json_result = {}
        json_result['death'] = result_death
        json_result['injury'] = result_injury
        json_result['property'] = result_property

        rendered_result = json_result
        return rendered_result

    def get_monthly_incidents_stats(self, params):
        match = self.build_match(params)
        data = None

        group = {
            '$group': {
                '_id': {
                    'month': {
                        '$substr': ['$incident_date', 5, 2]
                    }
                },
                'total_injury': {
                    '$sum': '$injuries_count'
                },
                'total_property': {
                    '$sum': '$property_destroyed_count'
                },
                'total_death': {
                    '$sum': '$deaths_count'
                }
            }
        }
        sort = {
            "$sort": {
                "_id.month": 1
            }
        }
        project = {
            "$project": {
                "_id": 0,
                'month': "$_id.month",
                'injuries': "$total_injury",
                'property': "$total_property",
                'death': "$total_death"

            }
        }
        data = self.mongo.db[params['dataset']].aggregate([match, group, sort, project])
        rendered_result = data['result']
        return rendered_result

    def get_quarterly_incidents_stats(self, params):
        match = self.build_match(params)
        data = None

        project = {
            "$project": {
                "incident_date": 1,
                'year': {
                    "$year": "$incident_date"
                },
                'injuries_count': 1,
                'property_destroyed_count': 1,
                'deaths_count': 1,
                "quarter": {
                    "$cond": [
                        {
                            "$lte": [
                                {
                                    "$month": "$incident_date"
                                },
                                3
                            ]
                        },
                        1,
                        {
                            "$cond": [
                                {
                                    "$lte": [
                                        {
                                            "$month": "$incident_date"
                                        },
                                        6
                                    ]
                                },
                                2,
                                {
                                    "$cond": [
                                        {
                                            "$lte": [
                                                {
                                                    "$month": "$incident_date"
                                                },
                                                9
                                            ]
                                        },
                                        3,
                                        4
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        }

        group = {
            "$group": {
                "_id": {
                    "quarter": "$quarter",
                    "year": "$year"
                },
                "incidents": {
                    "$sum": 1
                },
                'total_injury': {
                    '$sum': '$injuries_count'
                },
                'total_property': {
                    '$sum': '$property_destroyed_count'
                },
                'total_death': {
                    '$sum': '$deaths_count'
                }
            }
        }
        second_project = {
            "$project": {
                "_id": 0,
                "quarter": "$_id.quarter",
                "year": "$_id.year",
                "incidents": "$incidents",
                'injuries': "$total_injury",
                'property': "$total_property",
                'death': "$total_death"
            }
        }
        sort = {
            "$sort": {
                "year": 1
            }
        }
        query = [match, project, group, second_project, sort]
        data = self.mongo.db[params['dataset']].aggregate(query)
        rendered_result = data['result']
        return rendered_result

    def build_match(self, params):
        match = None
        if params['division'] != '' and params['district'] != '' and params['upazila'] != '':
            match = {
                "$match": {
                    'violence_month': {
                        "$nin": [
                            ""
                        ]
                    },
                    'violence_type': {
                        "$in": [
                            str(params['violence_type'])
                        ]
                    },
                    "incident_date": {"$gte": params['from_date'], "$lte": params['to_date']},
                    'division': params['division'],
                    'district': params['district'],
                    'upazila': params['upazila'],
                }
            }
        elif params['division'] != '' and params['district']:
            match = {
                "$match": {
                    'violence_type': {
                        "$in": [
                            str(params['violence_type'])
                        ]
                    },
                    "incident_date": {"$gte": params['from_date'], "$lte": params['to_date']},
                    'division': params['division'],
                    'district': params['district']
                }
            }
        elif params['division'] != '':
            match = {
                "$match": {
                    'violence_type': {
                        "$in": [
                            str(params['violence_type'])
                        ]
                    },
                    "incident_date": {"$gte": params['from_date'], "$lte": params['to_date']},
                    'division': params['division']
                }
            }
        else:
            match = {
                "$match": {
                    'violence_type': {
                        "$in": [
                            str(params['violence_type'])
                        ]
                    },
                    "incident_date": {"$gte": params['from_date'], "$lte": params['to_date']},
                }
            }
        return match

    def get_rank_stats(self, params):
        match = self.build_match(params)
        group_by_id = None
        if params['division'] != '' and params['district'] != '' and params['upazila'] != '':
            group_by_id = "upazila"
        elif params['division'] != '' and params['district']:
            group_by_id = "upazila"
        elif params['division'] != '':
            group_by_id = "district"
        else:
            group_by_id = "division"
        group = {
            "$group": {
                "_id": {
                    group_by_id: '$' + group_by_id
                },
                "incidents": {
                    "$sum": 1
                },
                'total_injury': {
                    '$sum': '$injuries_count'
                },
                'total_property': {
                    '$sum': '$property_destroyed_count'
                },
                'total_death': {
                    '$sum': '$deaths_count'
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
                'name': "$_id." + group_by_id,
                "incidents": "$incidents",
                'injuries': "$total_injury",
                'property': "$total_property",
                'death': "$total_death"
            }
        }
        query = [match, group, sort, project]
        data = self.mongo.db[params['dataset']].aggregate(query)
        rendered_result = data['result']
        return rendered_result

    def get_incidents_stats(self, params):
        match = self.build_match(params)
        group_by_id = None
        if params['division'] != '' and params['district'] != '' and params['upazila'] != '':
            group_by_id = "upazila"
        elif params['division'] != '' and params['district']:
            group_by_id = "upazila"
        elif params['division'] != '':
            group_by_id = "district"
        else:
            group_by_id = "division"

        group = {
            "$group": {
                "_id": {
                    group_by_id: '$' + group_by_id
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
                'name': "$_id." + group_by_id,
                "incidents": "$incidents"
            }
        }
        query = [match, group, sort, project]
        data = self.mongo.db[params['dataset']].aggregate(query)
        rendered_result = data['result']
        return rendered_result

    def get_violence_types(self, params):
        violence_types = self.mongo.db[params['dataset']].distinct('violence_type')
        rendered_result = violence_types
        return rendered_result

    def get_incident_types_by_time(self, params):
        match = self.build_match(params)
        group = {
            '$group': {
                '_id': {
                    'date': '$incident_date'
                },
                'total_injury': {
                    '$sum': '$injuries_count'
                },
                'total_property': {
                    '$sum': '$property_destroyed_count'
                },
                'total_death': {
                    '$sum': '$deaths_count'
                },
                'incidents': {
                    '$sum': 1
                }
            }
        }
        project = {
            '$project': {
                '_id': 0,
                'date': '$_id.date',
                'death': '$total_death',
                'incidents': '$incidents',
                'property': '$total_property',
                'injuries': '$total_injury'
            }
        }
        sort = {
            '$sort': {
                'date': 1
            }
        }
        data = self.mongo.db[params['dataset']].aggregate([match, group, project, sort])
        rendered_result = data['result']
        return rendered_result

    def get_top_3_stats(self, params):
        match = self.build_match(params)

        casualties = self.mongo.db[params['dataset']].aggregate([
            {
                "$unwind": "$responders"
            },
            match,
            {
                "$group": {
                    "_id": {
                        'casualties': "$responders"
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

        property = self.mongo.db[params['dataset']].aggregate([
            {
                "$unwind": "$property_destroyed_type"
            },
            match,
            {
                "$group": {
                    "_id": {
                        'property': "$property_destroyed_type"
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

        perpetrator = self.mongo.db[params['dataset']].aggregate([ \
            {
                "$unwind": "$violence_actor"
            },
            match,
            {
                "$group": {
                    "_id": {
                        'perpetrator': "$violence_actor"
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
        unwind_by = ""
        if params['dataset'] == 'idams':
            unwind_by = "causes"
        else:
            unwind_by = "causes"
        motivations = self.mongo.db[params['dataset']].aggregate([ \
            {
                "$unwind": "$"+unwind_by
            },
            match,
            {
                "$group": {
                    "_id": {
                        'motivations': "$"+unwind_by
                    },
                    "motivations_count": {
                        "$sum": 1
                    }

                }
            },
            {
                "$sort": {
                    "motivations_count": -1,
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "motivations": "$_id.motivations",
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
            "perpetrator": perpetrator,
            "motivations": motivations
        }

        return result

    def get_map_victims_count(self, params):
        match = self.build_match(params)
        group_by_division = {
            "$group": {
                "_id": {
                    'division': '$division'
                },
                "incidents": {
                    "$sum": 1
                }
            }
        }
        group_by_district = {
            "$group": {
                "_id": {
                    'district': '$upazila'
                },
                "incidents": {
                    "$sum": 1
                }
            }
        }
        group_by_upazila = group = {
            "$group": {
                "_id": {
                    'upazila': '$upazila'
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

        project_division = {
            "$project": {
                "_id": 0,
                'division': "$_id.division",
                "incidents": "$incidents"
            }
        }
        project_district = {
            "$project": {
                "_id": 0,
                'district': "$_id.district",
                "incidents": "$incidents"
            }
        }
        project_upazila = {
            "$project": {
                "_id": 0,
                'upazila': "$_id.upazila",
                "incidents": "$incidents"
            }
        }
        result = {}
        division_aggregation = [match, group_by_division, sort, project_division]
        district_aggregation = [match, group_by_district, sort, project_district]
        upazila_aggregation = [match, group_by_upazila, sort, project_upazila]

        result['divisions'] = self.mongo.db[params['dataset']].aggregate(division_aggregation)['result']
        result['districts'] = self.mongo.db[params['dataset']].aggregate(district_aggregation)['result']
        result['upazilas'] = self.mongo.db[params['dataset']].aggregate(upazila_aggregation)['result']

        return result

    def get_census_info(self, params):
        match = None
        if params['division'] != '' and params['district'] != '' and params['upazila'] != '':
            match = {
                "$match": {
                    'division': params['division'],
                    'district': params['district'],
                    'upazila': params['upazila'],
                }
            }
        elif params['division'] != '' and params['district']:
            match = {
                "$match": {
                    'division': params['division'],
                    'district': params['district']
                }
            }
        elif params['division'] != '':
            match = {
                "$match": {
                    'division': params['division']
                }
            }
        else:
            match = {
                "$match": {
                }
            }
        result = self.mongo.db.census.aggregate([
            match,
            {
                "$group": {
                    "_id": {
                    },
                    "population": {
                        "$sum": "$population"
                    },
                    "poverty":{
                        "$avg":"$poverty"
                    },
                    "muslim": {
                        "$sum": "$Muslim"
                    },
                    "buddhist": {
                        "$sum": "$Buddhist"
                    },
                    "hindu": {
                        "$sum": "$Hindu"
                    },
                    "christian": {
                        "$sum": "$Christian"
                    },
                    "other": {
                        "$sum": "$Other"
                    },


                }
            },
            {
                "$project": {
                    "_id": 0,
                    "population": "$population",
                    "poverty":{ "$substr": [ "$poverty", 0, 4 ]},
                    "muslim": "$muslim",
                    "buddhist": "$buddhist",
                    "hindu": "$hindu",
                    "christian": "$christian",
                    "other": "$other",
                }
            }]
        )['result']
        return result