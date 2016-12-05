# -*- coding: UTF-8 -*-
import csv
import os
import re

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
        "comment": "comment",
        "ARRACB": "TotalNumberofArrestedReportedActorB",
        "DPROP3": "Destructionofproperty3",
        "NCODE": "Nameofcoder",
        "VTAGC": "Violenteventtagcontinuation",
        "Comment_2": "Comment_2",
        "Comment_3": "Comment_3",
        "LUPC": "EventLocationUpazilla/Pourashava/City",
        "NDPRO1_1": "Numberofpropertydestroyed1",
        "WOUACA": "TotalNumberofWoundedReportedActorA",
        "WNONP": "Woundednon-participant",
        "VNUM": "ViolenceNumber",
        "VREF": "ViolenceReference",
        "VACTB2": "ViolenceActor#2",
        "VACTB3": "ViolenceActor#3",
        "VTAGM": "Violenteventtagmultiple",
        "VACTB1": "ViolenceActor#2",
        "VDAY": "ViolenceDay",
        "VTPRE": "ViolentEventTimePrecision",
        "WOUACB": "TotalNumberofWoundedReportedActorB",
        "CommentVACT": "CommentVACT",
        "VCONT": "Violenteventcontinuation",
        "VTRIG2": "VTRIG2",
        "RDATE": "ReportDate",
        "Comment_1": "Comment_1",
        "VNONP": "Violencenon-participants",
        "VTYP2": "ViolenceType2",
        "VTAGT": "Violenteventtagtrigger",
        "Comment_4": "Comment_4",
        "VTRIGC": "ConflictingTriggerofviolence",
        "LUNW": "EventLocationUnion/Ward/Village/area",
        "VYEAR": "ViolenceYear",
        "AAVER": "ArrestedAveraged",
        "VTAR2": "ViolenceTargetGroup2",
        "VTYP1": "ViolenceType1",
        "WOUTAR": "TotalNumberofWoundedReportedTarget",
        "ARRTAR": "TotalNumberofArrestedReportedTarget",
        "VPOL": "ViolencePoliceRole",
        "CASTAR": "TotalNumberofCasualtiesReportedTarget",
        "ANONP": "Arrestednon-participant",
        "VTRIG1": "TriggerofViolence",
        "CAVER": "CasualtiesAveraged",
        "NDPRO1": "Numberofpropertydestroyed1",
        "VACTA2": "ViolenceActor2",
        "Comment": "Comment",
        "DPROP2": "Destructionofproperty2",
        "DPROP1": "Destructionofproperty1",
        "NDPRO3": "Numberofpropertydestroyed3",
        "VTAR1": "ViolenceTargetGroup",
        "VREMU": "ViolenceReportMultipleEvents",
        "VTAR3": "ViolenceTargetGroup3",
        "VACTA3": "ViolenceActor3",
        "Comment_1": "Comment_1",
        "VACTA1": "ViolenceActor",
        "Comment_3": "Comment_3",
        "LDIS": "EventLocationDistrict",
        "CASACB": "TotalNumberofCasualtiesReportedActorB",
        "CASACA": "TotalNumberofCasualtiesReportedActorA",
        "ARRACA": "TotalNumberofArrestedReportedActorA",
        "VSOUR": "ViolenceSource",
        "VTYP3": "ViolenceType3",
        "WAVER": "WoundedAveraged",
        "VMONT": "ViolenceMonth",
        "VHART": "ViolentEventHartal",
        "Comment_2": "Comment_2",
        "CNONP": "Casualtiesnon-participant"
    }
    violence_source = {
        "1": "Daily Star",
        "2": "Prothom Alu",
        "3": "Ittefaq",
        "4": "Inqilab",
        "5": "Manab Zamin"
    }
    violence_type_1 = {
        "0": "Unspecified",
        "000": "Unspecified",
        "100": "Battle/Clashes",
        "110": "Armed battle/clashes",
        "111": "Battle/clash with the use of arms",
        "112": "The arms used are not specified",
        "113": "Armed battle/clashes (throwing of projectiles)",
        "114": "Armed battle/clashes (knives)",
        "115": "Armed battle/clashes (tear gas)",
        "116": "Armed battle/clashes (rubber bullets)",
        "117": "Armed battle/clashes (rubber bullets)",
        "120": "Unarmed battle/clashes (fists)",
        "200": "Attack",
        "210": "Armed Attack",
        "211": "Armed Attack (guns, pistols)",
        "212": "Armed Attack (baton, stick, lathi, blunt weapons)",
        "213": "Armed Attack (throwing of projectiles)",
        "214": "Armed Attack (knives, sharp weapons)",
        "215": "Armed Attack (tear gas)",
        "216": "Armed battle/clashes (rubber bullets)",
        "217": "Armed battle/clashes (Water cannon)",
        "220": "Unarmed Attack (fists)",
        "300": "Destruction of property",
        "310": "No Arson",
        "320": "Arson",
        "400": "Bombing",
        "410": "Bombing (high impact)",
        "420": "Bombing (low impact)",
        "500": "Rape",
        "600": "Kidnapping, abduction",
        "700": "Hostage taking",
        "999": "Other*"
    }
    violence_trigger_1 = {
        "0": "Unspecified",
        "100": "Political",
        "110": "Election",
        "120": "Peace Process",
        "130": "Clash",
        "140": "Attack",
        "150": "Procession/demonstration",
        "160": "Hartal",
        "170": "Meeting",
        "180": "Assassination",
        "190": "Other*",
        "200": "Socio-Economic",
        "210": "Price Hike",
        "220": "Strike",
        "230": "Labour recruitment",
        "290": "Other*",
        "300": "Religious",
        "310": "Religious festival",
        "320": "Religious gathering",
        "390": "Other*",
        "400": "Judicial",
        "410": "Trial",
        "411": "Verdict",
        "420": "Arrest",
        "430": "Passing of new law",
        "490": "Other*",
        "500": "Remembrance",
        "510": "Independence",
        "520": "Language movement",
        "530": "Other National event",
        "540": "Death of leader",
        "590": "Other*",
        "600": "Access to Resource",
        "610": "Tender",
        "611": "Tender for public purpose",
        "612": "Tender for private purpose",
        "619": "Other*",
        "620": "Immoveable Property",
        "621": "Land",
        "622": "House",
        "623": "Farm",
        "624": "Factory",
        "629": "Other*",
        "630": "Moveable property",
        "631": "car",
        "632": "bike",
        "633": "boat",
        "634": "bus",
        "635": "Other vehicle*",
        "636": "farming equipment",
        "637": "industrial equipment",
        "638": "Money/cash",
        "639": "Other*",
        "699": "Other*",
        "700": "Position/job",
        "710": "Within organization",
        "720": "In public sector",
        "730": "In private sector",
        "799": "Other*",
        "800": "Organisational dynamics",
        "810": "Area Domination/Supremacy",
        "820": "Committee formation",
        "890": "Internal feud (non-specified)",
        "998": "Unknown",
        "999": "Other*"
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
        "100": "State Actor",
        "110": "Law enforcement agencies",
        "111": "Police",
        "112": "Ansar",
        "113": "Rapid Action Battalion (RAB)",
        "114": "Range Reserve Force (RRF)",
        "115": "Special Armed Force (SAF)",
        "118": "Other*",
        "120": "Paramilitary",
        "121": "Border Guards Bangladesh",
        "128": "Other*",
        "130": "Military",
        "140": "Administration",
        "141": "Union/ward level",
        "142": "Upazilla level",
        "143": "District level",
        "144": "National level",
        "188": "Other*",
        "200": "Political Party",
        "210": "Awami League (AL)",
        "211": "Local Leader (Unspecified)",
        "212": "Local Leader (Union/ward/ Upazilla/Pourahava)",
        "213": "Local Leader (district/city)",
        "214": "National Leader (Unspecified)",
        "215": "Elected representative (national)",
        "216": "Former elected representative (national)",
        "217": "Member of Central Committee",
        "218": "Leader (Unspecified)",
        "219": "Activist",
        "220": "Bangladesh Nationalist Party (BNP)",
        "221": "Local Leader (Unspecified)",
        "222": "Local Leader (Union/ward/ Upazilla/Pourahava)",
        "223": "Local Leader (district/city)",
        "224": "National Leader (Unspecified)",
        "225": "Elected representative (national)",
        "226": "Former elected representative (national)",
        "227": "Member of Central Committee",
        "228": "Leader (Unspecified)",
        "229": "Activist",
        "230": "Jamaat-e-Islami (JI)",
        "231": "Local Leader (Unspecified)",
        "232": "Local Leader (Union/ward/ Upazilla/Pourahava)",
        "233": "Local Leader (district/city)",
        "234": "National Leader (Unspecified)",
        "235": "Elected representative (national)",
        "236": "Former elected representative (national)",
        "237": "Member of Central Committee",
        "238": "Leader (Unspecified)",
        "239": "Activist",
        "240": "Jatiya Party",
        "241": "Local Leader (Unspecified)",
        "242": "Local Leader (Union/ward/ Upazilla/Pourahava)",
        "243": "Local Leader (district/city)",
        "244": "National Leader (Unspecified)",
        "245": "Elected representative (national)",
        "246": "Former elected representative (national)",
        "247": "Member of Central Committee",
        "248": "Leader (Unspecified)",
        "249": "Activist",
        "250": "Left-Wing Parties",
        "251": "Communist Party of Bangladesh*",
        "252": "Socialist Party of Bangladesh*",
        "253": "Jatiyo Samajtantrik Dal (JSD)*",
        "254": "Worker’s Party of Bangladesh (WPB) *",
        "259": "Other left-wing party*",
        "260": "Islamist Parties",
        "261": "Bangladesh Khelafat Andolan",
        "262": "Islami Oikya Jote",
        "263": "Bangladesh Khelafat Majlish",
        "269": "Other Islamist Party*",
        "270": "Parbattya Chhattagram Jana Samhati Samiti (PCJSS)",
        "288": "Other*",
        "300": "Student Group",
        "310": "Bangladesh Chattro League",
        "311": "Local Leader (Unspecified)",
        "312": "Hall committee member",
        "313": "Hall Committee member (president/general secretary)",
        "314": "University/college committee member",
        "315": "University/college committee member (president/general secretary)",
        "316": "National Leader (Unspecified)",
        "317": "Member of Central committee",
        "318": "Member of Central committee (president/general secretary)",
        "319": "Activist",
        "320": "Jatiyatabadi Chhattro Dal",
        "321": "Local Leader (Unspecified)",
        "322": "Hall committee member",
        "323": "Hall Committee member (president/general secretary)",
        "324": "University/college committee member",
        "325": "University/college committee member (president/general secretary)",
        "326": "National Leader (Unspecified)",
        "327": "Member of Central committee",
        "328": "Member of Central committee (president/general secretary)",
        "329": "Activist",
        "330": "Islami Chattro Shibir",
        "331": "Local Leader (Unspecified)",
        "332": "Hall committee member",
        "333": "Hall Committee member (president/generalsecretary)",
        "334": "University/college committee member",
        "335": "University/college committee member (president/general secretary)",
        "336": "National Leader (Unspecified)",
        "337": "Member of Central committee",
        "338": "Member of Central committee (president/general secretary)",
        "339": "Activist",
        "340": "Jatiyo Chattro Samaj",
        "341": "Local Leader (Unspecified)",
        "342": "Hall committee member",
        "343": "Hall Committee member (president/general secretary)",
        "344": "University/college committee member",
        "345": "University/college committee member (president/general secretary)",
        "346": "National Leader (Unspecified)",
        "347": "Member of Central committee",
        "348": "Member of Central committee (president/general secretary)",
        "349": "Activist",
        "350": "Left-Wing Student Group",
        "351": "Chattro Union",
        "352": "Chattro Moitree",
        "353": "Chattro Federation",
        "358": "Other left-wing student group*",
        "360": "Islamist Student Group*",
        "388": "Other*",
        "400": "Youth (Jubo) Group",
        "410": "Jubo League",
        "411": "Local Leader (Unspecified)",
        "412": "Local Leader (Union/ward/ Upazilla/Pourahava)",
        "414": "Local Leader (district/ city)",
        "415": "National Leader (Unspecified)",
        "416": "Member of Central Committee",
        "417": "Leader (Unspecified)",
        "419": "Activist",
        "420": "Jubo Dal",
        "421": "Local Leader (Unspecified)",
        "422": "Local Leader (Union/ward/ Upazilla/Pourahava)",
        "424": "Local Leader (district/ city)",
        "425": "National Leader (Unspecified)",
        "426": "Member of Central Committee",
        "427": "Leader (Unspecified)",
        "429": "Activist",
        "430": "JI Jubo group",
        "431": "Local Leader (Unspecified)",
        "432": "Local Leader (Union/ward/ Upazilla/Pourahava)",
        "434": "Local Leader (district/ city)",
        "435": "National Leader (Unspecified)",
        "436": "Member of Central Committee",
        "437": "Leader (Unspecified)",
        "439": "Activist",
        "440": "Jatiya Juba Sanghati",
        "441": "Local Leader (Unspecified)",
        "442": "Local Leader (Union/ward/ Upazilla/Pourahava)",
        "444": "Local Leader (district/ city)",
        "445": "National Leader (Unspecified)",
        "446": "Member of Central Committee",
        "447": "Leader (Unspecified)",
        "449": "Activist",
        "450": "Left Wing Youth Groups*",
        "451": "Organizer (unspecified)",
        "452": "Local Leader (Unspecified)",
        "453": "National Leader (Unspecified)",
        "454": "Member of Central committee",
        "455": "Activist",
        "460": "Islamist Youth Groups*",
        "461": "Organizer (unspecified)",
        "462": "Local Leader (Unspecified)",
        "463": "National Leader (Unspecified)",
        "464": "Member of Central committee",
        "465": "Activist",
        "488": "Other*",
        "500": "Islamist Group",
        "510": "Jama'at-ul-Mujahideen Bangladesh",
        "520": "Hizb-ut-Tahrir",
        "530": "Hizb-ut-Towhid",
        "540": "Harkat-ul-Jihad-al Islami Bangladesh (HuJI-B)",
        "550": "Jagrata Muslim Janata Bangladesh (JMJB)",
        "560": "Hefajat-i-Islam",
        "588": "Other*",
        "600": "Alliance of actors",
        "610": "Awami League Centred Alliance",
        "611": "Multiple AL organizations (e.g. AL, BCL, BJL)",
        "612": "Multiple AL alliance organizations (AL, Grand alliance organizations)",
        "620": "Bangladesh Nationalist Party centered alliance",
        "621": "Multiple BNP organizations (e.g. BNP, BCD, BJD)",
        "622": "Multiple BNP alliance organizations (e.g. BNP, fourparty alliance)",
        "630": "Jamaat-e-Islami centered alliance",
        "631": "Multiple JI organizations (JI, ICS)",
        "632": "Multiple JI allied organizations (JI + other Islamist groups)",
        "640": "Alliance of left-wing parties",
        "650": "Alliance of Islamist Groups (nonJI)",
        "660": "Alliance of rebel groups",
        "661": "Alliance of CHT rebel groups",
        "662": "Alliance of left-wing rebel groups",
        "670": "Alliance of Trade Unions",
        "680": "Alliance of Alliance",
        "699": "Other*",
        "700": "Rebel Group",
        "710": "Purba Bangla Communist Party (PBCP)",
        "720": "United People’s Democratic Front (UPDF)",
        "730": "Shanti Bahini",
        "799": "Other*",
        "800": "Ethnic/religious Minority Groups",
        "810": "Ethnic minority group*",
        "811": "Garo/Mandi",
        "812": "Chakma",
        "813": "Marma",
        "814": "Tripura",
        "815": "Tanchangyas",
        "816": "Chak",
        "817": "Other CHT group*",
        "819": "Other*",
        "820": "Ethnic minority organization*",
        "830": "Religious minority group",
        "831": "Hindu",
        "832": "Buddhist",
        "833": "Christian",
        "839": "Other*",
        "840": "Religious minority organization*",
        "900": "Occupational group/organisation",
        "910": "Workers (non-organised)",
        "920": "Trade Union",
        "921": "Bangladesh Jatio Sramik League",
        "922": "Bangladesh Jatiyatabadi Sramik Dal",
        "923": "Bangladesh Jatiyo Sarmik Jote",
        "929": "Other*",
        "930": "Other worker’s organization*",
        "940": "Farmers (non-organised)",
        "950": "Farmer’s organisation",
        "951": "Bangladesh Krishak League",
        "952": "Bangladesh Khetmajur Union",
        "959": "Other*",
        "960": "Combination of workers and peasants",
        "970": "White collar workers",
        "980": "Management",
        "988": "Other*",
        "995": "Unidentified/unknown",
        "996": "Criminal (known)",
        "997": "journalist",
        "998": "Civilian/non-participants*",
        "999": "Other*"
    }
    violence_police_role = {
        "100": "Police not mentioned",
        "200": "Police is participant in the violent event from the start",
        "322": "Police participates in violent event on side of VACTA",
        "300": "Police arrives during the violent event",
        "310": "Police remains inactive during violent event",
        "320": " Police intervenes during the violent event ",
        "321": "Police separates sides in violent event",
        "323": "Police participates in violent event on side of VACTA",
        "400": "Police arrives after the violent event"
    }
    destruction_of_property={
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
    for filename in os.listdir(dir_path + '/data/'):
        print filename
        json_obj = None
        if (filename.endswith(".json")):
            with open(dir_path + '/data/' + filename, 'rb') as jsonfile:
                json_obj = json.load(jsonfile)

        for elem in json_obj:
            new_json = {}
            for key in elem:
                if key in json_structure:
                    if key == 'VSOUR':
                        new_json[json_structure[key]] = violence_source[elem[key]]
                    elif key == 'VTYP1':
                        if elem[key] == "311":
                            new_json[json_structure[key]] = violence_type_1["310"]
                        else:
                            new_json[json_structure[key]] = violence_type_1[elem[key]]
                    elif key == 'VTYP2':
                        if elem[key] == "311":
                            new_json[json_structure[key]] = violence_type_1["310"]
                        elif elem[key] == '321' or elem[key] == '140' or elem[key] == '':
                            #ToDo: Figure out what this number means
                            new_json[json_structure[key]] = None
                        else:
                            new_json[json_structure[key]] = violence_type_1[elem[key]]
                    elif key == 'VTYP3':
                        if elem[key] == '' or elem[key] == None:
                            #ToDo: Figure out what this number means
                            new_json[json_structure[key]] = None
                        else:
                            new_json[json_structure[key]] = violence_type_1[elem[key]]
                    elif key == "VTRIG1" or key == "VTRIG2":
                        if elem[key] == '240':
                            new_json[json_structure[key]] = violence_trigger_1[re.sub("\D", "", str("230"))]
                        elif elem[key] == "111":
                            new_json[json_structure[key]] = violence_trigger_1[re.sub("\D", "", str("110"))]
                        elif elem[key] == "199":
                            new_json[json_structure[key]] = violence_trigger_1[re.sub("\D", "", str("190"))]
                        elif elem[key] == None or elem[key] == "":
                            new_json[json_structure[key]] = None
                        else:
                            new_json[json_structure[key]] = violence_trigger_1[re.sub("\D", "", str(elem[key]))]
                    elif key == "LDIS":
                        if re.sub("\D", "", elem[key]) == "417":
                            new_json[json_structure[key]] = event_location_district["317"]
                        elif re.sub("\D", "", elem[key]) == '30':
                            new_json[json_structure[key]] = event_location_district["301"]
                        else:
                            new_json[json_structure[key]] = event_location_district[re.sub("\D", "", elem[key])]
                    elif key == "VTRIGC":
                        if re.sub("\D", "", str(elem[key])) == "1":
                            new_json[json_structure[key]] = "Yes"
                        else:
                            new_json[json_structure[key]] = "No"
                    elif key == "VACTA1":
                        new_json[json_structure[key]] = violence_actor_1[re.sub("\D", "", elem[key])]
                    elif key == "VNUM":
                        new_json[json_structure[key]] = int(elem[key])
                    elif key == "VPOL":
                        new_json[json_structure[key]] = violence_police_role[str(elem[key])]
                    elif key == "DPROP1":
                        if elem[key] == None:
                            new_json[json_structure[key]] = None
                        else:
                            new_json[json_structure[key]] = destruction_of_property[str(elem[key])]
                    elif key == "DPROP2":
                        if elem[key] == None:
                            new_json[json_structure[key]] = None
                        elif elem[key] == '8401':
                            new_json[json_structure[key]] = destruction_of_property['840']
                        else:
                            new_json[json_structure[key]] = destruction_of_property[str(elem[key])]
                    elif key == "DPROP3":
                        if elem[key] == None:
                            new_json[json_structure[key]] = None
                        elif elem[key] == '8401' or elem[key] == '1':
                            new_json[json_structure[key]] = destruction_of_property['100']
                        else:
                            new_json[json_structure[key]] = destruction_of_property[elem[key]]
                    elif key == "VTAR1" or key == "VTAR2" or key == "VTAR3":
                        if elem[key] == '' or elem[key] == None:
                            new_json[json_structure[key]] = None
                        elif elem[key] == '210*':
                            new_json[json_structure[key]] = violence_actor_1['210']
                        else:
                            new_json[json_structure[key]] = violence_actor_1[elem[key]]
                    elif key == 'WOUACA':
                        if elem[key] == '':
                            new_json[json_structure[key]] = 0
                        elif elem[key] == 'imprecise':
                            new_json[json_structure[key]] = 0
                        else:
                            new_json[json_structure[key]] = float(elem[key])
                    elif key == 'VNUM':
                        if elem[key] == '':
                            new_json[json_structure[key]] = 0
                        else:
                            new_json[json_structure[key]] = int(elem[key])
                    else:
                        new_json[json_structure[key]] = elem[key]
            collection.insert(new_json)

    print "Importing finished"


parse()
