# -*- coding: UTF-8 -*-
import csv
import os
import re
from datetime import datetime
from pymongo import MongoClient
import json

# Connect to defualt local instance of MongoClient
client = MongoClient()

# Get database and collection
db = client.bpo
collection = db.mgr


def parse():
    collection.remove({})

    print "Importing Data"
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print dir_path
    json_structure = {
        "VNUM": "violence_number",
        "RDATE": "report_date",
        "NCODE": "name_of_coder",
        "LUPC": "upazila",
        "LDIS": "district",
        "LUNW": "village",
        "WNONP": "woundednon_participant",
        "VREF": "violence_reference",
        "VCONT": "violent_event_continuation",
        "VTPRE": "violent_event_time_precision",
        "VTAGM": "violent_event_tag_multiple",
        "VTAGT": "violent_event_tag_trigger",
        "VTAGC": "violent_event_tag_continuation",
        "VDAY": "violence_day",
        "VMONT": "violence_month",
        "VYEAR": "violence_year",
        "VNONP": "violence_non_participants",
        "VTRIGC": "conflicting_trigger_of_violence",
        "AAVER": "arrested_averaged",
        "VPOL": "violence_police_role",
        "ANONP": "arrested_non_participant",
        "VREMU": "violence_report_multiple_events",
        "CAVER": "casualties_averaged",
        "VSOUR": "violence_source",
        "WAVER": "wounded_averaged",
        "VHART": "violent_event_hartal",
        "CNONP": "casualties_non_participant",
        "VACTB1": "violence_actor_b_1",
        "VACTB2": "violence_actor_b_2",
        "VACTB3": "violence_actor_b_3",
        "WOUACA": "total_number_of_wounded_reported_actor_a",
        "WOUACB": "total_number_of_wounded_reported_actor_b",
        "VTRIG1": "trigger_of_violence_1",
        "VTRIG2": "trigger_of_violence_2",
        "VTYP1": "violence_type_1",
        "VTYP2": "violence_type_2",
        "VTYP3": "violence_type_3",
        "WOUTAR": "total_number_of_wounded_reported_target",
        "ARRTAR": "total_number_of_arrested_reported_target",
        "ARRACB": "total_number_of_arrested_reported_actor_b",
        "CASTAR": "total_number_of_casualties_reported_target",
        "DPROP1": "destruction_of_property_1",
        "DPROP2": "destruction_of_property_2",
        "DPROP3": "destruction_of_property_3",
        "NDPRO1": "number_of_property_destroyed_1",
        "NDPRO2": "number_of_property_destroyed_2",
        "NDPRO3": "number_of_property_destroyed_3",
        "VTAR1": "violence_target_group_1",
        "VTAR2": "violence_target_group_2",
        "VTAR3": "violence_target_group_3",
        "VACTA1": "violence_actor_1",
        "VACTA2": "violence_actor_2",
        "VACTA3": "violence_actor_3",
        "CASACA": "total_number_of_casualties_reported_actor_a",
        "CASACB": "total_number_of_casualties_reported_actor_b",
        "ARRACA": "total_number_of_arrested_reported_actor_a"
    }
    violence_source = {
        "1": "Daily Star",
        "2": "Prothom Alu",
        "3": "Ittefaq",
        "4": "Inqilab",
        "5": "Manab Zamin"
    }
    violence_type = {
        "0": "Unspecified",
        "000": "Unspecified",
        "100": "Clash/battle: Interaction between political parties, groups and fractions",
        "110": "Clash/battle: Interaction between political parties, groups and fractions",
        "111": "Clash/battle: Interaction between political parties, groups and fractions",
        "112": "Clash/battle: Interaction between political parties, groups and fractions",
        "113": "Clash/battle: Interaction between political parties, groups and fractions",
        "114": "Clash/battle: Interaction between political parties, groups and fractions",
        "115": "Clash/battle: Interaction between political parties, groups and fractions",
        "116": "Clash/battle: Interaction between political parties, groups and fractions",
        "117": "Clash/battle: Interaction between political parties, groups and fractions",
        "120": "Clash/battle: Interaction between political parties, groups and fractions",
        "200": "Attack: Coordinated action each-other political parties, groups, fractions and authorities",
        "210": "Attack: Coordinated action each-other political parties, groups, fractions and authorities",
        "211": "Attack: Coordinated action each-other political parties, groups, fractions and authorities",
        "212": "Attack: Coordinated action each-other political parties, groups, fractions and authorities",
        "213": "Attack: Coordinated action each-other political parties, groups, fractions and authorities",
        "214": "Attack: Coordinated action each-other political parties, groups, fractions and authorities",
        "215": "Attack: Coordinated action each-other political parties, groups, fractions and authorities",
        "216": "Attack: Coordinated action each-other political parties, groups, fractions and authorities",
        "217": "Attack: Coordinated action each-other political parties, groups, fractions and authorities",
        "220": "Attack: Coordinated action each-other political parties, groups, fractions and authorities",
        "300": "Destruction of property",
        "310": "Destruction of property",
        "320": "Destruction by arson attack",
        "400": "High and low impact bombing",
        "410": "High and low impact bombing",
        "420": "High and low impact bombing",
        "500": "Abduction, kidnap, hostage and rape",
        "600": "Abduction, kidnap, hostage and rape",
        "700": "Abduction, kidnap, hostage and rape",
        "999": "Other types of Political violence"
    }
    violence_trigger_1 = {
        "0": "Unspecified",
        "100": "Political",
        "110": "Political",
        "120": "Political",
        "130": "Political",
        "140": "Political",
        "150": "Political",
        "160": "Political",
        "170": "Political",
        "180": "Political",
        "190": "Political",
        "200": "Political",
        "210": "Socio-economic",
        "220": "Socio-economic",
        "230": "Socio-economic",
        "290": "Socio-economic",
        "300": "Religion as trigger",
        "310": "Religion as trigger",
        "320": "Religion as trigger",
        "390": "Religion as trigger",
        "400": "Judicial trial and arrest",
        "410": "Judicial trial and arrest",
        "411": "Judicial trial and arrest",
        "420": "Judicial trial and arrest",
        "430": "Judicial trial and arrest",
        "490": "Judicial trial and arrest",
        "500": "Political",
        "510": "Political",
        "520": "Political",
        "530": "Political",
        "540": "Political",
        "590": "Political",
        "600": "Access to resources",
        "610": "Access to resources",
        "611": "Access to resources",
        "612": "Access to resources",
        "619": "Access to resources",
        "620": "Access to resources",
        "621": "Access to resources",
        "622": "Access to resources",
        "623": "Access to resources",
        "624": "Access to resources",
        "629": "Access to resources",
        "630": "Access to resources",
        "631": "Access to resources",
        "632": "Access to resources",
        "633": "Access to resources",
        "634": "Access to resources",
        "635": "Access to resources",
        "636": "Access to resources",
        "637": "Access to resources",
        "638": "Access to resources",
        "639": "Access to resources",
        "699": "Access to resources",
        "700": "Organizational dynamics",
        "710": "Organizational dynamics",
        "720": "Organizational dynamics",
        "730": "Organizational dynamics",
        "799": "Organizational dynamics",
        "800": "Organizational dynamics",
        "810": "Organizational dynamics",
        "820": "Organizational dynamics",
        "890": "Organizational dynamics",
        "998": "Others",
        "999": "Others"
    }

    event_location_district = {
        "0": "Unspecified",
        "100": "Barisal",
        "101": "Barguna",
        "102": "Barisal",
        "103": "Bhola",
        "104": "Jhalokati",
        "105": "Patuakhali",
        "106": "Pirojpur",
        "200": "Chittagong",
        "201": "Bandarban",
        "202": "Brahmanbaria",
        "203": "Chandpur",
        "204": "Chittagong",
        "205": "Comilla",
        "206": "Cox’s Bazar",
        "207": "Feni",
        "208": "Khagrachhari",
        "209": "Lakshmipur",
        "210": "Noakhali",
        "211": "Rangamati",
        "300": "Dhaka",
        "301": "Dhaka",
        "302": "Faridpur",
        "303": "Gazipur",
        "304": "Gopalganj",
        "305": "Jamalpur",
        "306": "Kishoreganj",
        "307": "Kishoreganj",
        "308": "Manikganj",
        "309": "Munshiganj",
        "310": "Mymensingh",
        "311": "Mymensingh",
        "312": "Narsingdi",
        "313": "Natrakona",
        "314": "Rajbari",
        "315": "Shariatpur",
        "316": "Sherpur",
        "317": "Tangail",
        "400": "Khulna",
        "401": "Bagarhat",
        "402": "Chuadanga",
        "403": "Jessore",
        "404": "Jhenaidah",
        "405": "Khulna",
        "406": "Kushtia",
        "407": "Magura",
        "408": "Meherpur",
        "409": "Narail",
        "410": "Satkhira",
        "500": "Rajshahi",
        "501": "Bogra",
        "502": "Joypurhat",
        "503": "Naogaon",
        "504": "Natore",
        "505": "Nawabganj",
        "506": "Pabna",
        "507": "Rajshahi",
        "508": "Sirajganj",
        "600": "Rangpur",
        "601": "Dinajpur",
        "602": "Gaibandha",
        "603": "Kurigram",
        "604": "Lalmonirhat",
        "605": "Nilphamari",
        "606": "Panchagarh",
        "607": "Rangpur",
        "608": "Thakurgoan",
        "700": "Sylhet",
        "701": "Habiganj",
        "702": "Maulvibazar",
        "703": "Sunamganj",
        "704": "Sylhet",
        "800": "Multiple"
    }
    violence_actor_1 = {
        "0": "Unspecified",
        "100": "State Actors",
        "110": "State Actors",
        "111": "State Actors",
        "112": "State Actors",
        "113": "State Actors",
        "114": "State Actors",
        "115": "State Actors",
        "118": "State Actors",
        "120": "State Actors",
        "121": "State Actors",
        "128": "State Actors",
        "130": "State Actors",
        "140": "State Actors",
        "141": "State Actors",
        "142": "State Actors",
        "143": "State Actors",
        "144": "State Actors",
        "188": "State Actors",
        "200": "Political Party",
        "210": "Awami League (AL) and affiliated fronts",
        "211": "Awami League (AL) and affiliated fronts",
        "212": "Awami League (AL) and affiliated fronts",
        "213": "Awami League (AL) and affiliated fronts",
        "214": "Awami League (AL) and affiliated fronts",
        "215": "Awami League (AL) and affiliated fronts",
        "216": "Awami League (AL) and affiliated fronts",
        "217": "Awami League (AL) and affiliated fronts",
        "218": "Awami League (AL) and affiliated fronts",
        "219": "Awami League (AL) and affiliated fronts",
        "220": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "221": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "222": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "223": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "224": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "225": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "226": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "227": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "228": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "229": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "230": "Jamaat-e- Islami (JI) and affiliated fronts",
        "231": "Jamaat-e- Islami (JI) and affiliated fronts",
        "232": "Jamaat-e- Islami (JI) and affiliated fronts",
        "233": "Jamaat-e- Islami (JI) and affiliated fronts",
        "234": "Jamaat-e- Islami (JI) and affiliated fronts",
        "235": "Jamaat-e- Islami (JI) and affiliated fronts",
        "236": "Jamaat-e- Islami (JI) and affiliated fronts",
        "237": "Jamaat-e- Islami (JI) and affiliated fronts",
        "238": "Jamaat-e- Islami (JI) and affiliated fronts",
        "239": "Jamaat-e- Islami (JI) and affiliated fronts",
        "240": "Jatiya Party (JP) and affiliated fronts",
        "241": "Jatiya Party (JP) and affiliated fronts",
        "242": "Jatiya Party (JP) and affiliated fronts",
        "243": "Jatiya Party (JP) and affiliated fronts",
        "244": "Jatiya Party (JP) and affiliated fronts",
        "245": "Jatiya Party (JP) and affiliated fronts",
        "246": "Jatiya Party (JP) and affiliated fronts",
        "247": "Jatiya Party (JP) and affiliated fronts",
        "248": "Jatiya Party (JP) and affiliated fronts",
        "249": "Jatiya Party (JP) and affiliated fronts",
        "250": "Left-Wing Parties",
        "251": "Left-Wing Parties",
        "252": "Left-Wing Parties",
        "253": "Left-Wing Parties",
        "254": "Left-Wing Parties",
        "259": "Left-Wing Parties",
        "260": "Islamist Political Parties",
        "261": "Islamist Political Parties",
        "262": "Islamist Political Parties",
        "263": "Islamist Political Parties",
        "269": "Islamist Political Parties",
        "270": "Chittagong Hill Tracts (CHT) based groups",
        "288": "Other*",
        "300": "Student Group",
        "310": "Awami League (AL) and affiliated fronts",
        "311": "Awami League (AL) and affiliated fronts)",
        "312": "Awami League (AL) and affiliated fronts",
        "313": "Awami League (AL) and affiliated fronts",
        "314": "Awami League (AL) and affiliated fronts",
        "315": "Awami League (AL) and affiliated fronts",
        "316": "Awami League (AL) and affiliated fronts",
        "317": "Awami League (AL) and affiliated fronts",
        "318": "Awami League (AL) and affiliated fronts",
        "319": "Awami League (AL) and affiliated fronts",
        "320": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "321": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "322": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "323": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "324": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "325": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "326": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "327": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "328": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "329": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "330": "Jamaat-e- Islami (JI) and affiliated fronts",
        "331": "Jamaat-e- Islami (JI) and affiliated fronts",
        "332": "Jamaat-e- Islami (JI) and affiliated fronts",
        "333": "Jamaat-e- Islami (JI) and affiliated fronts",
        "334": "Jamaat-e- Islami (JI) and affiliated fronts",
        "335": "Jamaat-e- Islami (JI) and affiliated fronts",
        "336": "Jamaat-e- Islami (JI) and affiliated fronts",
        "337": "Jamaat-e- Islami (JI) and affiliated fronts",
        "338": "Jamaat-e- Islami (JI) and affiliated fronts",
        "339": "Jamaat-e- Islami (JI) and affiliated fronts",
        "340": "Jatiya Party (JP) and affiliated fronts",
        "341": "Jatiya Party (JP) and affiliated fronts",
        "342": "Jatiya Party (JP) and affiliated fronts",
        "343": "Jatiya Party (JP) and affiliated fronts",
        "344": "Jatiya Party (JP) and affiliated fronts",
        "345": "Jatiya Party (JP) and affiliated fronts",
        "346": "Jatiya Party (JP) and affiliated fronts",
        "347": "Jatiya Party (JP) and affiliated fronts",
        "348": "Jatiya Party (JP) and affiliated fronts",
        "349": "Jatiya Party (JP) and affiliated fronts",
        "350": "Left-Wing Parties",
        "351": "Left-Wing Parties",
        "352": "Left-Wing Parties",
        "353": "Left-Wing Parties",
        "358": "Left-Wing Parties",
        "360": "Islamist Political Parties",
        "388": "Islamist Political Parties",
        "400": "Youth (Jubo) Group",
        "410": "Awami League (AL) and affiliated fronts",
        "411": "Awami League (AL) and affiliated fronts",
        "412": "Awami League (AL) and affiliated fronts",
        "414": "Awami League (AL) and affiliated fronts",
        "415": "Awami League (AL) and affiliated fronts",
        "416": "Awami League (AL) and affiliated fronts",
        "417": "Awami League (AL) and affiliated fronts",
        "419": "Awami League (AL) and affiliated fronts",
        "420": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "421": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "422": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "424": "Bangladesh Nationalist Party (BNP) and affiliated fronts)",
        "425": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "426": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "427": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "429": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "430": "Jamaat-e- Islami (JI) and affiliated fronts",
        "431": "Jamaat-e- Islami (JI) and affiliated fronts",
        "432": "Jamaat-e- Islami (JI) and affiliated fronts",
        "434": "Jamaat-e- Islami (JI) and affiliated fronts",
        "435": "Jamaat-e- Islami (JI) and affiliated fronts",
        "436": "Jamaat-e- Islami (JI) and affiliated fronts",
        "437": "Jamaat-e- Islami (JI) and affiliated fronts",
        "439": "Jamaat-e- Islami (JI) and affiliated fronts",
        "440": "Jatiya Party (JP) and affiliated fronts",
        "441": "Jatiya Party (JP) and affiliated fronts",
        "442": "Jatiya Party (JP) and affiliated fronts",
        "444": "Jatiya Party (JP) and affiliated fronts",
        "445": "Jatiya Party (JP) and affiliated fronts",
        "446": "Jatiya Party (JP) and affiliated fronts",
        "447": "Jatiya Party (JP) and affiliated fronts",
        "449": "Jatiya Party (JP) and affiliated fronts",
        "450": "Left-Wing Parties",
        "451": "Left-Wing Parties",
        "452": "Left-Wing Parties",
        "453": "Left-Wing Parties",
        "454": "Left-Wing Parties",
        "455": "Left-Wing Parties",
        "460": "Islamist Political Parties",
        "461": "Islamist Political Parties",
        "462": "Islamist Political Parties",
        "463": "Islamist Political Parties)",
        "464": "Islamist Political Parties",
        "465": "Islamist Political Parties",
        "488": "Islamist Political Parties",
        "500": "Islamist Violent Groups",
        "510": "Islamist Violent Groups",
        "520": "Islamist Violent Groups",
        "530": "Islamist Violent Groups",
        "540": "Islamist Violent Groups",
        "550": "Islamist Violent Groups",
        "560": "Islamist Violent Groups",
        "588": "Islamist Violent Groups",
        "600": "Alliance of actors",
        "610": "Awami League (AL) and affiliated fronts",
        "611": "Awami League (AL) and affiliated fronts",
        "612": "Awami League (AL) and affiliated fronts",
        "620": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "621": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "622": "Bangladesh Nationalist Party (BNP) and affiliated fronts",
        "630": "Jamaat-e- Islami (JI) and affiliated fronts",
        "631": "Jamaat-e- Islami (JI) and affiliated fronts",
        "632": "Jamaat-e- Islami (JI) and affiliated fronts",
        "640": "Left-Wing Parties",
        "650": "Islamist Political Parties",
        "660": "Extremist Left Rebel Groups",
        "661": "Chittagong Hill Tracts (CHT) based groups",
        "662": "Extremist Left Rebel Groups",
        "670": "Occupational group/organization",
        "680": "Islamist Violent Groups",
        "699": "Islamist Violent Groups",
        "700": "Extremist Left Rebel Groups",
        "710": "Extremist Left Rebel Groups",
        "720": "Chittagong Hill Tracts (CHT) based groups",
        "730": "Chittagong Hill Tracts (CHT) based groups",
        "799": "Extremist Left Rebel Groups",
        "800": "Ethnic and religious Minority Groups",
        "810": "Ethnic and religious Minority Groups",
        "811": "Ethnic and religious Minority Groups",
        "812": "Ethnic and religious Minority Groups",
        "813": "Ethnic and religious Minority Groups",
        "814": "Ethnic and religious Minority Groups",
        "815": "Ethnic and religious Minority Groups",
        "816": "Ethnic and religious Minority Groups",
        "817": "Ethnic and religious Minority Groups",
        "819": "Ethnic and religious Minority Groups",
        "820": "Ethnic and religious Minority Groups",
        "830": "Ethnic and religious Minority Groups",
        "831": "Ethnic and religious Minority Groups",
        "832": "Ethnic and religious Minority Groups",
        "833": "Ethnic and religious Minority Groups",
        "839": "Ethnic and religious Minority Groups",
        "840": "Ethnic and religious Minority Groups",
        "900": "Occupational group/organization",
        "910": "Occupational group/organization",
        "920": "Occupational group/organization",
        "921": "Occupational group/organization",
        "922": "Occupational group/organization",
        "923": "Occupational group/organization",
        "929": "Occupational group/organization",
        "930": "Occupational group/organization",
        "940": "Occupational group/organization",
        "950": "Occupational group/organization",
        "951": "Occupational group/organization",
        "952": "Occupational group/organization",
        "959": "Occupational group/organization",
        "960": "Occupational group/organization",
        "970": "Occupational group/organization",
        "980": "Occupational group/organization",
        "988": "Occupational group/organization",
        "995": "Others known and unknown actors",
        "996": "Others known and unknown actors",
        "997": "Others known and unknown actors",
        "998": "Others known and unknown actors",
        "999": "Others known and unknown actors"
    }
    violence_police_role = {
        "100": "Police not mentioned",
        "200": "Police is participant in the violent event from the start",
        "322": "Police participates in violent event on side of VACTA",
        "300": "Police arrives during the violent event",
        "310": "Police remains inactive during violent event",
        "320": "Police intervenes during the violent event ",
        "321": "Police separates sides in violent event",
        "323": "Police participates in violent event on side of VACTA",
        "400": "Police arrives after the violent event"
    }
    destruction_of_property = {
        "0": "Unspecified",
        "100": "Agrarian",
        "110": "Fields",
        "120": "Harvested or stored crops",
        "130": "Farm Machinery",
        "140": "Farm Buildings",
        "150": "Farm Buildings",
        "199": "Other*",
        "200": "Industrial",
        "210": "Factory structure/building",
        "211": "Garments",
        "218": "Other",
        "220": "Machines",
        "221": "Garments",
        "228": "Other",
        "299": "Other*",
        "300": "Commercial",
        "310": "Shop",
        "320": "Market",
        "330": "Restaurant",
        "340": "Bank",
        "350": "Newspaper office",
        "360": "Warehouse",
        "370": "Harbour/port facilities",
        "380": "Filling station",
        "399": "Other*",
        "400": "Public facilities",
        "410": "Train station",
        "420": "Bus station",
        "430": "Public streets/squares",
        "440": "Monument",
        "450": "Meeting Hall",
        "460": "School Building",
        "470": "University/College building",
        "499": "Other*",
        "500": "Government property",
        "510": "Building",
        "511": "Office of local government (city, pourashava, union)",
        "512": "Office of district government",
        "513": "Office of central government",
        "514": "Parliament",
        "519": "Other*",
        "520": "Government vehicle",
        "521": "Police car",
        "522": "Government car",
        "522": "Other*",
        "599": "Other*",
        "600": "Religious building",
        "610": "Muslim",
        "620": "Hindu",
        "630": "Buddhist",
        "640": "Christian",
        "699": "Other*",
        "700": "Residence",
        "710": "House (general)",
        "720": "House (residence politician)",
        "730": "Apartment",
        "740": "Hotel",
        "799": "Other*",
        "800": "Transport/Vehicles",
        "810": "Rickshaw",
        "820": "CNG",
        "830": "Motorbike",
        "840": "Car",
        "850": "Bus",
        "860": "Train",
        "870": "Boat",
        "880": "Other private transport*",
        "890": "Other public transport*",
        "900": "Organizational office/headquarters",
        "910": "Political party",
        "911": "Office",
        "912": "Headquarters",
        "920": "Student group",
        "921": "Office",
        "922": "Headquarters",
        "930": "Youth Group",
        "931": "Office",
        "932": "Headquarters",
        "940": "Labour Union ",
        "941": "Office",
        "942": "Headquarters",
        "990": "Other*",
        "997": "Furniture",
        "998": "Banner",
        "999": "Other*"
    }

    upazila = {
        "100": "BARISAL DIVISION",
        "101": "BARGUNA DISTRICT",
        "101001": "Barguna",
        "101002": "Amtali",
        "101003": "Bamna",
        "101004": "Betagi",
        "101005": "Patharghata",
        "101006": "Taltoli",
        "102": "BARISAL DISTRICT",
        "102001": "Barisal",
        "102002": "Agailjhara",
        "102003": "Babuganj",
        "102004": "Bakerganj",
        "102005": "Banaripara",
        "102006": "Gaurnadi",
        "102007": "Hizla",
        "102008": "Mehendiganj",
        "102009": "Muladi",
        "102010": "Wazirpur",
        "103": "BHOLA DISTRICT",
        "103001": "Bhola",
        "103002": "Burhanuddin",
        "103003": "Char Fasson",
        "103004": "Daulatkhan",
        "103005": "Lalmohan",
        "103006": "Manpura",
        "103007": "Tazumuddin",
        "104": "JHALOKATI DISTRICT",
        "104001": "Jhalokati",
        "104002": "Kathalia",
        "104003": "Nalchity",
        "104004": "Rajapur",
        "105": "PATUAKHALI DISTRICT",
        "105001": "Patuakhali",
        "105002": "Dashmina",
        "105003": "Galachipa",
        "105004": "Kalapara",
        "105005": "Mirzaganj",
        "105006": "Bauphal",
        "105007": "Rangabali",
        "105008": "Dumki",
        "106": "PIROJPUR DISTRICT",
        "106001": "Pirojpur",
        "106002": "Kawkhali",
        "106003": "Mathbaria",
        "106004": "Nazirpur",
        "106005": "Bhandaria",
        "106006": "Nesarabad/Swarupkati",
        "106007": "Zianagor",
        "200": "CHITTAGONG DIVISION",
        "201": "BANDARBAN DISTRICT",
        "201001": "Bandarban",
        "201002": "Ali Kadam",
        "201003": "Lama",
        "201004": "Naikhongchhari",
        "201005": "Rowangchhari",
        "201006": "Ruma",
        "201007": "Thanchi",
        "202": "BRAHMANBARIA DISTRICT",
        "202001": "Brahmanbaria",
        "202002": "Bancharampur",
        "202003": "Akhaura",
        "202004": "Kasba",
        "202005": "Nabinagar",
        "202006": "Nasirnagar",
        "202007": "Sarail",
        "202008": "Ashuganj",
        "202009": "Bijoynagar",
        "203": "CHANDPUR DISTRICT",
        "203001": "Chandpur",
        "203002": "Faridganj",
        "203003": "Haimchar",
        "203004": "Haziganj",
        "203005": "Kachua",
        "203006": "Matlab Dakshin",
        "203006": "Matlab Uttar",
        "203007": "Shahrasti",
        "204": "CHITTAGONG DISTRICT",
        "204001": "Chittagong",
        "204002": "Anwara",
        "204003": "Banshkhali",
        "204004": "Boalkhali",
        "204005": "Chandanaish",
        "204006": "Fatikchhari",
        "204006": "Hathazari",
        "204007": "Karnaphuli",
        "204008": "Lohagara",
        "204009": "Mirsharai",
        "204010": "Patiya",
        "204011": "Rangunia",
        "204012": "Raozan",
        "204013": "Sandwip",
        "204014": "Satkania",
        "204015": "Sitakunda",
        "205": "COMILLA DISTRICT",
        "205001": "Comilla",
        "205002": "South Comilla",
        "205003": "Barura",
        "205004": "Brahmanpara",
        "205005": "Burichang",
        "205006": "Chandina",
        "205007": "Chauddagram",
        "205008": "Daudkandi",
        "205009": "Debidwar",
        "205010": "Homna",
        "205011": "Laksam",
        "205012": "Muradnagar",
        "205013": "Nangalkot",
        "205014": "Meghna",
        "205015": "Titash",
        "205016": "Monohargonj",
        "206": "COX'S BAZAR DISTRICT",
        "206001": "Cox's Bazar",
        "206002": "Chakaria",
        "206003": "Kutubdia",
        "206004": "Maheshkhali",
        "206005": "Ramu",
        "206006": "Teknaf",
        "206007": "Ukhia",
        "206008": "Pekua",
        "207": "FENI DISTRICT",
        "207001": "Feni",
        "207002": "Chhagalnaiya",
        "207003": "Daganbhuiyan",
        "207004": "Parshuram",
        "207005": "Sonagazi",
        "207006": "Fulgazi",
        "208": "KHAGRACHHARI DISTRICT",
        "208001": "Khagrachhari Sadr",
        "208002": "Dighinala",
        "208003": "Lakshmichhari",
        "208004": "Mahalchhari",
        "208005": "Manikchhari",
        "208006": "Matiranga",
        "208007": "Panchhari",
        "208008": "Ramgarh",
        "209": "LAKSHMIPUR DISTRICT",
        "209001": "Lakshmipur",
        "209002": "Raipur",
        "209003": "Ramganj",
        "209004": "Ramgati",
        "209005": "Kamalnagar",
        "210": "NOAKHALI DISTRICT",
        "210001": "Noakhali",
        "210002": "Begumganj",
        "210003": "Chatkhil",
        "210004": "Companiganj",
        "210005": "Hatiya",
        "210006": "Senbagh",
        "210007": "Sonaimuri",
        "210008": "Subarnachar",
        "210009": "Kabirhat",
        "211": "RANGAMATI DISTRICT",
        "211001": "Rangamati",
        "211002": "Bagaichhari",
        "211003": "Barkal",
        "211004": "Kawkhali (Betbunia)",
        "211005": "Belaichhari",
        "211006": "Kaptai",
        "211007": "Juraichhari",
        "211008": "Langadu",
        "211009": "Naniyachar",
        "211010": "Rajasthali",
        "300": "DHAKA DIVISION",
        "301": "DHAKA DISTRICT",
        "301001": "Dhaka",
        "301002": "Dhamrai",
        "301003": "Dohar",
        "301004": "Keraniganj",
        "301005": "Nawabganj",
        "301006": "Savar",
        "302": "FARIDPUR DISTRICT",
        "302001": "Faridpur",
        "302002": "Alfadanga",
        "302003": "Bhanga",
        "302004": "Boalmari",
        "302005": "Charbhadrasan",
        "302006": "Madhukhali",
        "302007": "Nagarkanda",
        "302008": "Sadarpur",
        "302009": "Saltha",
        "303": "GAZIPUR DISTRICT",
        "303001": "Gazipur",
        "303002": "Kaliakair",
        "303003": "Kaliganj",
        "303004": "Kapasia",
        "303005": "Sreepur",
        "304": "GOPALGANJ DISTRICT",
        "304001": "Gopalganj",
        "304002": "Kashiani",
        "304003": "Kotalipara",
        "304004": "Muksudpur",
        "304005": "Tungipara",
        "305": "JAMALPUR DISTRICT",
        "305001": "Jamalpur",
        "305002": "Baksiganj",
        "305003": "Dewanganj",
        "305004": "Islampur",
        "305005": "Madarganj",
        "305006": "Melandaha",
        "305007": "Sarishabari",
        "306": "KISHOREGANJ DISTRICT",
        "306001": "Kishoreganj",
        "306002": "Austagram",
        "306003": "Bajitpur",
        "306004": "Bhairab",
        "306005": "Hossainpur",
        "306006": "Itna",
        "306007": "Karimganj",
        "306008": "Katiadi",
        "306009": "Kuliarchar",
        "306010": "Mithamain",
        "306011": "Nikli",
        "306012": "Pakundia",
        "306013": "Tarail",
        "307": "MADARIPUR DISTRICT",
        "307001": "Madaripur",
        "307002": "Rajoir",
        "307003": "Kalkini",
        "307004": "Shibchar",
        "308": "MANIKGANJ DISTRICT",
        "308001": "Manikgonj",
        "308002": "Daulatpur",
        "308003": "Ghior",
        "308004": "Harirampur",
        "308005": "Saturia",
        "308006": "Shivalaya",
        "308007": "Singair",
        "309": "MUNSHIGANJ DISTRICT",
        "309001": "Munshiganj",
        "309002": "Gazaria",
        "309003": "Lohajang",
        "309004": "Sirajdikhan",
        "309005": "Sreenagar",
        "309006": "Tongibari",
        "310": "MYMENSINGH DISTRICT",
        "310001": "Mymensingh",
        "310002": "Bhaluka",
        "310003": "Dhobaura",
        "310004": "Fulbaria",
        "310005": "Gaffargaon",
        "310006": "Gauripur",
        "310007": "Haluaghat",
        "310008": "Ishwarganj",
        "310009": "Muktagachha",
        "310010": "Nandail",
        "310011": "Phulpur",
        "310012": "Trishal",
        "310013": "Tara Khanda",
        "311": "NARAYANGANJ DISTRICT",
        "311001": "Narayanganj",
        "311002": "Araihazar",
        "311003": "Bandar",
        "311004": "Rupganj",
        "311005": "Sonargaon",
        "312": "NARSINGDI DISTRICT",
        "312001": "Narsingdi",
        "312002": "Belabo",
        "312003": "Monohardi",
        "312004": "Palash",
        "312005": "Raipura",
        "312006": "Shibpur",
        "313": "NETROKONA DISTRICT",
        "313001": "Netrokona",
        "313002": "Atpara",
        "313003": "Barhatta",
        "313004": "Durgapur",
        "313005": "Khaliajuri",
        "313006": "Kalmakanda",
        "313007": "Kendua",
        "313008": "Madan",
        "313009": "Mohanganj",
        "313010": "Purbadhala",
        "314": "RAJBARI DISTRICT",
        "314001": "Rajbari",
        "314002": "Baliakandi",
        "314003": "Goalandaghat",
        "314004": "Pangsha",
        "314005": "Kalukhali",
        "315": "SHARIATPUR DISTRICT",
        "315001": "Shariatpur",
        "315002": "Bhedarganj",
        "315003": "Damudya",
        "315004": "Gosairhat",
        "315005": "Naria",
        "315006": "Zajira",
        "315007": "Shakhipur",
        "316": "SHERPUR DISTRICT",
        "316001": "Sherpur",
        "316002": "Jhenaigati",
        "316003": "Nakla",
        "316004": "Nalitabari",
        "316005": "Sreebardi",
        "317": "TANGAIL DISTRICT",
        "317001": "Tangail",
        "317002": "Gopalpur",
        "317003": "Basail",
        "317004": "Bhuapur",
        "317005": "Delduar",
        "317006": "Ghatail",
        "317007": "Kalihati",
        "317008": "Madhupur",
        "317009": "Mirzapur",
        "317010": "Nagarpur",
        "317011": "Sakhipur",
        "317012": "Dhanbari",
        "400": "KHULNA DIVISION",
        "401": "BAGERHAT DISTRICT",
        "401001": "Bagerhat",
        "401002": "Chitalmari",
        "401003": "Fakirhat",
        "401004": "Kachua",
        "401005": "Mollahat",
        "401006": "Mongla",
        "401007": "Morrelganj",
        "401008": "Rampal",
        "401009": "Sarankhola",
        "402": "CHUADANGA DISTRICT",
        "402001": "Chuadanga",
        "402002": "Alamdanga",
        "402003": "Damurhuda",
        "402004": "Jibannagar",
        "403": "JESSORE DISTRICT",
        "403001": "Jessore",
        "403002": "Abhaynagar",
        "403003": "Bagherpara",
        "403004": "Chaugachha",
        "403005": "Jhikargachha",
        "403006": "Keshabpur",
        "403007": "Manirampur",
        "403008": "Sharsha",
        "404": "JHENAIDA DISTRICT",
        "404001": "Jhenaidah",
        "404002": "Harinakunda",
        "404003": "Kaliganj",
        "404004": "Kotchandpur",
        "404005": "Maheshpur",
        "404006": "Shailkupa",
        "405": "KHULNA DISTRICT",
        "405001": "Khulna City/Kotwali Thana",
        "405002": "Batiaghata",
        "405003": "Dacope",
        "405004": "Dumuria",
        "405005": "Dighalia",
        "405006": "Koyra",
        "405007": "Paikgachha",
        "405008": "Phultala",
        "405009": "Rupsha",
        "405010": "Terokhada",
        "405011": "Daulatpur Thana",
        "405012": "Khalishpur Thana",
        "405013": "Khan Jahan Ali Thana",
        "401014": "Sonadanga Thana",
        "405015": "Harintana Thana",
        "406": "KUSHTIA DISTRICT",
        "406001": "Kushtia",
        "406002": "Bheramara",
        "406003": "Daulatpur",
        "406004": "Khoksa",
        "406005": "Kumarkhali",
        "406006": "Mirpur",
        "407": "MAGURA DISTRICT",
        "407001": "Magura",
        "407002": "Mohammadpur",
        "407003": "Shalikha",
        "407004": "Sreepur",
        "408": "MEHERPUR DISTRICT",
        "408001": "Meherpur",
        "408002": "Gangni",
        "408003": "Mujibnagar",
        "409": "NARAIL DISTRICT",
        "409001": "Narail",
        "409002": "Kalia",
        "409003": "Lohagara",
        "409004": "Naragati Thana",
        "410": "SATKHIRA DISTRICT",
        "410001": "Satkhira",
        "410002": "Assasuni",
        "410003": "Debhata",
        "410004": "Kalaroa",
        "410005": "Kaliganj",
        "410006": "Shyamnagar",
        "410007": "Tala",
        "500": "RAJSHAHI DIVISION ",
        "501": "BOGRA DISTRICT",
        "501001": "Bogra",
        "501002": "Adamdighi",
        "501003": "Dhunat",
        "501004": "Dhupchanchia",
        "501005": "Gabtali",
        "501006": "Kahaloo",
        "501007": "Nandigram",
        "501008": "Sariakandi",
        "501009": "Shajahanpur",
        "501010": "Sherpur",
        "501011": "Shibganj",
        "501012": "Sonatola",
        "502": "JOYPURHAT DISTRICT",
        "502001": "Joypurhat",
        "502002": "Akkelpur",
        "502003": "Kalai",
        "502004": "Khetlal",
        "502005": "Panchbibi",
        "503": "NAOGAON DISTRICT",
        "503001": "Naogaon",
        "503002": "Atrai",
        "503003": "Badalgachhi",
        "503004": "Manda",
        "503005": "Dhamoirhat",
        "503006": "Mohadevpur",
        "503007": "Niamatpur",
        "503008": "Patnitala",
        "503009": "Porsha",
        "503010": "Raninagar",
        "503011": "Sapahar",
        "504": "NATORE DISTRICT",
        "504001": "Natore",
        "504002": "Bagatipara",
        "504003": "Baraigram",
        "504004": "Gurudaspur",
        "504005": "Lalpur",
        "504006": "Singra",
        "504007": "Naldanga",
        "505": "NAWABGANJ DISTRICT",
        "505001": "Nawabganj",
        "505002": "Bholahat",
        "505003": "Gomastapur",
        "505004": "Nachole",
        "505005": "Shibganj",
        "506": "PABNA DISTRICT",
        "506001": "Pabna",
        "506002": "Ataikula",
        "506003": "Atgharia",
        "506004": "Bera",
        "506005": "Bhangura",
        "506006": "Chatmohar",
        "506007": "Faridpur",
        "506008": "Ishwardi",
        "506009": "Santhia",
        "506010": "Sujanagar",
        "507": "RAJSHAHI DISTRICT",
        "507001": "Rajshahi City",
        "507002": "Bagha",
        "507003": "Bagmara",
        "507004": "Charghat",
        "507005": "Durgapur",
        "507006": "Godagari",
        "507007": "Mohanpur",
        "507008": "Paba",
        "507009": "Puthia",
        "507010": "Tanore",
        "508": "SIRAJGANJ DISTRICT",
        "508001": "Sirajganj",
        "508002": "Belkuchi",
        "508003": "Chauhali",
        "508004": "Kamarkhanda",
        "508005": "Kazipur",
        "508006": "Raiganj",
        "508007": "Shahjadpur",
        "508008": "Tarash",
        "508009": "Ullahpara",
        "600": "RANGPUR DIVISION",
        "601": "DINAJPUR DISTRICt",
        "601001": "Dinajpur",
        "601002": "Birampur",
        "601003": "Birganj",
        "601004": "Biral",
        "601005": "Bochaganj",
        "601006": "Chirirbandar",
        "601007": "Phulbari",
        "601008": "Ghoraghat",
        "601009": "Hakimpur",
        "601010": "Kaharole",
        "601011": "Khansama",
        "601012": "Nawabganj",
        "601013": "Parbatipur",
        "602": "GAIBANDHA DISTRICT",
        "602001": "Gaibandha",
        "602002": "Phulchhari",
        "602003": "Gobindaganj",
        "602004": "Palashbari",
        "602005": "Sadullapur",
        "602006": "Sughatta",
        "602007": "Sundarganj",
        "603": "KURIGRAM DISTRICT",
        "603001": "Kurigram",
        "603002": "Bhurungamari",
        "603003": "Char Rajibpur ",
        "603004": "Chilmari",
        "603005": "Phulbari",
        "603006": "Nageshwari",
        "603007": "Rajarhat",
        "603008": "Raomari",
        "603009": "Ulipur",
        "604": "LALMONIRHAT DISTRICT",
        "604001": "Lalmonirhat",
        "604002": "Aditmari",
        "604003": "Hatibandha",
        "604004": "Kaliganj",
        "604005": "Patgram",
        "605": "NILPHAMARI DISTRICT",
        "605001": "Nilphamari",
        "605002": "Dimla",
        "605003": "Domar",
        "605004": "Jaldhaka",
        "605005": "Kishoreganj",
        "605006": "Saidpur",
        "606": "PANCHAGARH DISTRICT",
        "606001": "Panchagarh",
        "606002": "Atwari",
        "606003": "Boda",
        "606004": "Debiganj",
        "606005": "Tetulia",
        "607": "RANGPUR DISTRICT",
        "607001": "Rangpur",
        "607002": "Badarganj",
        "607003": "Gangachhara",
        "607004": "Kaunia",
        "607005": "Mithapukur",
        "607006": "Pirgachha",
        "607007": "Pirganj",
        "607008": "Taraganj",
        "608": "THAKURGAON DISTRICT",
        "608001": "Thakurgaon",
        "608002": "Baliadangi",
        "608003": "Haripur",
        "608004": "Pirganj",
        "608005": "Ranisankail",
        "701": "HABIGANJ DISTRICT",
        "701001": "Habiganj",
        "701002": "Ajmiriganj",
        "701003": "Bahubal",
        "701004": "Baniachong",
        "701005": "Chunarughat",
        "701006": "Lakhai",
        "701007": "Madhabpur",
        "701008": "Nabiganj",
        "702": "MOULVIBAZAR DISTRICT",
        "702001": "Moulvibazar",
        "702002": "Barlekha",
        "702003": "Kamalganj",
        "702004": "Kulaura",
        "702005": "Rajnagar",
        "702006": "Sreemangal",
        "702007": "Juri",
        "703": "SUNAMGANJ DISTRICT",
        "703001": "Sunamganj",
        "703002": "Bishwamvarpur",
        "703003": "Chhatak",
        "703004": "Derai",
        "703005": "Dharamapasha",
        "703006": "Dowarabazar",
        "703007": "Jagannathpur",
        "703008": "Jamalganj",
        "703009": "Sullah",
        "703010": "Tahirpur",
        "703011": "Dakshin Sunamganj",
        "704": "SYLHET DISTRICT",
        "704001": "Sylhet",
        "704002": "Balaganj",
        "704003": "Beanibazar",
        "704004": "Bishwanath",
        "704005": "Companigonj",
        "704006": "Fenchuganj",
        "704007": "Golapganj",
        "704008": "Gowainghat",
        "704009": "Jaintiapur",
        "704010": "Kanaighat",
        "704011": "Zakiganj",
        "704012": "South Surma",
        "704013": "Osmani Nagar"
    }
    for filename in os.listdir(dir_path + '/data/'):
        print filename
        json_obj = None
        if (filename.endswith(".json")):
            with open(dir_path + '/data/' + filename, 'rb') as jsonfile:
                json_obj = json.load(jsonfile)

        for elem in json_obj:
            new_json = {}
            v_day = None
            v_month = None
            v_year = None
            new_json['violence_actor'] = []
            new_json['violence_type'] = []
            new_json['responders'] = []
            new_json['property_destroyed_type'] = []
            new_json['injuries_count'] = 0
            new_json['deaths_count'] = 0
            new_json['property_destroyed_count'] = 0
            for key in elem:
                if key in json_structure:
                    if key == 'VSOUR':
                        new_json[json_structure[key]] = violence_source[str(elem[key])]
                    elif key == 'NDPRO1' or key == 'NDPRO2' or key == 'NDPRO3':
                        if elem[key] == '' or elem[key] == 'Imprecise' or elem[key] == 'imprecise' or elem[key] == None:
                            pass
                        else:
                            new_json['property_destroyed_count'] += int(elem[key])
                    elif key == 'CAviolence_type_1SACA' or key == 'CASACB':
                        if elem[key] == '' or elem[key] == 'Imprecise' or elem[key] == 'imprecise' or elem[key] == None:
                            new_json[json_structure[key]] = 0

                        else:
                            new_json[json_structure[key]] = float(elem[key])
                    elif key == 'VTYP1':
                        if elem[key] == "311" or elem[key] == 311 :
                            new_json[json_structure[key]] = violence_type["310"]
                        elif elem[key] == 207:
                            new_json[json_structure[key]] = violence_type['217']
                        elif elem[key] == 602:
                            new_json[json_structure[key]] = violence_type['320']
                        elif elem[key] == 702:
                            new_json[json_structure[key]] = violence_type['320']
                        elif elem[key] == 704:
                            new_json[json_structure[key]] = violence_type['320']
                        elif elem[key] == 810:
                            new_json[json_structure[key]] = violence_type['210']
                        elif elem[key] == 121:
                            new_json[json_structure[key]] = violence_type['211']
                        elif elem[key] == None:
                            new_json[json_structure[key]] = None
                        else:
                            new_json['violence_type'].append(violence_type[str(elem[key])])
                    elif key == 'VTYP2':
                        if elem[key] == "311"  or elem[key] == 311:
                            new_json['violence_type'].append(violence_type["310"])
                        elif elem[key] == '321':
                            new_json['violence_type'].append(violence_type["320"])
                        elif elem[key] == '140':
                            new_json['violence_type'].append(violence_type["410"])
                        elif elem[key] == 301:
                            new_json['violence_type'].append(violence_type["310"])
                        elif elem[key] == '' or elem[key]== None:
                            pass
                        else:
                            new_json['violence_type'].append(violence_type[str(elem[key])])
                    elif key == 'VTYP3':
                        if elem[key] == '' or elem[key] == None:
                            pass
                        else:
                            new_json['violence_type'].append(violence_type[str(elem[key])])
                    elif key == "VTRIG1" or key == "VTRIG2":
                        if elem[key] == '240':
                            new_json[json_structure[key]] = violence_trigger_1[re.sub("\D", "", str("230"))]
                        elif elem[key] == "111" or elem[key] == 111:
                            new_json[json_structure[key]] = violence_trigger_1[re.sub("\D", "", str("110"))]
                        elif elem[key] == "199":
                            new_json[json_structure[key]] = violence_trigger_1[re.sub("\D", "", str("190"))]
                        elif elem[key] == None or elem[key] == "" or elem[key] == 995:
                            new_json[json_structure[key]] = "Unknown/Unidentified"
                        else:
                            new_json[json_structure[key]] = violence_trigger_1[re.sub("\D", "", str(elem[key]))]
                    elif key == "LDIS":
                        if re.sub("\D", "", str(elem[key])) == "417":
                            new_json[json_structure[key]] = event_location_district["317"]
                        elif re.sub("\D", "", str(elem[key])) == '30':
                            new_json[json_structure[key]] = event_location_district["301"]
                        else:
                            new_json[json_structure[key]] = event_location_district[re.sub("\D", "", str(elem[key]))]
                    elif key == "VTRIGC":
                        if re.sub("\D", "", str(elem[key])) == "1":
                            new_json[json_structure[key]] = "Yes"
                        else:
                            new_json[json_structure[key]] = "No"
                    elif key == "VACTA1" or key == "VACTA2" or key == "VACTA3" or key == "VACTB1" or key == "VACTB2" or key == "VACTB3":
                        if elem[key] == None or elem[key] == '' or elem[key] == 790 :
                            pass
                        elif elem[key] == '32':
                            new_json['violence_actor'].append(violence_actor_1['329'])
                        elif elem[key] == '299':
                            new_json['violence_actor'].append(violence_actor_1['219'])
                        else:
                            new_json['violence_actor'].append(violence_actor_1[re.sub("\D", "", str(elem[key]))])
                    elif key == "VNUM":
                        new_json[json_structure[key]] = int(elem[key])
                    elif key == "VPOL":
                        if elem[key] == None or elem[key] == 1000:
                            new_json[json_structure[key]] = violence_police_role['100']
                        else:
                            new_json[json_structure[key]] = violence_police_role[str(elem[key])]
                    elif key == "DPROP1":
                        if elem[key] == None:
                            pass
                        elif  elem[key] == 770:
                            new_json[json_structure[str(key)]] = destruction_of_property['710']
                            new_json['property_destroyed_type'].append(destruction_of_property['710'])
                        elif elem[key] == 8500:
                            new_json[json_structure[str(key)]] = destruction_of_property['850']
                            new_json['property_destroyed_type'].append(destruction_of_property['850'])
                        else:
                            new_json[json_structure[str(key)]] = destruction_of_property[str(elem[key])]
                            new_json['property_destroyed_type'].append(destruction_of_property[str(elem[key])])
                    elif key == "DPROP2":
                        if elem[key] == None or elem[key] == 1:
                            pass
                        elif elem[key] == '8401':
                            new_json['property_destroyed_type'].append(destruction_of_property['840'])
                        else:
                            new_json['property_destroyed_type'].append(destruction_of_property[str(elem[key])])
                    elif key == "DPROP3":
                        if elem[key] == None or elem[key] == 3:
                            pass
                        elif elem[key] == '8401' or elem[key] == '1':
                            new_json[json_structure[key]] = destruction_of_property['100']
                            new_json['property_destroyed_type'].append(destruction_of_property['100'])
                        else:
                            new_json[json_structure[key]] = destruction_of_property[str(elem[key])]
                            new_json['property_destroyed_type'].append(destruction_of_property[str(elem[key])])
                    elif key == "VTAR1" or key == "VTAR2" or key == "VTAR3":
                        if elem[key] == '' or elem[key] == None or elem[key] == '188:supporters of union parishad chairman':
                            new_json[json_structure[key]] = None
                        elif elem[key] == '210*' :
                            new_json['responders'].append(violence_actor_1['210'])
                        else:
                            new_json['responders'].append(violence_actor_1[str(elem[key])])
                    elif key == 'WOUACA' or key == 'WOUACB' or key == 'WOUTAR'  or key == 'WNONP':
                        if elem[key] == '' or elem[key]==None or elem[key] == 'imprecise' or elem[key] == 'Imprecise':
                            new_json['injuries_count'] += float(0)
                        else:
                            try:
                                new_json['injuries_count'] += float(elem[key])
                            except:
                                new_json['injuries_count'] += float(0)
                    elif key == 'CASACA' or key == 'CASACB':
                        if elem[key] == '' or elem[key] == None:
                            new_json['deaths_count'] += float(0)
                        elif elem[key] == 'imprecise':
                            new_json['deaths_count'] += float(0)
                        else:
                            new_json['deaths_count'] += float(elem[key])
                    elif key == 'CASTAR' or key == 'CNONP':
                        if elem[key] == '' or elem[key] == ' ' or elem[key] == '`' or elem[key] == None:
                            new_json['deaths_count'] += float(0)
                        elif elem[key] == 'imprecise':
                            new_json['deaths_count'] += float(0)
                        else:
                            new_json['deaths_count'] += float(elem[key])
                    elif key == 'VNUM':
                        if elem[key] == '':
                            new_json[json_structure[key]] = 0
                        else:
                            new_json[json_structure[key]] = int(elem[key])
                    elif key == 'LUPC':
                        if elem[key] == '':
                            new_json[json_structure[key]] = ""
                        elif elem[key] == '800001' or elem[key] == '30100':
                            new_json[json_structure[key]] = "multiple"
                        elif elem[key] == '508012' or elem[key] =='508010' or elem[key] =='508011':
                            new_json[json_structure[key]] = upazila['508002']
                        else:
                            new_json[json_structure[key]] = upazila[str(elem[key])]
                    elif key =='VDAY':
                        if key == None:
                            v_day = 1
                            new_json[json_structure[key]] = elem[key]
                        else:
                            v_day = elem['VDAY']
                            new_json[json_structure[key]] = elem[key]
                    elif key == 'VMONT':
                        if key == None or key == '':
                            v_month = 1
                            new_json[json_structure[key]] = elem[key]
                        else:
                            v_month = elem['VMONT']
                            new_json[json_structure[key]] = elem[key]
                    elif key =='VYEAR':
                        if elem['VYEAR'] == '2103' or elem['VYEAR'] == 2103:
                            new_json[json_structure[key]] = 2013
                            v_year = 2013
                        if elem['VYEAR'] == '2104' or elem['VYEAR'] == 2104:
                            new_json[json_structure[key]] = 2014
                            v_year = 2014
                        else:
                            v_year = elem['VYEAR']
                            new_json[json_structure[key]] = elem[key]
                            # print v_year
                    else:
                        new_json[json_structure[key]] = elem[key]

                    if key == "LDIS":
                        division_number = elem["LDIS"]

                        if elem["LDIS"] == '30`':
                            division_number = 300
                        else:
                            division_number = int(division_number)
                        if division_number >= 100 and division_number < 200:
                            new_json['division'] = 'Barisal'
                        elif division_number >= 200 and division_number < 300:
                            new_json['division'] = 'Chittagong'
                        elif division_number >= 300 and division_number < 400:
                            new_json['division'] = 'Dhaka'
                        elif division_number >= 400 and division_number < 500:
                            new_json['division'] = 'Khulna'
                        elif division_number >= 500 and division_number < 600:
                            new_json['division'] = 'Rajshahi'
                        elif division_number >= 600 and division_number  < 700:
                            new_json['division'] = 'Rangpur'
                        elif division_number >= 700 and division_number < 800:
                            new_json['division'] = 'Sylhet'
                        elif division_number == 800:
                            new_json['division'] = 'Multiple'
            if v_day and v_month and v_year:
                try:
                    datetime_object = datetime.strptime(str(v_day)+' '+str(v_month)+' '+str(v_year), '%d %m %Y')
                    new_json['incident_date'] = datetime_object
                except:
                    pass
            new_json['state'] = 'Bangladesh'
            collection.insert(new_json)

    print "Importing finished"


parse()
