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
collection = db.census

collection.drop()
def parse():
    population = [
        {
            "division": "Barisal",
            "upazila": "Amtali",
            "district": "Barguna",
            "population": 270802
        },
        {
            "division": "Barisal",
            "upazila": "Bamna",
            "district": "Barguna",
            "population": 79564
        },
        {
            "division": "Barisal",
            "upazila": "Barguna",
            "district": "Barguna",
            "population": 261343
        },
        {
            "division": "Barisal",
            "upazila": "Betagi",
            "district": "Barguna",
            "population": 117145
        },
        {
            "division": "Barisal",
            "upazila": "Patharghata",
            "district": "Barguna",
            "population": 163927
        },
        {
            "division": "Barisal",
            "upazila": "Agailjhara",
            "district": "Barisal ",
            "population": 149455
        },
        {
            "division": "Barisal",
            "upazila": "Babuganj",
            "district": "Barisal ",
            "population": 140361
        },
        {
            "division": "Barisal",
            "upazila": "Bakerganj",
            "district": "Barisal ",
            "population": 313845
        },
        {
            "division": "Barisal",
            "upazila": "Banari para",
            "district": "Barisal ",
            "population": 148188
        },
        {
            "division": "Barisal",
            "upazila": "Gaurnadi",
            "district": "Barisal ",
            "population": 188586
        },
        {
            "division": "Barisal",
            "upazila": "Hizla",
            "district": "Barisal ",
            "population": 146077
        },
        {
            "division": "Barisal",
            "upazila": "Barisal",
            "district": "Barisal ",
            "population": 527017
        },
        {
            "division": "Barisal",
            "upazila": "Mhendiganj",
            "district": "Barisal ",
            "population": 301046
        },
        {
            "division": "Barisal",
            "upazila": "Muladi",
            "district": "Barisal ",
            "population": 174775
        },
        {
            "division": "Barisal",
            "upazila": "Wazirpur",
            "district": "Barisal ",
            "population": 234959
        },
        {
            "division": "Barisal",
            "upazila": "Bhola",
            "district": "Bhola",
            "population": 430520
        },
        {
            "division": "Barisal",
            "upazila": "Burhanuddin",
            "district": "Bhola",
            "population": 233860
        },
        {
            "division": "Barisal",
            "upazila": "Char fasson",
            "district": "Bhola",
            "population": 456437
        },
        {
            "division": "Barisal",
            "upazila": "Daulat khan",
            "district": "Bhola",
            "population": 168567
        },
        {
            "division": "Barisal",
            "upazila": "Lalmohan",
            "district": "Bhola",
            "population": 283889
        },
        {
            "division": "Barisal",
            "upazila": "Manpura",
            "district": "Bhola",
            "population": 76582
        },
        {
            "division": "Barisal",
            "upazila": "Tazumuddin",
            "district": "Bhola",
            "population": 126940
        },
        {
            "division": "Barisal",
            "upazila": "Jhalokati",
            "district": "Jhalokati",
            "population": 216357
        },
        {
            "division": "Barisal",
            "upazila": "Kanthalia",
            "district": "Jhalokati",
            "population": 124284
        },
        {
            "division": "Barisal",
            "upazila": "Nalchity",
            "district": "Jhalokati",
            "population": 193525
        },
        {
            "division": "Barisal",
            "upazila": "Rajapur",
            "district": "Jhalokati",
            "population": 148503
        },
        {
            "division": "Barisal",
            "upazila": "Bauphal",
            "district": "Patuakhali ",
            "population": 304284
        },
        {
            "division": "Barisal",
            "upazila": "Dashmina",
            "district": "Patuakhali ",
            "population": 123388
        },
        {
            "division": "Barisal",
            "upazila": "Dumki",
            "district": "Patuakhali ",
            "population": 70655
        },
        {
            "division": "Barisal",
            "upazila": "Galachipa",
            "district": "Patuakhali ",
            "population": 361518
        },
        {
            "division": "Barisal",
            "upazila": "Kalapara",
            "district": "Patuakhali ",
            "population": 237831
        },
        {
            "division": "Barisal",
            "upazila": "Mirzaganj",
            "district": "Patuakhali ",
            "population": 121716
        },
        {
            "division": "Barisal",
            "upazila": "Patuakhali",
            "district": "Patuakhali ",
            "population": 316462
        },
        {
            "division": "Barisal",
            "upazila": "Bhandaria",
            "district": "Pirojpur",
            "population": 148159
        },
        {
            "division": "Barisal",
            "upazila": "Kawkhali",
            "district": "Pirojpur",
            "population": 70130
        },
        {
            "division": "Barisal",
            "upazila": "Mathbaria",
            "district": "Pirojpur",
            "population": 262841
        },
        {
            "division": "Barisal",
            "upazila": "Nazirpur",
            "district": "Pirojpur",
            "population": 180408
        },
        {
            "division": "Barisal",
            "upazila": "Pirojpur",
            "district": "Pirojpur",
            "population": 163470
        },
        {
            "division": "Barisal",
            "upazila": "Nesarabad",
            "district": "Pirojpur",
            "population": 211032
        },
        {
            "division": "Barisal",
            "upazila": "Zianagar",
            "district": "Pirojpur",
            "population": 77217
        },
        {
            "division": "Chittagong",
            "upazila": "Alikadam",
            "district": "Bandarban ",
            "population": 49317
        },
        {
            "division": "Chittagong",
            "upazila": "Bandarban",
            "district": "Bandarban ",
            "population": 88282
        },
        {
            "division": "Chittagong",
            "upazila": "Lama",
            "district": "Bandarban ",
            "population": 108995
        },
        {
            "division": "Chittagong",
            "upazila": "Naikhongchhari",
            "district": "Bandarban ",
            "population": 61788
        },
        {
            "division": "Chittagong",
            "upazila": "Rowangchhari",
            "district": "Bandarban ",
            "population": 27264
        },
        {
            "division": "Chittagong",
            "upazila": "Ruma",
            "district": "Bandarban ",
            "population": 29098
        },
        {
            "division": "Chittagong",
            "upazila": "Thanchi",
            "district": "Bandarban ",
            "population": 23591
        },
        {
            "division": "Chittagong",
            "upazila": "Akhaura",
            "district": "Brahmanbaria",
            "population": 145215
        },
        {
            "division": "Chittagong",
            "upazila": "Banchharampur",
            "district": "Brahmanbaria",
            "population": 298430
        },
        {
            "division": "Chittagong",
            "upazila": "Bijoynagar",
            "district": "Brahmanbaria",
            "population": 257247
        },
        {
            "division": "Chittagong",
            "upazila": "Brahmanbaria",
            "district": "Brahmanbaria",
            "population": 521994
        },
        {
            "division": "Chittagong",
            "upazila": "Ashuganj",
            "district": "Brahmanbaria",
            "population": 180654
        },
        {
            "division": "Chittagong",
            "upazila": "Kasba",
            "district": "Brahmanbaria",
            "population": 319221
        },
        {
            "division": "Chittagong",
            "upazila": "Nabinagar",
            "district": "Brahmanbaria",
            "population": 493518
        },
        {
            "division": "Chittagong",
            "upazila": "Nasirnagar",
            "district": "Brahmanbaria",
            "population": 309011
        },
        {
            "division": "Chittagong",
            "upazila": "Sarail",
            "district": "Brahmanbaria",
            "population": 315208
        },
        {
            "division": "Chittagong",
            "upazila": "Chandpur",
            "district": "Chandpur",
            "population": 465919
        },
        {
            "division": "Chittagong",
            "upazila": "Faridganj",
            "district": "Chandpur",
            "population": 396683
        },
        {
            "division": "Chittagong",
            "upazila": "Haim Char",
            "district": "Chandpur",
            "population": 109575
        },
        {
            "division": "Chittagong",
            "upazila": "Hajiganj",
            "district": "Chandpur",
            "population": 330477
        },
        {
            "division": "Chittagong",
            "upazila": "Kachua",
            "district": "Chandpur",
            "population": 382139
        },
        {
            "division": "Chittagong",
            "upazila": "Matlab dakshin",
            "district": "Chandpur",
            "population": 210050
        },
        {
            "division": "Chittagong",
            "upazila": "Matlab uttar",
            "district": "Chandpur",
            "population": 292057
        },
        {
            "division": "Chittagong",
            "upazila": "Shahrasti",
            "district": "Chandpur",
            "population": 229118
        },
        {
            "division": "Chittagong",
            "upazila": "Anowara",
            "district": "Chittagong",
            "population": 259022
        },
        {
            "division": "Chittagong",
            "upazila": "Bayejid bostami",
            "district": "Chittagong",
            "population": 211355
        },
        {
            "division": "Chittagong",
            "upazila": "Banshkhali",
            "district": "Chittagong",
            "population": 431162
        },
        {
            "division": "Chittagong",
            "upazila": "Bakalia",
            "district": "Chittagong",
            "population": 262703
        },
        {
            "division": "Chittagong",
            "upazila": "Boalkhali",
            "district": "Chittagong",
            "population": 223125
        },
        {
            "division": "Chittagong",
            "upazila": "Chandanaish",
            "district": "Chittagong",
            "population": 233017
        },
        {
            "division": "Chittagong",
            "upazila": "Chandgaon",
            "district": "Chittagong",
            "population": 256411
        },
        {
            "division": "Chittagong",
            "upazila": "Chittagong port",
            "district": "Chittagong",
            "population": 208260
        },
        {
            "division": "Chittagong",
            "upazila": "Double mooring",
            "district": "Chittagong",
            "population": 361154
        },
        {
            "division": "Chittagong",
            "upazila": "Fatikchhari",
            "district": "Chittagong",
            "population": 526003
        },
        {
            "division": "Chittagong",
            "upazila": "Halishahar",
            "district": "Chittagong",
            "population": 151515
        },
        {
            "division": "Chittagong",
            "upazila": "Hathazari",
            "district": "Chittagong",
            "population": 431748
        },
        {
            "division": "Chittagong",
            "upazila": "Kotwali",
            "district": "Chittagong",
            "population": 319972
        },
        {
            "division": "Chittagong",
            "upazila": "Khulshi",
            "district": "Chittagong",
            "population": 278623
        },
        {
            "division": "Chittagong",
            "upazila": "Lohagara",
            "district": "Chittagong",
            "population": 279913
        },
        {
            "division": "Chittagong",
            "upazila": "Mirsharai",
            "district": "Chittagong",
            "population": 398716
        },
        {
            "division": "Chittagong",
            "upazila": "Pahartali",
            "district": "Chittagong",
            "population": 190637
        },
        {
            "division": "Chittagong",
            "upazila": "Panchlaish",
            "district": "Chittagong",
            "population": 219132
        },
        {
            "division": "Chittagong",
            "upazila": "Patiya",
            "district": "Chittagong",
            "population": 528120
        },
        {
            "division": "Chittagong",
            "upazila": "Patenga",
            "district": "Chittagong",
            "population": 132677
        },
        {
            "division": "Chittagong",
            "upazila": "Rangunia",
            "district": "Chittagong",
            "population": 339004
        },
        {
            "division": "Chittagong",
            "upazila": "Raozan",
            "district": "Chittagong",
            "population": 322840
        },
        {
            "division": "Chittagong",
            "upazila": "Sandwip",
            "district": "Chittagong",
            "population": 278605
        },
        {
            "division": "Chittagong",
            "upazila": "Satkania",
            "district": "Chittagong",
            "population": 384806
        },
        {
            "division": "Chittagong",
            "upazila": "Sitakunda",
            "district": "Chittagong",
            "population": 387832
        },
        {
            "division": "Chittagong",
            "upazila": "Barura",
            "district": "Comilla",
            "population": 405118
        },
        {
            "division": "Chittagong",
            "upazila": "Brahman Para",
            "district": "Comilla",
            "population": 204691
        },
        {
            "division": "Chittagong",
            "upazila": "Burichang",
            "district": "Comilla",
            "population": 301825
        },
        {
            "division": "Chittagong",
            "upazila": "Chandina",
            "district": "Comilla",
            "population": 350273
        },
        {
            "division": "Chittagong",
            "upazila": "Chauddagram",
            "district": "Comilla",
            "population": 443648
        },
        {
            "division": "Chittagong",
            "upazila": "Comilla dakshin",
            "district": "Comilla",
            "population": 427391
        },
        {
            "division": "Chittagong",
            "upazila": "Daudkandi",
            "district": "Comilla",
            "population": 349910
        },
        {
            "division": "Chittagong",
            "upazila": "Debidwar",
            "district": "Comilla",
            "population": 431352
        },
        {
            "division": "Chittagong",
            "upazila": "Homna",
            "district": "Comilla",
            "population": 206386
        },
        {
            "division": "Chittagong",
            "upazila": "Comilla Adarsha",
            "district": "Comilla",
            "population": 532419
        },
        {
            "division": "Chittagong",
            "upazila": "Laksam",
            "district": "Comilla",
            "population": 294719
        },
        {
            "division": "Chittagong",
            "upazila": "Manoharganj",
            "district": "Comilla",
            "population": 244943
        },
        {
            "division": "Chittagong",
            "upazila": "Meghna",
            "district": "Comilla",
            "population": 112453
        },
        {
            "division": "Chittagong",
            "upazila": "Muradnagar",
            "district": "Comilla",
            "population": 523556
        },
        {
            "division": "Chittagong",
            "upazila": "Nangalkot",
            "district": "Comilla",
            "population": 373987
        },
        {
            "division": "Chittagong",
            "upazila": "Titas",
            "district": "Comilla",
            "population": 184617
        },
        {
            "division": "Chittagong",
            "upazila": "Chakaria",
            "district": "Cox's bazar",
            "population": 474465
        },
        {
            "division": "Chittagong",
            "upazila": "Cox's bazar",
            "district": "Cox's bazar",
            "population": 459082
        },
        {
            "division": "Chittagong",
            "upazila": "Kutubdia",
            "district": "Cox's bazar",
            "population": 125279
        },
        {
            "division": "Chittagong",
            "upazila": "Maheshkhali",
            "district": "Cox's bazar",
            "population": 321218
        },
        {
            "division": "Chittagong",
            "upazila": "Pekua",
            "district": "Cox's bazar",
            "population": 171538
        },
        {
            "division": "Chittagong",
            "upazila": "Ramu",
            "district": "Cox's bazar",
            "population": 266640
        },
        {
            "division": "Chittagong",
            "upazila": "Teknaf",
            "district": "Cox's bazar",
            "population": 264389
        },
        {
            "division": "Chittagong",
            "upazila": "Ukhia",
            "district": "Cox's bazar",
            "population": 207379
        },
        {
            "division": "Chittagong",
            "upazila": "Chhagalnaiya",
            "district": "Feni",
            "population": 187156
        },
        {
            "division": "Chittagong",
            "upazila": "Daganbhuiyan",
            "district": "Feni",
            "population": 254402
        },
        {
            "division": "Chittagong",
            "upazila": "Feni",
            "district": "Feni",
            "population": 512646
        },
        {
            "division": "Chittagong",
            "upazila": "Fulgazi",
            "district": "Feni",
            "population": 119558
        },
        {
            "division": "Chittagong",
            "upazila": "Parshuram",
            "district": "Feni",
            "population": 101062
        },
        {
            "division": "Chittagong",
            "upazila": "Sonagazi",
            "district": "Feni",
            "population": 262547
        },
        {
            "division": "Chittagong",
            "upazila": "Dighinala",
            "district": "Khagrachhari",
            "population": 103392
        },
        {
            "division": "Chittagong",
            "upazila": "Khagrachhari",
            "district": "Khagrachhari",
            "population": 111833
        },
        {
            "division": "Chittagong",
            "upazila": "Lakshmichhari",
            "district": "Khagrachhari",
            "population": 25994
        },
        {
            "division": "Chittagong",
            "upazila": "Mahalchhari",
            "district": "Khagrachhari",
            "population": 50757
        },
        {
            "division": "Chittagong",
            "upazila": "Manikchhari",
            "district": "Khagrachhari",
            "population": 61589
        },
        {
            "division": "Chittagong",
            "upazila": "Matiranga",
            "district": "Khagrachhari",
            "population": 126477
        },
        {
            "division": "Chittagong",
            "upazila": "Panchhari",
            "district": "Khagrachhari",
            "population": 62198
        },
        {
            "division": "Chittagong",
            "upazila": "Ramgarh",
            "district": "Khagrachhari",
            "population": 71677
        },
        {
            "division": "Chittagong",
            "upazila": "Kamalnagar",
            "district": "Lakshmipur",
            "population": 222915
        },
        {
            "division": "Chittagong",
            "upazila": "Lakshmipur",
            "district": "Lakshmipur",
            "population": 684425
        },
        {
            "division": "Chittagong",
            "upazila": "Roypur",
            "district": "Lakshmipur",
            "population": 275160
        },
        {
            "division": "Chittagong",
            "upazila": "Ramganj",
            "district": "Lakshmipur",
            "population": 285686
        },
        {
            "division": "Chittagong",
            "upazila": "Ramgati",
            "district": "Lakshmipur",
            "population": 261002
        },
        {
            "division": "Chittagong",
            "upazila": "Begumganj",
            "district": "Noakhali ",
            "population": 549308
        },
        {
            "division": "Chittagong",
            "upazila": "Chatkhil",
            "district": "Noakhali ",
            "population": 233253
        },
        {
            "division": "Chittagong",
            "upazila": "Companiganj",
            "district": "Noakhali ",
            "population": 250579
        },
        {
            "division": "Chittagong",
            "upazila": "Hatiya",
            "district": "Noakhali ",
            "population": 452463
        },
        {
            "division": "Chittagong",
            "upazila": "Kabirhat",
            "district": "Noakhali ",
            "population": 196944
        },
        {
            "division": "Chittagong",
            "upazila": "Senbagh",
            "district": "Noakhali ",
            "population": 282894
        },
        {
            "division": "Chittagong",
            "upazila": "Sonaimuri",
            "district": "Noakhali ",
            "population": 327194
        },
        {
            "division": "Chittagong",
            "upazila": "Subarnachar",
            "district": "Noakhali ",
            "population": 289514
        },
        {
            "division": "Chittagong",
            "upazila": "Noakhali",
            "district": "Noakhali ",
            "population": 525934
        },
        {
            "division": "Chittagong",
            "upazila": "Baghaichhari",
            "district": "Rangamati",
            "population": 96899
        },
        {
            "division": "Chittagong",
            "upazila": "Barkal",
            "district": "Rangamati",
            "population": 47523
        },
        {
            "division": "Chittagong",
            "upazila": "Kawkhali (betbunia)",
            "district": "Rangamati",
            "population": 59578
        },
        {
            "division": "Chittagong",
            "upazila": "Belai chhari  upazi",
            "district": "Rangamati",
            "population": 28525
        },
        {
            "division": "Chittagong",
            "upazila": "Kaptai",
            "district": "Rangamati",
            "population": 59693
        },
        {
            "division": "Chittagong",
            "upazila": "Jurai chhari upazil",
            "district": "Rangamati",
            "population": 27786
        },
        {
            "division": "Chittagong",
            "upazila": "Langadu",
            "district": "Rangamati",
            "population": 81548
        },
        {
            "division": "Chittagong",
            "upazila": "Naniarchar",
            "district": "Rangamati",
            "population": 43616
        },
        {
            "division": "Chittagong",
            "upazila": "Rajasthali",
            "district": "Rangamati",
            "population": 26083
        },
        {
            "division": "Chittagong",
            "upazila": "Rangamati  up",
            "district": "Rangamati",
            "population": 124728
        },
        {
            "division": "Dhaka",
            "upazila": "Adabor",
            "district": "Dhaka",
            "population": 203989
        },
        {
            "division": "Dhaka",
            "upazila": "Badda",
            "district": "Dhaka",
            "population": 536621
        },
        {
            "division": "Dhaka",
            "upazila": "Bangshal",
            "district": "Dhaka",
            "population": 186952
        },
        {
            "division": "Dhaka",
            "upazila": "Biman bandar",
            "district": "Dhaka",
            "population": 10626
        },
        {
            "division": "Dhaka",
            "upazila": "Cantonment",
            "district": "Dhaka",
            "population": 131864
        },
        {
            "division": "Dhaka",
            "upazila": "Chak bazar",
            "district": "Dhaka",
            "population": 156147
        },
        {
            "division": "Dhaka",
            "upazila": "Dakshinkhan",
            "district": "Dhaka",
            "population": 255931
        },
        {
            "division": "Dhaka",
            "upazila": "Darus salam",
            "district": "Dhaka",
            "population": 159139
        },
        {
            "division": "Dhaka",
            "upazila": "Demra",
            "district": "Dhaka",
            "population": 226679
        },
        {
            "division": "Dhaka",
            "upazila": "Dhamrai",
            "district": "Dhaka",
            "population": 412418
        },
        {
            "division": "Dhaka",
            "upazila": "302616",
            "district": "Dhaka",
            "population": 147643
        },
        {
            "division": "Dhaka",
            "upazila": "Dohar",
            "district": "Dhaka",
            "population": 226439
        },
        {
            "division": "Dhaka",
            "upazila": "Gendaria",
            "district": "Dhaka",
            "population": 137721
        },
        {
            "division": "Dhaka",
            "upazila": "Gulshan",
            "district": "Dhaka",
            "population": 253050
        },
        {
            "division": "Dhaka",
            "upazila": "302628",
            "district": "Dhaka",
            "population": 185639
        },
        {
            "division": "Dhaka",
            "upazila": "Jatrabari",
            "district": "Dhaka",
            "population": 443601
        },
        {
            "division": "Dhaka",
            "upazila": "Kafrul",
            "district": "Dhaka",
            "population": 396182
        },
        {
            "division": "Dhaka",
            "upazila": "Kadamtali",
            "district": "Dhaka",
            "population": 370895
        },
        {
            "division": "Dhaka",
            "upazila": "Kalabagan",
            "district": "Dhaka",
            "population": 118660
        },
        {
            "division": "Dhaka",
            "upazila": "Kamrangir char",
            "district": "Dhaka",
            "population": 93601
        },
        {
            "division": "Dhaka",
            "upazila": "Khilgaon",
            "district": "Dhaka",
            "population": 327717
        },
        {
            "division": "Dhaka",
            "upazila": "Khilkhet",
            "district": "Dhaka",
            "population": 130053
        },
        {
            "division": "Dhaka",
            "upazila": "Keraniganj",
            "district": "Dhaka",
            "population": 794360
        },
        {
            "division": "Dhaka",
            "upazila": "Kotwali",
            "district": "Dhaka",
            "population": 62087
        },
        {
            "division": "Dhaka",
            "upazila": "Lalbagh",
            "district": "Dhaka",
            "population": 369933
        },
        {
            "division": "Dhaka",
            "upazila": "Mirpur",
            "district": "Dhaka",
            "population": 500373
        },
        {
            "division": "Dhaka",
            "upazila": "302650",
            "district": "Dhaka",
            "population": 355843
        },
        {
            "division": "Dhaka",
            "upazila": "Motijheel",
            "district": "Dhaka",
            "population": 210006
        },
        {
            "division": "Dhaka",
            "upazila": "Nawabganj",
            "district": "Dhaka",
            "population": 318811
        },
        {
            "division": "Dhaka",
            "upazila": "New market",
            "district": "Dhaka",
            "population": 49523
        },
        {
            "division": "Dhaka",
            "upazila": "Pallabi",
            "district": "Dhaka",
            "population": 596835
        },
        {
            "division": "Dhaka",
            "upazila": "Paltan",
            "district": "Dhaka",
            "population": 59639
        },
        {
            "division": "Dhaka",
            "upazila": "302666",
            "district": "Dhaka",
            "population": 200973
        },
        {
            "division": "Dhaka",
            "upazila": "Rampura",
            "district": "Dhaka",
            "population": 224079
        },
        {
            "division": "Dhaka",
            "upazila": "Sabujbagh",
            "district": "Dhaka",
            "population": 376421
        },
        {
            "division": "Dhaka",
            "upazila": "Savar",
            "district": "Dhaka",
            "population": 1385910
        },
        {
            "division": "Dhaka",
            "upazila": "Shah ali",
            "district": "Dhaka",
            "population": 115489
        },
        {
            "division": "Dhaka",
            "upazila": "Shahbagh",
            "district": "Dhaka",
            "population": 68140
        },
        {
            "division": "Dhaka",
            "upazila": "Shyampur",
            "district": "Dhaka",
            "population": 184062
        },
        {
            "division": "Dhaka",
            "upazila": "Sher-e-bangla nagar",
            "district": "Dhaka",
            "population": 137573
        },
        {
            "division": "Dhaka",
            "upazila": "Sutrapur",
            "district": "Dhaka",
            "population": 211210
        },
        {
            "division": "Dhaka",
            "upazila": "Tejgaon",
            "district": "Dhaka",
            "population": 148255
        },
        {
            "division": "Dhaka",
            "upazila": "Tejgaon",
            "district": "Dhaka",
            "population": 146732
        },
        {
            "division": "Dhaka",
            "upazila": "Turag",
            "district": "Dhaka",
            "population": 157316
        },
        {
            "division": "Dhaka",
            "upazila": "Uttara  purba",
            "district": "Dhaka",
            "population": 179907
        },
        {
            "division": "Dhaka",
            "upazila": "Uttar khan",
            "district": "Dhaka",
            "population": 78933
        },
        {
            "division": "Dhaka",
            "upazila": "Alfadanga",
            "district": "Faridpur",
            "population": 108302
        },
        {
            "division": "Dhaka",
            "upazila": "Bhanga",
            "district": "Faridpur",
            "population": 259032
        },
        {
            "division": "Dhaka",
            "upazila": "Boalmari",
            "district": "Faridpur",
            "population": 256658
        },
        {
            "division": "Dhaka",
            "upazila": "Char Bhadrasan",
            "district": "Faridpur",
            "population": 63477
        },
        {
            "division": "Dhaka",
            "upazila": "Faridpur",
            "district": "Faridpur",
            "population": 469410
        },
        {
            "division": "Dhaka",
            "upazila": "Madhukhali",
            "district": "Faridpur",
            "population": 204492
        },
        {
            "division": "Dhaka",
            "upazila": "Nagarkanda",
            "district": "Faridpur",
            "population": 197898
        },
        {
            "division": "Dhaka",
            "upazila": "Sadarpur",
            "district": "Faridpur",
            "population": 186254
        },
        {
            "division": "Dhaka",
            "upazila": "Saltha",
            "district": "Faridpur",
            "population": 167446
        },
        {
            "division": "Dhaka",
            "upazila": "Gazipur",
            "district": "Gazipur",
            "population": 1820374
        },
        {
            "division": "Dhaka",
            "upazila": "Kaliakair",
            "district": "Gazipur",
            "population": 483308
        },
        {
            "division": "Dhaka",
            "upazila": "Kaliganj",
            "district": "Gazipur",
            "population": 265276
        },
        {
            "division": "Dhaka",
            "upazila": "Kapasia",
            "district": "Gazipur",
            "population": 342162
        },
        {
            "division": "Dhaka",
            "upazila": "Sreepur",
            "district": "Gazipur",
            "population": 492792
        },
        {
            "division": "Dhaka",
            "upazila": "Gopalganj",
            "district": "Gopalganj",
            "population": 344008
        },
        {
            "division": "Dhaka",
            "upazila": "Kashiani",
            "district": "Gopalganj",
            "population": 207615
        },
        {
            "division": "Dhaka",
            "upazila": "Kotalipara",
            "district": "Gopalganj",
            "population": 230493
        },
        {
            "division": "Dhaka",
            "upazila": "Muksudpur",
            "district": "Gopalganj",
            "population": 289406
        },
        {
            "division": "Dhaka",
            "upazila": "Tungipara",
            "district": "Gopalganj",
            "population": 100893
        },
        {
            "division": "Dhaka",
            "upazila": "Bakshiganj",
            "district": "Jamalpur",
            "population": 218930
        },
        {
            "division": "Dhaka",
            "upazila": "Dewanganj",
            "district": "Jamalpur",
            "population": 258133
        },
        {
            "division": "Dhaka",
            "upazila": "Islampur",
            "district": "Jamalpur",
            "population": 298429
        },
        {
            "division": "Dhaka",
            "upazila": "Jamalpur",
            "district": "Jamalpur",
            "population": 615072
        },
        {
            "division": "Dhaka",
            "upazila": "Madarganj",
            "district": "Jamalpur",
            "population": 263608
        },
        {
            "division": "Dhaka",
            "upazila": "Melandaha",
            "district": "Jamalpur",
            "population": 313182
        },
        {
            "division": "Dhaka",
            "upazila": "Sarishabari",
            "district": "Jamalpur",
            "population": 325320
        },
        {
            "division": "Dhaka",
            "upazila": "Austagram",
            "district": "Kishoreganj",
            "population": 152523
        },
        {
            "division": "Dhaka",
            "upazila": "Bajitpur",
            "district": "Kishoreganj",
            "population": 248730
        },
        {
            "division": "Dhaka",
            "upazila": "Bhairab",
            "district": "Kishoreganj",
            "population": 298309
        },
        {
            "division": "Dhaka",
            "upazila": "Hossainpur",
            "district": "Kishoreganj",
            "population": 183884
        },
        {
            "division": "Dhaka",
            "upazila": "Itna",
            "district": "Kishoreganj",
            "population": 164127
        },
        {
            "division": "Dhaka",
            "upazila": "Karimganj",
            "district": "Kishoreganj",
            "population": 287807
        },
        {
            "division": "Dhaka",
            "upazila": "Katiadi",
            "district": "Kishoreganj",
            "population": 314529
        },
        {
            "division": "Dhaka",
            "upazila": "Kishoreganj",
            "district": "Kishoreganj",
            "population": 414208
        },
        {
            "division": "Dhaka",
            "upazila": "Kuliar Char",
            "district": "Kishoreganj",
            "population": 182236
        },
        {
            "division": "Dhaka",
            "upazila": "Mithamain",
            "district": "Kishoreganj",
            "population": 122026
        },
        {
            "division": "Dhaka",
            "upazila": "Nikli",
            "district": "Kishoreganj",
            "population": 133729
        },
        {
            "division": "Dhaka",
            "upazila": "Pakundia",
            "district": "Kishoreganj",
            "population": 250060
        },
        {
            "division": "Dhaka",
            "upazila": "Tarail",
            "district": "Kishoreganj",
            "population": 159739
        },
        {
            "division": "Dhaka",
            "upazila": "Kalkini",
            "district": "Madaripur",
            "population": 273258
        },
        {
            "division": "Dhaka",
            "upazila": "Madaripur",
            "district": "Madaripur",
            "population": 345764
        },
        {
            "division": "Dhaka",
            "upazila": "Rajoir",
            "district": "Madaripur",
            "population": 228710
        },
        {
            "division": "Dhaka",
            "upazila": "Shib Char",
            "district": "Madaripur",
            "population": 318220
        },
        {
            "division": "Dhaka",
            "upazila": "Daulatpur",
            "district": "Manikganj",
            "population": 167026
        },
        {
            "division": "Dhaka",
            "upazila": "Ghior",
            "district": "Manikganj",
            "population": 146292
        },
        {
            "division": "Dhaka",
            "upazila": "Harirampur",
            "district": "Manikganj",
            "population": 139318
        },
        {
            "division": "Dhaka",
            "upazila": "Manikganj",
            "district": "Manikganj",
            "population": 309413
        },
        {
            "division": "Dhaka",
            "upazila": "Saturia",
            "district": "Manikganj",
            "population": 171494
        },
        {
            "division": "Dhaka",
            "upazila": "Shibalaya",
            "district": "Manikganj",
            "population": 171873
        },
        {
            "division": "Dhaka",
            "upazila": "Singair",
            "district": "Manikganj",
            "population": 287451
        },
        {
            "division": "Dhaka",
            "upazila": "Gazaria",
            "district": "Munshiganj",
            "population": 157988
        },
        {
            "division": "Dhaka",
            "upazila": "Lohajang",
            "district": "Munshiganj",
            "population": 159242
        },
        {
            "division": "Dhaka",
            "upazila": "Munshiganj",
            "district": "Munshiganj",
            "population": 383263
        },
        {
            "division": "Dhaka",
            "upazila": "Serajdikhan",
            "district": "Munshiganj",
            "population": 288107
        },
        {
            "division": "Dhaka",
            "upazila": "Sreenagar",
            "district": "Munshiganj",
            "population": 259887
        },
        {
            "division": "Dhaka",
            "upazila": "Tongibari",
            "district": "Munshiganj",
            "population": 197173
        },
        {
            "division": "Dhaka",
            "upazila": "Bhaluka",
            "district": "Mymensingh",
            "population": 430320
        },
        {
            "division": "Dhaka",
            "upazila": "Dhobaura",
            "district": "Mymensingh",
            "population": 196284
        },
        {
            "division": "Dhaka",
            "upazila": "Fulbaria",
            "district": "Mymensingh",
            "population": 448467
        },
        {
            "division": "Dhaka",
            "upazila": "Gaffargaon",
            "district": "Mymensingh",
            "population": 430746
        },
        {
            "division": "Dhaka",
            "upazila": "Gauripur",
            "district": "Mymensingh",
            "population": 323057
        },
        {
            "division": "Dhaka",
            "upazila": "Haluaghat",
            "district": "Mymensingh",
            "population": 290043
        },
        {
            "division": "Dhaka",
            "upazila": "Ishwarganj",
            "district": "Mymensingh",
            "population": 376348
        },
        {
            "division": "Dhaka",
            "upazila": "Mymensingh",
            "district": "Mymensingh",
            "population": 775733
        },
        {
            "division": "Dhaka",
            "upazila": "Muktagachha",
            "district": "Mymensingh",
            "population": 415473
        },
        {
            "division": "Dhaka",
            "upazila": "Nandail",
            "district": "Mymensingh",
            "population": 402727
        },
        {
            "division": "Dhaka",
            "upazila": "Phulpur",
            "district": "Mymensingh",
            "population": 601766
        },
        {
            "division": "Dhaka",
            "upazila": "Trishal",
            "district": "Mymensingh",
            "population": 419308
        },
        {
            "division": "Dhaka",
            "upazila": "Araihazar",
            "district": "Narayanganj",
            "population": 376550
        },
        {
            "division": "Dhaka",
            "upazila": "Sonargaon",
            "district": "Narayanganj",
            "population": 400358
        },
        {
            "division": "Dhaka",
            "upazila": "Bandar",
            "district": "Narayanganj",
            "population": 312841
        },
        {
            "division": "Dhaka",
            "upazila": "Narayanganj",
            "district": "Narayanganj",
            "population": 1323600
        },
        {
            "division": "Dhaka",
            "upazila": "Rupganj",
            "district": "Narayanganj",
            "population": 534868
        },
        {
            "division": "Dhaka",
            "upazila": "Belabo",
            "district": "Narsingdi",
            "population": 190086
        },
        {
            "division": "Dhaka",
            "upazila": "Manohardi",
            "district": "Narsingdi",
            "population": 275112
        },
        {
            "division": "Dhaka",
            "upazila": "Narsingdi",
            "district": "Narsingdi",
            "population": 707525
        },
        {
            "division": "Dhaka",
            "upazila": "Palash",
            "district": "Narsingdi",
            "population": 212612
        },
        {
            "division": "Dhaka",
            "upazila": "Roypura",
            "district": "Narsingdi",
            "population": 535796
        },
        {
            "division": "Dhaka",
            "upazila": "Shibpur",
            "district": "Narsingdi",
            "population": 303813
        },
        {
            "division": "Dhaka",
            "upazila": "Atpara",
            "district": "Netrokona",
            "population": 144624
        },
        {
            "division": "Dhaka",
            "upazila": "Barhatta",
            "district": "Netrokona",
            "population": 180449
        },
        {
            "division": "Dhaka",
            "upazila": "Durgapur",
            "district": "Netrokona",
            "population": 224873
        },
        {
            "division": "Dhaka",
            "upazila": "Khaliajuri",
            "district": "Netrokona",
            "population": 97450
        },
        {
            "division": "Dhaka",
            "upazila": "Kalmakanda",
            "district": "Netrokona",
            "population": 271912
        },
        {
            "division": "Dhaka",
            "upazila": "Kendua",
            "district": "Netrokona",
            "population": 304729
        },
        {
            "division": "Dhaka",
            "upazila": "Madan",
            "district": "Netrokona",
            "population": 154479
        },
        {
            "division": "Dhaka",
            "upazila": "Mohanganj",
            "district": "Netrokona",
            "population": 167507
        },
        {
            "division": "Dhaka",
            "upazila": "Netrokona",
            "district": "Netrokona",
            "population": 372785
        },
        {
            "division": "Dhaka",
            "upazila": "Purbadhala",
            "district": "Netrokona",
            "population": 310834
        },
        {
            "division": "Dhaka",
            "upazila": "Baliakandi",
            "district": "Rajbari",
            "population": 207086
        },
        {
            "division": "Dhaka",
            "upazila": "Goalanda",
            "district": "Rajbari",
            "population": 112732
        },
        {
            "division": "Dhaka",
            "upazila": "Kalukhali",
            "district": "Rajbari",
            "population": 155044
        },
        {
            "division": "Dhaka",
            "upazila": "Pangsha",
            "district": "Rajbari",
            "population": 243285
        },
        {
            "division": "Dhaka",
            "upazila": "Rajbari",
            "district": "Rajbari",
            "population": 331631
        },
        {
            "division": "Dhaka",
            "upazila": "Bhedarganj",
            "district": "Shariatpur",
            "population": 253234
        },
        {
            "division": "Dhaka",
            "upazila": "Damudya",
            "district": "Shariatpur",
            "population": 109003
        },
        {
            "division": "Dhaka",
            "upazila": "Gosairhat",
            "district": "Shariatpur",
            "population": 157665
        },
        {
            "division": "Dhaka",
            "upazila": "Naria",
            "district": "Shariatpur",
            "population": 231644
        },
        {
            "division": "Dhaka",
            "upazila": "Shariatpur",
            "district": "Shariatpur",
            "population": 210259
        },
        {
            "division": "Dhaka",
            "upazila": "Zanjira",
            "district": "Shariatpur",
            "population": 194019
        },
        {
            "division": "Dhaka",
            "upazila": "Jhenaigati",
            "district": "Sherpur",
            "population": 160452
        },
        {
            "division": "Dhaka",
            "upazila": "Nakla",
            "district": "Sherpur",
            "population": 189685
        },
        {
            "division": "Dhaka",
            "upazila": "Nalitabari",
            "district": "Sherpur",
            "population": 251361
        },
        {
            "division": "Dhaka",
            "upazila": "Sherpur",
            "district": "Sherpur",
            "population": 497179
        },
        {
            "division": "Dhaka",
            "upazila": "Sreebardi",
            "district": "Sherpur",
            "population": 259648
        },
        {
            "division": "Dhaka",
            "upazila": "Basail",
            "district": "Tangail ",
            "population": 159870
        },
        {
            "division": "Dhaka",
            "upazila": "Bhuapur",
            "district": "Tangail ",
            "population": 189913
        },
        {
            "division": "Dhaka",
            "upazila": "Delduar",
            "district": "Tangail ",
            "population": 207278
        },
        {
            "division": "Dhaka",
            "upazila": "Dhanbari",
            "district": "Tangail ",
            "population": 176068
        },
        {
            "division": "Dhaka",
            "upazila": "Ghatail",
            "district": "Tangail ",
            "population": 417939
        },
        {
            "division": "Dhaka",
            "upazila": "Gopalpur",
            "district": "Tangail ",
            "population": 252331
        },
        {
            "division": "Dhaka",
            "upazila": "Kalihati",
            "district": "Tangail ",
            "population": 410293
        },
        {
            "division": "Dhaka",
            "upazila": "Madhupur",
            "district": "Tangail ",
            "population": 296729
        },
        {
            "division": "Dhaka",
            "upazila": "Mirzapur",
            "district": "Tangail ",
            "population": 407781
        },
        {
            "division": "Dhaka",
            "upazila": "Nagarpur",
            "district": "Tangail ",
            "population": 288092
        },
        {
            "division": "Dhaka",
            "upazila": "Sakhipur",
            "district": "Tangail ",
            "population": 277685
        },
        {
            "division": "Dhaka",
            "upazila": "Tangail",
            "district": "Tangail ",
            "population": 521104
        },
        {
            "division": "Khulna",
            "upazila": "Bagerhat",
            "district": "Bagerhat",
            "population": 266389
        },
        {
            "division": "Khulna",
            "upazila": "Chitalmari",
            "district": "Bagerhat",
            "population": 138810
        },
        {
            "division": "Khulna",
            "upazila": "Fakirhat",
            "district": "Bagerhat",
            "population": 137789
        },
        {
            "division": "Khulna",
            "upazila": "Kachua",
            "district": "Bagerhat",
            "population": 97011
        },
        {
            "division": "Khulna",
            "upazila": "Mollahat",
            "district": "Bagerhat",
            "population": 130878
        },
        {
            "division": "Khulna",
            "upazila": "Mongla",
            "district": "Bagerhat",
            "population": 136588
        },
        {
            "division": "Khulna",
            "upazila": "Morrelganj",
            "district": "Bagerhat",
            "population": 294576
        },
        {
            "division": "Khulna",
            "upazila": "Rampal",
            "district": "Bagerhat",
            "population": 154965
        },
        {
            "division": "Khulna",
            "upazila": "Sarankhola",
            "district": "Bagerhat",
            "population": 119084
        },
        {
            "division": "Khulna",
            "upazila": "Alamdanga",
            "district": "Chuadanga",
            "population": 345922
        },
        {
            "division": "Khulna",
            "upazila": "Chuadanga",
            "district": "Chuadanga",
            "population": 313935
        },
        {
            "division": "Khulna",
            "upazila": "Damurhuda",
            "district": "Chuadanga",
            "population": 289577
        },
        {
            "division": "Khulna",
            "upazila": "Jiban Nagar",
            "district": "Chuadanga",
            "population": 179581
        },
        {
            "division": "Khulna",
            "upazila": "Abhaynagar",
            "district": "Jessore",
            "population": 262434
        },
        {
            "division": "Khulna",
            "upazila": "Bagherpara",
            "district": "Jessore",
            "population": 216897
        },
        {
            "division": "Khulna",
            "upazila": "Chaugachha",
            "district": "Jessore",
            "population": 231370
        },
        {
            "division": "Khulna",
            "upazila": "Jhikargachha",
            "district": "Jessore",
            "population": 298908
        },
        {
            "division": "Khulna",
            "upazila": "Keshabpur",
            "district": "Jessore",
            "population": 253291
        },
        {
            "division": "Khulna",
            "upazila": "Jessore",
            "district": "Jessore",
            "population": 742898
        },
        {
            "division": "Khulna",
            "upazila": "Manirampur",
            "district": "Jessore",
            "population": 417421
        },
        {
            "division": "Khulna",
            "upazila": "Sharsha",
            "district": "Jessore",
            "population": 341328
        },
        {
            "division": "Khulna",
            "upazila": "Harinakunda",
            "district": "Jhenaidah",
            "population": 197723
        },
        {
            "division": "Khulna",
            "upazila": "Jhenaidah",
            "district": "Jhenaidah",
            "population": 455932
        },
        {
            "division": "Khulna",
            "upazila": "Kaliganj",
            "district": "Jhenaidah",
            "population": 282366
        },
        {
            "division": "Khulna",
            "upazila": "Kotchandpur",
            "district": "Jhenaidah",
            "population": 141121
        },
        {
            "division": "Khulna",
            "upazila": "Maheshpur",
            "district": "Jhenaidah",
            "population": 332514
        },
        {
            "division": "Khulna",
            "upazila": "Shailkupa",
            "district": "Jhenaidah",
            "population": 361648
        },
        {
            "division": "Khulna",
            "upazila": "Batiaghata",
            "district": "Khulna",
            "population": 171691
        },
        {
            "division": "Khulna",
            "upazila": "Dacope",
            "district": "Khulna",
            "population": 152316
        },
        {
            "division": "Khulna",
            "upazila": "Daulatpur",
            "district": "Khulna",
            "population": 112442
        },
        {
            "division": "Khulna",
            "upazila": "Dumuria",
            "district": "Khulna",
            "population": 305675
        },
        {
            "division": "Khulna",
            "upazila": "Dighalia",
            "district": "Khulna",
            "population": 115585
        },
        {
            "division": "Khulna",
            "upazila": "Khalishpur",
            "district": "Khulna",
            "population": 165299
        },
        {
            "division": "Khulna",
            "upazila": "Khan jahan ali",
            "district": "Khulna",
            "population": 81313
        },
        {
            "division": "Khulna",
            "upazila": "Khulna",
            "district": "Khulna",
            "population": 224444
        },
        {
            "division": "Khulna",
            "upazila": "Koyra",
            "district": "Khulna",
            "population": 193931
        },
        {
            "division": "Khulna",
            "upazila": "Paikgachha",
            "district": "Khulna",
            "population": 247983
        },
        {
            "division": "Khulna",
            "upazila": "Phultala",
            "district": "Khulna",
            "population": 83881
        },
        {
            "division": "Khulna",
            "upazila": "Rupsa",
            "district": "Khulna",
            "population": 179519
        },
        {
            "division": "Khulna",
            "upazila": "Sonadanga",
            "district": "Khulna",
            "population": 167739
        },
        {
            "division": "Khulna",
            "upazila": "Terokhada",
            "district": "Khulna",
            "population": 116709
        },
        {
            "division": "Khulna",
            "upazila": "Bheramara",
            "district": "Kushtia",
            "population": 200084
        },
        {
            "division": "Khulna",
            "upazila": "Daulatpur",
            "district": "Kushtia",
            "population": 456372
        },
        {
            "division": "Khulna",
            "upazila": "Khoksa",
            "district": "Kushtia",
            "population": 129555
        },
        {
            "division": "Khulna",
            "upazila": "Kumarkhali",
            "district": "Kushtia",
            "population": 328457
        },
        {
            "division": "Khulna",
            "upazila": "Kushtia",
            "district": "Kushtia",
            "population": 502255
        },
        {
            "division": "Khulna",
            "upazila": "Mirpur",
            "district": "Kushtia",
            "population": 330115
        },
        {
            "division": "Khulna",
            "upazila": "Magura",
            "district": "Magura",
            "population": 380107
        },
        {
            "division": "Khulna",
            "upazila": "Mohammadpur",
            "district": "Magura",
            "population": 207905
        },
        {
            "division": "Khulna",
            "upazila": "Shalikha",
            "district": "Magura",
            "population": 163658
        },
        {
            "division": "Khulna",
            "upazila": "Sreepur",
            "district": "Magura",
            "population": 166749
        },
        {
            "division": "Khulna",
            "upazila": "Gangni",
            "district": "Meherpur",
            "population": 299607
        },
        {
            "division": "Khulna",
            "upazila": "Mujib Nagar",
            "district": "Meherpur",
            "population": 99143
        },
        {
            "division": "Khulna",
            "upazila": "Meherpur",
            "district": "Meherpur",
            "population": 256642
        },
        {
            "division": "Khulna",
            "upazila": "Kalia",
            "district": "Narail",
            "population": 220202
        },
        {
            "division": "Khulna",
            "upazila": "Lohagara",
            "district": "Narail",
            "population": 228594
        },
        {
            "division": "Khulna",
            "upazila": "Narail",
            "district": "Narail",
            "population": 272872
        },
        {
            "division": "Khulna",
            "upazila": "Assasuni",
            "district": "Satkhira",
            "population": 268754
        },
        {
            "division": "Khulna",
            "upazila": "Debhata",
            "district": "Satkhira",
            "population": 125358
        },
        {
            "division": "Khulna",
            "upazila": "Kalaroa",
            "district": "Satkhira",
            "population": 237992
        },
        {
            "division": "Khulna",
            "upazila": "Kaliganj",
            "district": "Satkhira",
            "population": 274889
        },
        {
            "division": "Khulna",
            "upazila": "Satkhira",
            "district": "Satkhira",
            "population": 460892
        },
        {
            "division": "Khulna",
            "upazila": "Shyamnagar",
            "district": "Satkhira",
            "population": 318254
        },
        {
            "division": "Khulna",
            "upazila": "Tala",
            "district": "Satkhira",
            "population": 299820
        },
        {
            "division": "Rajshahi",
            "upazila": "Adamdighi",
            "district": "Bogra ",
            "population": 195186
        },
        {
            "division": "Rajshahi",
            "upazila": "Bogra",
            "district": "Bogra ",
            "population": 555014
        },
        {
            "division": "Rajshahi",
            "upazila": "Dhunat",
            "district": "Bogra ",
            "population": 292404
        },
        {
            "division": "Rajshahi",
            "upazila": "Dhupchanchia",
            "district": "Bogra ",
            "population": 176678
        },
        {
            "division": "Rajshahi",
            "upazila": "Gabtali",
            "district": "Bogra ",
            "population": 319588
        },
        {
            "division": "Rajshahi",
            "upazila": "Kahaloo",
            "district": "Bogra ",
            "population": 222376
        },
        {
            "division": "Rajshahi",
            "upazila": "Nandigram",
            "district": "Bogra ",
            "population": 180802
        },
        {
            "division": "Rajshahi",
            "upazila": "Sariakandi",
            "district": "Bogra ",
            "population": 270719
        },
        {
            "division": "Rajshahi",
            "upazila": "Shajahanpur",
            "district": "Bogra ",
            "population": 289804
        },
        {
            "division": "Rajshahi",
            "upazila": "Sherpur",
            "district": "Bogra ",
            "population": 332825
        },
        {
            "division": "Rajshahi",
            "upazila": "Shibganj",
            "district": "Bogra ",
            "population": 378700
        },
        {
            "division": "Rajshahi",
            "upazila": "Sonatola",
            "district": "Bogra ",
            "population": 186778
        },
        {
            "division": "Rajshahi",
            "upazila": "Akkelpur",
            "district": "Joypurhat",
            "population": 137619
        },
        {
            "division": "Rajshahi",
            "upazila": "Joypurhat",
            "district": "Joypurhat",
            "population": 289058
        },
        {
            "division": "Rajshahi",
            "upazila": "Kalai",
            "district": "Joypurhat",
            "population": 143197
        },
        {
            "division": "Rajshahi",
            "upazila": "Khetlal",
            "district": "Joypurhat",
            "population": 108326
        },
        {
            "division": "Rajshahi",
            "upazila": "Panchbibi",
            "district": "Joypurhat",
            "population": 235568
        },
        {
            "division": "Rajshahi",
            "upazila": "Atrai",
            "district": "Naogaon",
            "population": 193256
        },
        {
            "division": "Rajshahi",
            "upazila": "Badalgachhi",
            "district": "Naogaon",
            "population": 201342
        },
        {
            "division": "Rajshahi",
            "upazila": "Dhamoirhat",
            "district": "Naogaon",
            "population": 184778
        },
        {
            "division": "Rajshahi",
            "upazila": "Manda",
            "district": "Naogaon",
            "population": 363858
        },
        {
            "division": "Rajshahi",
            "upazila": "Mahadebpur",
            "district": "Naogaon",
            "population": 292859
        },
        {
            "division": "Rajshahi",
            "upazila": "Naogaon",
            "district": "Naogaon",
            "population": 405148
        },
        {
            "division": "Rajshahi",
            "upazila": "Niamatpur",
            "district": "Naogaon",
            "population": 248351
        },
        {
            "division": "Rajshahi",
            "upazila": "Patnitala",
            "district": "Naogaon",
            "population": 231900
        },
        {
            "division": "Rajshahi",
            "upazila": "Porsha",
            "district": "Naogaon",
            "population": 132095
        },
        {
            "division": "Rajshahi",
            "upazila": "Raninagar",
            "district": "Naogaon",
            "population": 184778
        },
        {
            "division": "Rajshahi",
            "upazila": "Sapahar",
            "district": "Naogaon",
            "population": 161792
        },
        {
            "division": "Rajshahi",
            "upazila": "Bagatipara",
            "district": "Natore",
            "population": 131004
        },
        {
            "division": "Rajshahi",
            "upazila": "Baraigram",
            "district": "Natore",
            "population": 279672
        },
        {
            "division": "Rajshahi",
            "upazila": "Gurudaspur",
            "district": "Natore",
            "population": 214788
        },
        {
            "division": "Rajshahi",
            "upazila": "Lalpur",
            "district": "Natore",
            "population": 274405
        },
        {
            "division": "Rajshahi",
            "upazila": "Natore",
            "district": "Natore",
            "population": 442422
        },
        {
            "division": "Rajshahi",
            "upazila": "Singra",
            "district": "Natore",
            "population": 364382
        },
        {
            "division": "Rajshahi",
            "upazila": "Bholahat",
            "district": "Chapai",
            "population": 103301
        },
        {
            "division": "Rajshahi",
            "upazila": "Gomastapur",
            "district": "Chapai",
            "population": 275823
        },
        {
            "division": "Rajshahi",
            "upazila": "Nachole",
            "district": "Chapai",
            "population": 146627
        },
        {
            "division": "Rajshahi",
            "upazila": "Chapai",
            "district": "Chapai",
            "population": 530592
        },
        {
            "division": "Rajshahi",
            "upazila": "Shibganj",
            "district": "Chapai",
            "population": 591178
        },
        {
            "division": "Rajshahi",
            "upazila": "Atgharia",
            "district": "Pabna",
            "population": 157254
        },
        {
            "division": "Rajshahi",
            "upazila": "Bera",
            "district": "Pabna",
            "population": 256793
        },
        {
            "division": "Rajshahi",
            "upazila": "Bhangura",
            "district": "Pabna",
            "population": 124433
        },
        {
            "division": "Rajshahi",
            "upazila": "Chatmohar",
            "district": "Pabna",
            "population": 291121
        },
        {
            "division": "Rajshahi",
            "upazila": "Faridpur",
            "district": "Pabna",
            "population": 130335
        },
        {
            "division": "Rajshahi",
            "upazila": "Ishwardi",
            "district": "Pabna",
            "population": 313932
        },
        {
            "division": "Rajshahi",
            "upazila": "Pabna",
            "district": "Pabna",
            "population": 590914
        },
        {
            "division": "Rajshahi",
            "upazila": "Santhia",
            "district": "Pabna",
            "population": 380301
        },
        {
            "division": "Rajshahi",
            "upazila": "Sujanagar",
            "district": "Pabna",
            "population": 278096
        },
        {
            "division": "Rajshahi",
            "upazila": "Bagha",
            "district": "Rajshahi",
            "population": 184183
        },
        {
            "division": "Rajshahi",
            "upazila": "Baghmara",
            "district": "Rajshahi",
            "population": 354664
        },
        {
            "division": "Rajshahi",
            "upazila": "Boalia",
            "district": "Rajshahi",
            "population": 221163
        },
        {
            "division": "Rajshahi",
            "upazila": "Charghat",
            "district": "Rajshahi",
            "population": 206788
        },
        {
            "division": "Rajshahi",
            "upazila": "Durgapur",
            "district": "Rajshahi",
            "population": 185845
        },
        {
            "division": "Rajshahi",
            "upazila": "Godagari",
            "district": "Rajshahi",
            "population": 330924
        },
        {
            "division": "Rajshahi",
            "upazila": "Matihar",
            "district": "Rajshahi",
            "population": 62172
        },
        {
            "division": "Rajshahi",
            "upazila": "Mohanpur",
            "district": "Rajshahi",
            "population": 170021
        },
        {
            "division": "Rajshahi",
            "upazila": "Paba",
            "district": "Rajshahi",
            "population": 314196
        },
        {
            "division": "Rajshahi",
            "upazila": "Puthia",
            "district": "Rajshahi",
            "population": 207490
        },
        {
            "division": "Rajshahi",
            "upazila": "Rajpara",
            "district": "Rajshahi",
            "population": 137318
        },
        {
            "division": "Rajshahi",
            "upazila": "Shah makhdum",
            "district": "Rajshahi",
            "population": 29103
        },
        {
            "division": "Rajshahi",
            "upazila": "Tanore",
            "district": "Rajshahi",
            "population": 191330
        },
        {
            "division": "Rajshahi",
            "upazila": "Belkuchi",
            "district": "Sirajganj",
            "population": 352835
        },
        {
            "division": "Rajshahi",
            "upazila": "Chauhali",
            "district": "Sirajganj",
            "population": 160063
        },
        {
            "division": "Rajshahi",
            "upazila": "Kamarkhanda",
            "district": "Sirajganj",
            "population": 138645
        },
        {
            "division": "Rajshahi",
            "upazila": "Kazipur",
            "district": "Sirajganj",
            "population": 274679
        },
        {
            "division": "Rajshahi",
            "upazila": "Royganj",
            "district": "Sirajganj",
            "population": 317666
        },
        {
            "division": "Rajshahi",
            "upazila": "Shahjadpur",
            "district": "Sirajganj",
            "population": 561076
        },
        {
            "division": "Rajshahi",
            "upazila": "Sirajganj",
            "district": "Sirajganj",
            "population": 555155
        },
        {
            "division": "Rajshahi",
            "upazila": "Tarash",
            "district": "Sirajganj",
            "population": 197214
        },
        {
            "division": "Rajshahi",
            "upazila": "Ullah para",
            "district": "Sirajganj",
            "population": 540156
        },
        {
            "division": "Rangpur",
            "upazila": "Birampur",
            "district": "Dinajpur",
            "population": 170806
        },
        {
            "division": "Rangpur",
            "upazila": "Birganj",
            "district": "Dinajpur",
            "population": 317253
        },
        {
            "division": "Rangpur",
            "upazila": "Biral",
            "district": "Dinajpur",
            "population": 257925
        },
        {
            "division": "Rangpur",
            "upazila": "Bochaganj",
            "district": "Dinajpur",
            "population": 160049
        },
        {
            "division": "Rangpur",
            "upazila": "Chirirbandar",
            "district": "Dinajpur",
            "population": 292500
        },
        {
            "division": "Rangpur",
            "upazila": "Fulbari",
            "district": "Dinajpur",
            "population": 176023
        },
        {
            "division": "Rangpur",
            "upazila": "Ghoraghat",
            "district": "Dinajpur",
            "population": 117740
        },
        {
            "division": "Rangpur",
            "upazila": "Hakimpur",
            "district": "Dinajpur",
            "population": 92599
        },
        {
            "division": "Rangpur",
            "upazila": "Kaharole",
            "district": "Dinajpur",
            "population": 154432
        },
        {
            "division": "Rangpur",
            "upazila": "Khansama",
            "district": "Dinajpur",
            "population": 171764
        },
        {
            "division": "Rangpur",
            "upazila": "Dinajpur",
            "district": "Dinajpur",
            "population": 484597
        },
        {
            "division": "Rangpur",
            "upazila": "Nawabganj",
            "district": "Dinajpur",
            "population": 229337
        },
        {
            "division": "Rangpur",
            "upazila": "Parbatipur",
            "district": "Dinajpur",
            "population": 365103
        },
        {
            "division": "Rangpur",
            "upazila": "Fulchhari",
            "district": "Gaibandha",
            "population": 165334
        },
        {
            "division": "Rangpur",
            "upazila": "Gaibandha",
            "district": "Gaibandha",
            "population": 437268
        },
        {
            "division": "Rangpur",
            "upazila": "Gobindaganj",
            "district": "Gaibandha",
            "population": 514696
        },
        {
            "division": "Rangpur",
            "upazila": "Palashbari",
            "district": "Gaibandha",
            "population": 244792
        },
        {
            "division": "Rangpur",
            "upazila": "Sadullapur",
            "district": "Gaibandha",
            "population": 287426
        },
        {
            "division": "Rangpur",
            "upazila": "Saghata",
            "district": "Gaibandha",
            "population": 267819
        },
        {
            "division": "Rangpur",
            "upazila": "Sundarganj",
            "district": "Gaibandha",
            "population": 461920
        },
        {
            "division": "Rangpur",
            "upazila": "Bhurungamari",
            "district": "Kurigram",
            "population": 231538
        },
        {
            "division": "Rangpur",
            "upazila": "Char Rajibpur",
            "district": "Kurigram",
            "population": 73373
        },
        {
            "division": "Rangpur",
            "upazila": "Chilmari",
            "district": "Kurigram",
            "population": 122841
        },
        {
            "division": "Rangpur",
            "upazila": "Phulbari",
            "district": "Kurigram",
            "population": 160250
        },
        {
            "division": "Rangpur",
            "upazila": "Kurigram",
            "district": "Kurigram",
            "population": 312408
        },
        {
            "division": "Rangpur",
            "upazila": "Nageshwari",
            "district": "Kurigram",
            "population": 394258
        },
        {
            "division": "Rangpur",
            "upazila": "Rajarhat",
            "district": "Kurigram",
            "population": 182981
        },
        {
            "division": "Rangpur",
            "upazila": "Raumari",
            "district": "Kurigram",
            "population": 196417
        },
        {
            "division": "Rangpur",
            "upazila": "Ulipur",
            "district": "Kurigram",
            "population": 395207
        },
        {
            "division": "Rangpur",
            "upazila": "Aditmari",
            "district": "Lalmonirhat",
            "population": 224796
        },
        {
            "division": "Rangpur",
            "upazila": "Hatibandha",
            "district": "Lalmonirhat",
            "population": 233927
        },
        {
            "division": "Rangpur",
            "upazila": "Kaliganj",
            "district": "Lalmonirhat",
            "population": 245595
        },
        {
            "division": "Rangpur",
            "upazila": "Lalmonirhat",
            "district": "Lalmonirhat",
            "population": 333166
        },
        {
            "division": "Rangpur",
            "upazila": "Patgram",
            "district": "Lalmonirhat",
            "population": 218615
        },
        {
            "division": "Rangpur",
            "upazila": "Dimla",
            "district": "Nilphamari",
            "population": 283438
        },
        {
            "division": "Rangpur",
            "upazila": "Domar",
            "district": "Nilphamari",
            "population": 249429
        },
        {
            "division": "Rangpur",
            "upazila": "Jaldhaka",
            "district": "Nilphamari",
            "population": 340672
        },
        {
            "division": "Rangpur",
            "upazila": "Kishoreganj",
            "district": "Nilphamari",
            "population": 261069
        },
        {
            "division": "Rangpur",
            "upazila": "Nilphamari",
            "district": "Nilphamari",
            "population": 435162
        },
        {
            "division": "Rangpur",
            "upazila": "Saidpur",
            "district": "Nilphamari",
            "population": 264461
        },
        {
            "division": "Rangpur",
            "upazila": "Atwari",
            "district": "Panchagarh",
            "population": 133650
        },
        {
            "division": "Rangpur",
            "upazila": "Boda",
            "district": "Panchagarh",
            "population": 232124
        },
        {
            "division": "Rangpur",
            "upazila": "Debiganj",
            "district": "Panchagarh",
            "population": 224709
        },
        {
            "division": "Rangpur",
            "upazila": "Panchagarh",
            "district": "Panchagarh",
            "population": 271707
        },
        {
            "division": "Rangpur",
            "upazila": "Tentulia",
            "district": "Panchagarh",
            "population": 125454
        },
        {
            "division": "Rangpur",
            "upazila": "Badarganj",
            "district": "Rangpur",
            "population": 287746
        },
        {
            "division": "Rangpur",
            "upazila": "Gangachara",
            "district": "Rangpur",
            "population": 297869
        },
        {
            "division": "Rangpur",
            "upazila": "Kaunia",
            "district": "Rangpur",
            "population": 227805
        },
        {
            "division": "Rangpur",
            "upazila": "Rangpur",
            "district": "Rangpur",
            "population": 718203
        },
        {
            "division": "Rangpur",
            "upazila": "Mitha pukur",
            "district": "Rangpur",
            "population": 508133
        },
        {
            "division": "Rangpur",
            "upazila": "Pirgachha",
            "district": "Rangpur",
            "population": 313319
        },
        {
            "division": "Rangpur",
            "upazila": "Pirganj",
            "district": "Rangpur",
            "population": 385499
        },
        {
            "division": "Rangpur",
            "upazila": "Taraganj",
            "district": "Rangpur",
            "population": 142512
        },
        {
            "division": "Rangpur",
            "upazila": "Baliadangi",
            "district": "Thakurgaon",
            "population": 195049
        },
        {
            "division": "Rangpur",
            "upazila": "Haripur",
            "district": "Thakurgaon",
            "population": 147947
        },
        {
            "division": "Rangpur",
            "upazila": "Pirganj",
            "district": "Thakurgaon",
            "population": 243535
        },
        {
            "division": "Rangpur",
            "upazila": "Ranisankail",
            "district": "Thakurgaon",
            "population": 222284
        },
        {
            "division": "Rangpur",
            "upazila": "Thakurgaon",
            "district": "Thakurgaon",
            "population": 581227
        },
        {
            "division": "Sylhet",
            "upazila": "Ajmiriganj",
            "district": "Habiganj",
            "population": 114265
        },
        {
            "division": "Sylhet",
            "upazila": "Bahubal",
            "district": "Habiganj",
            "population": 197997
        },
        {
            "division": "Sylhet",
            "upazila": "Baniachong",
            "district": "Habiganj",
            "population": 332530
        },
        {
            "division": "Sylhet",
            "upazila": "Chunarughat",
            "district": "Habiganj",
            "population": 302110
        },
        {
            "division": "Sylhet",
            "upazila": "Habiganj",
            "district": "Habiganj",
            "population": 329093
        },
        {
            "division": "Sylhet",
            "upazila": "Lakhai",
            "district": "Habiganj",
            "population": 148811
        },
        {
            "division": "Sylhet",
            "upazila": "Madhabpur",
            "district": "Habiganj",
            "population": 319016
        },
        {
            "division": "Sylhet",
            "upazila": "Nabiganj",
            "district": "Habiganj",
            "population": 345179
        },
        {
            "division": "Sylhet",
            "upazila": "Barlekha",
            "district": "Maulvibazar",
            "population": 257620
        },
        {
            "division": "Sylhet",
            "upazila": "Juri",
            "district": "Maulvibazar",
            "population": 148958
        },
        {
            "division": "Sylhet",
            "upazila": "Kamalganj",
            "district": "Maulvibazar",
            "population": 259130
        },
        {
            "division": "Sylhet",
            "upazila": "Kulaura",
            "district": "Maulvibazar",
            "population": 360195
        },
        {
            "division": "Sylhet",
            "upazila": "Maulvibazar",
            "district": "Maulvibazar",
            "population": 342468
        },
        {
            "division": "Sylhet",
            "upazila": "Rajnagar",
            "district": "Maulvibazar",
            "population": 232666
        },
        {
            "division": "Sylhet",
            "upazila": "Sreemangal",
            "district": "Maulvibazar",
            "population": 318025
        },
        {
            "division": "Sylhet",
            "upazila": "Bishwambarpur",
            "district": "Sunamganj",
            "population": 156381
        },
        {
            "division": "Sylhet",
            "upazila": "Chhatak",
            "district": "Sunamganj",
            "population": 397642
        },
        {
            "division": "Sylhet",
            "upazila": "Dakshin Sunamganj",
            "district": "Sunamganj",
            "population": 183881
        },
        {
            "division": "Sylhet",
            "upazila": "Derai",
            "district": "Sunamganj",
            "population": 243690
        },
        {
            "division": "Sylhet",
            "upazila": "Dharampasha",
            "district": "Sunamganj",
            "population": 223202
        },
        {
            "division": "Sylhet",
            "upazila": "Dowarabazar",
            "district": "Sunamganj",
            "population": 228460
        },
        {
            "division": "Sylhet",
            "upazila": "Jagannathpur",
            "district": "Sunamganj",
            "population": 259490
        },
        {
            "division": "Sylhet",
            "upazila": "Jamalganj",
            "district": "Sunamganj",
            "population": 167260
        },
        {
            "division": "Sylhet",
            "upazila": "Sulla",
            "district": "Sunamganj",
            "population": 113743
        },
        {
            "division": "Sylhet",
            "upazila": "Sunamganj",
            "district": "Sunamganj",
            "population": 279019
        },
        {
            "division": "Sylhet",
            "upazila": "Tahirpur",
            "district": "Sunamganj",
            "population": 215200
        },
        {
            "division": "Sylhet",
            "upazila": "Balaganj",
            "district": "Sylhet",
            "population": 320227
        },
        {
            "division": "Sylhet",
            "upazila": "Beani Bazar",
            "district": "Sylhet",
            "population": 253616
        },
        {
            "division": "Sylhet",
            "upazila": "Bishwanath",
            "district": "Sylhet",
            "population": 232573
        },
        {
            "division": "Sylhet",
            "upazila": "Companiganj",
            "district": "Sylhet",
            "population": 174029
        },
        {
            "division": "Sylhet",
            "upazila": "Dakshin Surma",
            "district": "Sylhet",
            "population": 253388
        },
        {
            "division": "Sylhet",
            "upazila": "Fenchuganj",
            "district": "Sylhet",
            "population": 104741
        },
        {
            "division": "Sylhet",
            "upazila": "Golapganj",
            "district": "Sylhet",
            "population": 316149
        },
        {
            "division": "Sylhet",
            "upazila": "Gowainghat",
            "district": "Sylhet",
            "population": 287512
        },
        {
            "division": "Sylhet",
            "upazila": "Jaintiapur",
            "district": "Sylhet",
            "population": 161744
        },
        {
            "division": "Sylhet",
            "upazila": "Kanaighat",
            "district": "Sylhet",
            "population": 263969
        },
        {
            "division": "Sylhet",
            "upazila": "Sylhet",
            "district": "Sylhet",
            "population": 829103
        },
        {
            "division": "Sylhet",
            "upazila": "Zakiganj",
            "district": "Sylhet",
            "population": 237137
        }
    ]

    for item in population:
        collection.insert(item)


def parsePoverty():
    poverty = [
        {
            "upazilla": "Bagerhat",
            "poverty": "35.9",
            "district": "Bagerhat"
        },
        {
            "upazilla": "Chitalmari",
            "poverty": "50",
            "district": "Bagerhat"
        },
        {
            "upazilla": "Fakirhat",
            "poverty": "36.4",
            "district": "Bagerhat"
        },
        {
            "upazilla": "Kachua",
            "poverty": "42.5",
            "district": "Bagerhat"
        },
        {
            "upazilla": "MollaHat",
            "poverty": "46.1",
            "district": "Bagerhat"
        },
        {
            "upazilla": "Mongla",
            "poverty": "41.9",
            "district": "Bagerhat"
        },
        {
            "upazilla": "Morrelganj",
            "poverty": "46.5",
            "district": "Bagerhat"
        },
        {
            "upazilla": "Rampal",
            "poverty": "41.1",
            "district": "Bagerhat"
        },
        {
            "upazilla": "Sarankhola",
            "poverty": "48",
            "district": "Bagerhat"
        },
        {
            "upazilla": "Alikadam",
            "poverty": "42.9",
            "district": "Bandarban"
        },
        {
            "upazilla": "Bandarban",
            "poverty": "30.8",
            "district": "Bandarban"
        },
        {
            "upazilla": "Lama",
            "poverty": "41",
            "district": "Bandarban"
        },
        {
            "upazilla": "Naikhongahhari",
            "poverty": "46",
            "district": "Bandarban"
        },
        {
            "upazilla": "Rowangahhari",
            "poverty": "32.9",
            "district": "Bandarban"
        },
        {
            "upazilla": "Ruma",
            "poverty": "42.3",
            "district": "Bandarban"
        },
        {
            "upazilla": "Thanchi ",
            "poverty": "53",
            "district": "Bandarban"
        },
        {
            "upazilla": "Amtali",
            "poverty": "22.8",
            "district": "Barguna"
        },
        {
            "upazilla": "Bamina",
            "poverty": "17.1",
            "district": "Barguna"
        },
        {
            "upazilla": "Barguna",
            "poverty": "19.2",
            "district": "Barguna"
        },
        {
            "upazilla": "Betagi",
            "poverty": "19.6",
            "district": "Barguna"
        },
        {
            "upazilla": "Patharghata",
            "poverty": "12.9",
            "district": "Barguna"
        },
        {
            "upazilla": "Agailjhara",
            "poverty": "51.1",
            "district": "Barisal"
        },
        {
            "upazilla": "Babuganj",
            "poverty": "48.7",
            "district": "Barisal"
        },
        {
            "upazilla": "Bakerganj",
            "poverty": "55.4",
            "district": "Barisal"
        },
        {
            "upazilla": "Banari para ",
            "poverty": "52.2",
            "district": "Barisal"
        },
        {
            "upazilla": "Gaurnade",
            "poverty": "55.5",
            "district": "Barisal"
        },
        {
            "upazilla": "Hizla",
            "poverty": "62.3",
            "district": "Barisal"
        },
        {
            "upazilla": "Barisal",
            "poverty": "49.9",
            "district": "Barisal"
        },
        {
            "upazilla": "Mhendiganj",
            "poverty": "64.4",
            "district": "Barisal"
        },
        {
            "upazilla": "Muladi",
            "poverty": "58.2",
            "district": "Barisal"
        },
        {
            "upazilla": "Wazirpur",
            "poverty": "52.1",
            "district": "Barisal"
        },
        {
            "upazilla": "Bhola",
            "poverty": "42.2",
            "district": "Bhola"
        },
        {
            "upazilla": "Burhanuddin",
            "poverty": "28.3",
            "district": "Bhola"
        },
        {
            "upazilla": "Oharfasson",
            "poverty": "28.2",
            "district": "Bhola"
        },
        {
            "upazilla": "Daulatkhan",
            "poverty": "30.3",
            "district": "Bhola"
        },
        {
            "upazilla": "Lalmohan",
            "poverty": "27.8",
            "district": "Bhola"
        },
        {
            "upazilla": "Manpura",
            "poverty": "32.8",
            "district": "Bhola"
        },
        {
            "upazilla": "Tazumuddin",
            "poverty": "22.3",
            "district": "Bhola"
        },
        {
            "upazilla": "Adamdighi",
            "poverty": "13.1",
            "district": "Bogra"
        },
        {
            "upazilla": "Bogra",
            "poverty": "17.6",
            "district": "Bogra"
        },
        {
            "upazilla": "Dhunat",
            "poverty": "19.8",
            "district": "Bogra"
        },
        {
            "upazilla": "Dhupahanahia",
            "poverty": "13.2",
            "district": "Bogra"
        },
        {
            "upazilla": "Gabtali",
            "poverty": "15.6",
            "district": "Bogra"
        },
        {
            "upazilla": "Kahaloo",
            "poverty": "1107",
            "district": "Bogra"
        },
        {
            "upazilla": "Nandigram",
            "poverty": "16.1",
            "district": "Bogra"
        },
        {
            "upazilla": "Sariakandi",
            "poverty": "21.6",
            "district": "Bogra"
        },
        {
            "upazilla": "Shajahanpur",
            "poverty": "12.5",
            "district": "Bogra"
        },
        {
            "upazilla": "Sherpur",
            "poverty": "15.7",
            "district": "Bogra"
        },
        {
            "upazilla": "Shibganj",
            "poverty": "16.9",
            "district": "Bogra"
        },
        {
            "upazilla": "Sonatola",
            "poverty": "23.7",
            "district": "Bogra"
        },
        {
            "upazilla": "Akhaura",
            "poverty": "26.7",
            "district": "Brahmanbaria "
        },
        {
            "upazilla": "Banohharampur",
            "poverty": "27.3",
            "district": "Brahmanbaria "
        },
        {
            "upazilla": "Bijoynagar",
            "poverty": "35.8",
            "district": "Brahmanbaria "
        },
        {
            "upazilla": "Brahmanbaria",
            "poverty": "26",
            "district": "Brahmanbaria "
        },
        {
            "upazilla": "Ashuganj",
            "poverty": "21.8",
            "district": "Brahmanbaria "
        },
        {
            "upazilla": "Kasba",
            "poverty": "25.5",
            "district": "Brahmanbaria "
        },
        {
            "upazilla": "Nabinagar",
            "poverty": "30.5",
            "district": "Brahmanbaria "
        },
        {
            "upazilla": "Nasrnagar",
            "poverty": "43.7",
            "district": "Brahmanbaria "
        },
        {
            "upazilla": "Sarail",
            "poverty": "31.1",
            "district": "Brahmanbaria "
        },
        {
            "upazilla": "Chandpur",
            "poverty": "45.5",
            "district": "Chandpur"
        },
        {
            "upazilla": "Faridganj",
            "poverty": "46.6",
            "district": "Chandpur"
        },
        {
            "upazilla": "Haim ohar",
            "poverty": "61.3",
            "district": "Chandpur"
        },
        {
            "upazilla": "Hajganj",
            "poverty": "53.7",
            "district": "Chandpur"
        },
        {
            "upazilla": "Kaqhur",
            "poverty": "56.3",
            "district": "Chandpur"
        },
        {
            "upazilla": "Matlabdakshin",
            "poverty": "53.7",
            "district": "Chandpur"
        },
        {
            "upazilla": "Matlabuttar",
            "poverty": "49.9",
            "district": "Chandpur"
        },
        {
            "upazilla": "Shahrasti",
            "poverty": "50.5",
            "district": "Chandpur"
        },
        {
            "upazilla": "Anowara",
            "poverty": "15.5",
            "district": "Chittagong"
        },
        {
            "upazilla": "Bayejd bostami",
            "poverty": "9.2",
            "district": "Chittagong"
        },
        {
            "upazilla": "Banshkhali",
            "poverty": "27.9",
            "district": "Chittagong"
        },
        {
            "upazilla": "Boalkhali",
            "poverty": "10.5",
            "district": "Chittagong"
        },
        {
            "upazilla": "Chandgaon",
            "poverty": "16.9",
            "district": "Chittagong"
        },
        {
            "upazilla": "Chittagongport",
            "poverty": "12.4",
            "district": "Chittagong"
        },
        {
            "upazilla": "Doublemooring",
            "poverty": "0",
            "district": "Chittagong"
        },
        {
            "upazilla": "Fatikqhhari",
            "poverty": "17.6",
            "district": "Chittagong"
        },
        {
            "upazilla": "Halishahar",
            "poverty": "5.6",
            "district": "Chittagong"
        },
        {
            "upazilla": "Hathazari",
            "poverty": "1.1",
            "district": "Chittagong"
        },
        {
            "upazilla": "Kotwali",
            "poverty": "0.3",
            "district": "Chittagong"
        },
        {
            "upazilla": "Khulshi",
            "poverty": "1.1",
            "district": "Chittagong"
        },
        {
            "upazilla": "Lohagara",
            "poverty": "18.3",
            "district": "Chittagong"
        },
        {
            "upazilla": "Mirsharai",
            "poverty": "13.4",
            "district": "Chittagong"
        },
        {
            "upazilla": "Pahartali",
            "poverty": "30",
            "district": "Chittagong"
        },
        {
            "upazilla": "Panqhlaish",
            "poverty": "0.8",
            "district": "Chittagong"
        },
        {
            "upazilla": "Patiya",
            "poverty": "8.1",
            "district": "Chittagong"
        },
        {
            "upazilla": "Patenga",
            "poverty": "3.9",
            "district": "Chittagong"
        },
        {
            "upazilla": "Ranguna",
            "poverty": "14",
            "district": "Chittagong"
        },
        {
            "upazilla": "Raozan",
            "poverty": "8.5",
            "district": "Chittagong"
        },
        {
            "upazilla": "Sandwip",
            "poverty": "19.1",
            "district": "Chittagong"
        },
        {
            "upazilla": "Satkania ",
            "poverty": "15.2",
            "district": "Chittagong"
        },
        {
            "upazilla": "Sitakunda",
            "poverty": "11.5",
            "district": "Chittagong"
        },
        {
            "upazilla": "Alamdanga",
            "poverty": "26",
            "district": "Chuadanga"
        },
        {
            "upazilla": "Qhuadanga",
            "poverty": "29.2",
            "district": "Chuadanga"
        },
        {
            "upazilla": "Damurhuda",
            "poverty": "27.1",
            "district": "Chuadanga"
        },
        {
            "upazilla": "Jiban nagar",
            "poverty": "29.1",
            "district": "Chuadanga"
        },
        {
            "upazilla": "Barura ",
            "poverty": "37.9",
            "district": "Comilla"
        },
        {
            "upazilla": "Brahman para ",
            "poverty": "39.9",
            "district": "Comilla"
        },
        {
            "upazilla": "Buriqhang",
            "poverty": "33.3",
            "district": "Comilla"
        },
        {
            "upazilla": "Chandina ",
            "poverty": "41.2",
            "district": "Comilla"
        },
        {
            "upazilla": "Chauddagram",
            "poverty": "34.4",
            "district": "Comilla"
        },
        {
            "upazilla": "Comilla Dakshin",
            "poverty": "33.3",
            "district": "Comilla"
        },
        {
            "upazilla": "Daudkandi",
            "poverty": "38.5",
            "district": "Comilla"
        },
        {
            "upazilla": "Debidwar",
            "poverty": "41.4",
            "district": "Comilla"
        },
        {
            "upazilla": "Homna",
            "poverty": "38.3",
            "district": "Comilla"
        },
        {
            "upazilla": "Comilla Adarsha",
            "poverty": "24.4",
            "district": "Comilla"
        },
        {
            "upazilla": "Laksam",
            "poverty": "37.4",
            "district": "Comilla"
        },
        {
            "upazilla": "Manoharganj",
            "poverty": "47.1",
            "district": "Comilla"
        },
        {
            "upazilla": "Meghna",
            "poverty": "37.3",
            "district": "Comilla"
        },
        {
            "upazilla": "Muradnagar",
            "poverty": "45",
            "district": "Comilla"
        },
        {
            "upazilla": "Nangalkot",
            "poverty": "45.1",
            "district": "Comilla"
        },
        {
            "upazilla": "Titas",
            "poverty": "37.7",
            "district": "Comilla"
        },
        {
            "upazilla": "Chakaria",
            "poverty": "28.5",
            "district": "Cox�Sbazar"
        },
        {
            "upazilla": "Cox�sbazar",
            "poverty": "26.2",
            "district": "Cox�Sbazar"
        },
        {
            "upazilla": "Kutubdia",
            "poverty": "31.1",
            "district": "Cox�Sbazar"
        },
        {
            "upazilla": "Maheshkhali",
            "poverty": "40.2",
            "district": "Cox�Sbazar"
        },
        {
            "upazilla": "Pekua",
            "poverty": "30.9",
            "district": "Cox�Sbazar"
        },
        {
            "upazilla": "Ramu",
            "poverty": "34.3",
            "district": "Cox�Sbazar"
        },
        {
            "upazilla": "Teknaf",
            "poverty": "38.2",
            "district": "Cox�Sbazar"
        },
        {
            "upazilla": "Ukhia",
            "poverty": "37.8",
            "district": "Cox�Sbazar"
        },
        {
            "upazilla": "Adabor",
            "poverty": "12.5",
            "district": "Dhaka"
        },
        {
            "upazilla": "Badda",
            "poverty": "13.4",
            "district": "Dhaka"
        },
        {
            "upazilla": "Bangshal",
            "poverty": "9.4",
            "district": "Dhaka"
        },
        {
            "upazilla": "Biman Bandar",
            "poverty": "1.3",
            "district": "Dhaka"
        },
        {
            "upazilla": "Cantonment",
            "poverty": "1.5",
            "district": "Dhaka"
        },
        {
            "upazilla": "Chak Bazar",
            "poverty": "10.7",
            "district": "Dhaka"
        },
        {
            "upazilla": "Dakshnkhan",
            "poverty": "24.6",
            "district": "Dhaka"
        },
        {
            "upazilla": "Darus salam",
            "poverty": "14.2",
            "district": "Dhaka"
        },
        {
            "upazilla": "Demra ",
            "poverty": "19.9",
            "district": "Dhaka"
        },
        {
            "upazilla": "Dhamrai",
            "poverty": "22.8",
            "district": "Dhaka"
        },
        {
            "upazilla": "Dhanmindi",
            "poverty": "1.4",
            "district": "Dhaka"
        },
        {
            "upazilla": "Dohar",
            "poverty": "23.9",
            "district": "Dhaka"
        },
        {
            "upazilla": "Gendaria",
            "poverty": "9.3",
            "district": "Dhaka"
        },
        {
            "upazilla": "Gulshan",
            "poverty": "3.3",
            "district": "Dhaka"
        },
        {
            "upazilla": "Hazaribagh",
            "poverty": "12.2",
            "district": "Dhaka"
        },
        {
            "upazilla": "Jatrabari",
            "poverty": "11.6",
            "district": "Dhaka"
        },
        {
            "upazilla": "Kafrul",
            "poverty": "0.7",
            "district": "Dhaka"
        },
        {
            "upazilla": "Kadamtali",
            "poverty": "15",
            "district": "Dhaka"
        },
        {
            "upazilla": "Kalabagan",
            "poverty": "10.1",
            "district": "Dhaka"
        },
        {
            "upazilla": "Kamrangir Char",
            "poverty": "22",
            "district": "Dhaka"
        },
        {
            "upazilla": "Khilgaon",
            "poverty": "13.7",
            "district": "Dhaka"
        },
        {
            "upazilla": "Khilkhet",
            "poverty": "14.7",
            "district": "Dhaka"
        },
        {
            "upazilla": "Keraniganj",
            "poverty": "25.9",
            "district": "Dhaka"
        },
        {
            "upazilla": "Kotwali",
            "poverty": "5.9",
            "district": "Dhaka"
        },
        {
            "upazilla": "Lalbagh",
            "poverty": "16",
            "district": "Dhaka"
        },
        {
            "upazilla": "Mirpur ",
            "poverty": "6.7",
            "district": "Dhaka"
        },
        {
            "upazilla": "Mohammadpur",
            "poverty": "4",
            "district": "Dhaka"
        },
        {
            "upazilla": "Motijheel",
            "poverty": "1.3",
            "district": "Dhaka"
        },
        {
            "upazilla": "Nawabganj",
            "poverty": "21.1",
            "district": "Dhaka"
        },
        {
            "upazilla": "New market ",
            "poverty": "3.7",
            "district": "Dhaka"
        },
        {
            "upazilla": "Pallabi",
            "poverty": "12",
            "district": "Dhaka"
        },
        {
            "upazilla": "Paltan",
            "poverty": "2.7",
            "district": "Dhaka"
        },
        {
            "upazilla": "Ramna",
            "poverty": "3.8",
            "district": "Dhaka"
        },
        {
            "upazilla": "Rampura",
            "poverty": "10.2",
            "district": "Dhaka"
        },
        {
            "upazilla": "Sabujbagh",
            "poverty": "11.6",
            "district": "Dhaka"
        },
        {
            "upazilla": "Saber",
            "poverty": "34",
            "district": "Dhaka"
        },
        {
            "upazilla": "Shan alu",
            "poverty": "15.7",
            "district": "Dhaka"
        },
        {
            "upazilla": "Shahbagh",
            "poverty": "1.5",
            "district": "Dhaka"
        },
        {
            "upazilla": "Shyampur",
            "poverty": "12.9",
            "district": "Dhaka"
        },
        {
            "upazilla": "Sher-e- Bangla Nagar",
            "poverty": "7.7",
            "district": "Dhaka"
        },
        {
            "upazilla": "Sutapur",
            "poverty": "4.6",
            "district": "Dhaka"
        },
        {
            "upazilla": "Tejgon",
            "poverty": "5.3",
            "district": "Dhaka"
        },
        {
            "upazilla": "Tejgaonind . Area",
            "poverty": "6.7",
            "district": "Dhaka"
        },
        {
            "upazilla": "Turag",
            "poverty": "25.1",
            "district": "Dhaka"
        },
        {
            "upazilla": "Uttara ",
            "poverty": "3.7",
            "district": "Dhaka"
        },
        {
            "upazilla": "Birampur",
            "poverty": "35.9",
            "district": "Dinajpur"
        },
        {
            "upazilla": "Birganj",
            "poverty": "43.1",
            "district": "Dinajpur"
        },
        {
            "upazilla": "Biral",
            "poverty": "38.8",
            "district": "Dinajpur"
        },
        {
            "upazilla": "Bochaganj",
            "poverty": "38.4",
            "district": "Dinajpur"
        },
        {
            "upazilla": "chirrbandar",
            "poverty": "38.5",
            "district": "Dinajpur"
        },
        {
            "upazilla": "Fulbari",
            "poverty": "33.8",
            "district": "Dinajpur"
        },
        {
            "upazilla": "Ghoraghat",
            "poverty": "41.8",
            "district": "Dinajpur"
        },
        {
            "upazilla": "Hakimpur",
            "poverty": "38.9",
            "district": "Dinajpur"
        },
        {
            "upazilla": "Kaharole",
            "poverty": "44.3",
            "district": "Dinajpur"
        },
        {
            "upazilla": "Khansama",
            "poverty": "46.5",
            "district": "Dinajpur"
        },
        {
            "upazilla": "Danajpur",
            "poverty": "28.2",
            "district": "Dinajpur"
        },
        {
            "upazilla": "Nawabganj",
            "poverty": "37.3",
            "district": "Dinajpur"
        },
        {
            "upazilla": "Parbatipur",
            "poverty": "39.7",
            "district": "Dinajpur"
        },
        {
            "upazilla": "Alfadanga",
            "poverty": "29.9",
            "district": "Faridpur"
        },
        {
            "upazilla": "Bhanga",
            "poverty": "33.5",
            "district": "Faridpur"
        },
        {
            "upazilla": "Boalmari",
            "poverty": "39.3",
            "district": "Faridpur"
        },
        {
            "upazilla": "Charbhiadrasan",
            "poverty": "35.8",
            "district": "Faridpur"
        },
        {
            "upazilla": "Faridpur",
            "poverty": "38.3",
            "district": "Faridpur"
        },
        {
            "upazilla": "Madhulhali",
            "poverty": "30.5",
            "district": "Faridpur"
        },
        {
            "upazilla": "Nagarkanda",
            "poverty": "35.9",
            "district": "Faridpur"
        },
        {
            "upazilla": "Sadarpur",
            "poverty": "36.9",
            "district": "Faridpur"
        },
        {
            "upazilla": "Saltha",
            "poverty": "42.1",
            "district": "Faridpur"
        },
        {
            "upazilla": "Chhagalnaiya",
            "poverty": "25.9",
            "district": "Fani"
        },
        {
            "upazilla": "Daganbhuyan",
            "poverty": "16.3",
            "district": "Fani"
        },
        {
            "upazilla": "Feni",
            "poverty": "18.6",
            "district": "Fani"
        },
        {
            "upazilla": "Fulgazi",
            "poverty": "31.8",
            "district": "Fani"
        },
        {
            "upazilla": "Parshuram",
            "poverty": "30.6",
            "district": "Fani"
        },
        {
            "upazilla": "Sonagazi",
            "poverty": "44.5",
            "district": "Fani"
        },
        {
            "upazilla": "Fulchhari",
            "poverty": "58.1",
            "district": "Gaibandha"
        },
        {
            "upazilla": "Gaibandha",
            "poverty": "44.8",
            "district": "Gaibandha"
        },
        {
            "upazilla": "Gobindaganj",
            "poverty": "45.4",
            "district": "Gaibandha"
        },
        {
            "upazilla": "Palashbari",
            "poverty": "44.8",
            "district": "Gaibandha"
        },
        {
            "upazilla": "Sadullapur",
            "poverty": "51",
            "district": "Gaibandha"
        },
        {
            "upazilla": "Saghata",
            "poverty": "52.8",
            "district": "Gaibandha"
        },
        {
            "upazilla": "Sundarganj",
            "poverty": "47.6",
            "district": "Gaibandha"
        },
        {
            "upazilla": "Gazipur",
            "poverty": "22.1",
            "district": "Gazipur"
        },
        {
            "upazilla": "Kaliakair",
            "poverty": "11",
            "district": "Gazipur"
        },
        {
            "upazilla": "Kaluganj",
            "poverty": "15.7",
            "district": "Gazipur"
        },
        {
            "upazilla": " Kapasia ",
            "poverty": "27",
            "district": "Gazipur"
        },
        {
            "upazilla": "Sreepur",
            "poverty": "14.4",
            "district": "Gazipur"
        },
        {
            "upazilla": "Gopalganjsadar",
            "poverty": "41.1",
            "district": "Gopalganj"
        },
        {
            "upazilla": "Kashiani",
            "poverty": "39.1",
            "district": "Gopalganj"
        },
        {
            "upazilla": "Kotalipara",
            "poverty": "43.6",
            "district": "Gopalganj"
        },
        {
            "upazilla": "Muksudpur",
            "poverty": "46.5",
            "district": "Gopalganj"
        },
        {
            "upazilla": "Tungipara",
            "poverty": "42.6",
            "district": "Gopalganj"
        },
        {
            "upazilla": "Ajmiriganj",
            "poverty": "32.6",
            "district": "Habiganj"
        },
        {
            "upazilla": "Bahubal",
            "poverty": "24.1",
            "district": "Habiganj"
        },
        {
            "upazilla": "Baniachong",
            "poverty": "27.6",
            "district": "Habiganj"
        },
        {
            "upazilla": "Chunarughat",
            "poverty": "27.5",
            "district": "Habiganj"
        },
        {
            "upazilla": "Habiganj",
            "poverty": "16.9",
            "district": "Habiganj"
        },
        {
            "upazilla": "Lakhai",
            "poverty": "25.5",
            "district": "Habiganj"
        },
        {
            "upazilla": "Madhabpur",
            "poverty": "25.9",
            "district": "Habiganj"
        },
        {
            "upazilla": "Nabiganj",
            "poverty": "26.8",
            "district": "Habiganj"
        },
        {
            "upazilla": "Akkelpur",
            "poverty": "26.9",
            "district": "Joypurhat"
        },
        {
            "upazilla": "Joypurhat",
            "poverty": "26",
            "district": "Joypurhat"
        },
        {
            "upazilla": "Kalai",
            "poverty": "25.6",
            "district": "Joypurhat"
        },
        {
            "upazilla": "Khetlal",
            "poverty": "26.1",
            "district": "Joypurhat"
        },
        {
            "upazilla": "Panchbibi",
            "poverty": "28.3",
            "district": "Joypurhat"
        },
        {
            "upazilla": "Bakshiganj",
            "poverty": "50.4",
            "district": "Jamalpur"
        },
        {
            "upazilla": "Dewanganj",
            "poverty": "58.5",
            "district": "Jamalpur"
        },
        {
            "upazilla": "0",
            "poverty": "0",
            "district": "Jamalpur"
        },
        {
            "upazilla": "Islampur",
            "poverty": "55",
            "district": "Jamalpur"
        },
        {
            "upazilla": "JAMALPURSADAR",
            "poverty": "49",
            "district": "Jamalpur"
        },
        {
            "upazilla": "MADARGANJ",
            "poverty": "55.5",
            "district": "Jamalpur"
        },
        {
            "upazilla": "MELANDAHA",
            "poverty": "47.2",
            "district": "Jamalpur"
        },
        {
            "upazilla": "SARISHABARI ",
            "poverty": "44.7",
            "district": "Jamalpur"
        },
        {
            "upazilla": "ABHAYNAGAR",
            "poverty": "36",
            "district": "Jessore"
        },
        {
            "upazilla": "BAGHERPARA",
            "poverty": "42.5",
            "district": "Jessore"
        },
        {
            "upazilla": "CHAUGACHHA",
            "poverty": "42.8",
            "district": "Jessore"
        },
        {
            "upazilla": "JHIKARGACHHA",
            "poverty": "38.9",
            "district": "Jessore"
        },
        {
            "upazilla": "KESHABPUR",
            "poverty": "42",
            "district": "Jessore"
        },
        {
            "upazilla": "JESSORE",
            "poverty": "35.3",
            "district": "Jessore"
        },
        {
            "upazilla": "MANIRAMPUR",
            "poverty": "40.2",
            "district": "Jessore"
        },
        {
            "upazilla": "SHARSHA",
            "poverty": "40.8",
            "district": "Jessore"
        },
        {
            "upazilla": "JHALOKATI",
            "poverty": "37.7",
            "district": "Jhalokati"
        },
        {
            "upazilla": "KANTHALIA",
            "poverty": "34.2",
            "district": "Jhalokati"
        },
        {
            "upazilla": "NALCHITY",
            "poverty": "46.5",
            "district": "Jhalokati"
        },
        {
            "upazilla": "RAJPUR",
            "poverty": "42",
            "district": "Jhalokati"
        },
        {
            "upazilla": "HARINAKUNDA",
            "poverty": "26",
            "district": "Jhenaidah"
        },
        {
            "upazilla": "JHENAIDAH",
            "poverty": "23.9",
            "district": "Jhenaidah"
        },
        {
            "upazilla": "KALIGANJ",
            "poverty": "24",
            "district": "Jhenaidah"
        },
        {
            "upazilla": "KOTCHANDPUR",
            "poverty": "20.2",
            "district": "Jhenaidah"
        },
        {
            "upazilla": "MAHESHPUR",
            "poverty": "23.6",
            "district": "Jhenaidah"
        },
        {
            "upazilla": "SHAILKUPA",
            "poverty": "28.2",
            "district": "Jhenaidah"
        },
        {
            "upazilla": "DIGHINALA",
            "poverty": "22.5",
            "district": "Khagrachhari"
        },
        {
            "upazilla": "KHAGRACHHARI",
            "poverty": "19.5",
            "district": "Khagrachhari"
        },
        {
            "upazilla": "LAKSHMICHHARI",
            "poverty": "31",
            "district": "Khagrachhari"
        },
        {
            "upazilla": "MAHALCHARI",
            "poverty": "21.4",
            "district": "Khagrachhari"
        },
        {
            "upazilla": "MANIKCHHARI",
            "poverty": "30.1",
            "district": "Khagrachhari"
        },
        {
            "upazilla": "MATIRANGA",
            "poverty": "28.3",
            "district": "Khagrachhari"
        },
        {
            "upazilla": "PANCHHARI",
            "poverty": "23.4",
            "district": "Khagrachhari"
        },
        {
            "upazilla": "RAMGARH",
            "poverty": "32.6",
            "district": "Khagrachhari"
        },
        {
            "upazilla": "BATIAGHATA",
            "poverty": "40.5",
            "district": "Khulna"
        },
        {
            "upazilla": "DACOPE",
            "poverty": "44.5",
            "district": "Khulna"
        },
        {
            "upazilla": "DAULATPUR",
            "poverty": "34.5",
            "district": "Khulna"
        },
        {
            "upazilla": "DUMURIA",
            "poverty": "37.2",
            "district": "Khulna"
        },
        {
            "upazilla": "DIGHALIA",
            "poverty": "39.3",
            "district": "Khulna"
        },
        {
            "upazilla": "KHALISHPUR",
            "poverty": "41.1",
            "district": "Khulna"
        },
        {
            "upazilla": "KHAN JAHAN ALI",
            "poverty": "31.9",
            "district": "Khulna"
        },
        {
            "upazilla": "KHULNA",
            "poverty": "35.5",
            "district": "Khulna"
        },
        {
            "upazilla": "KOYRA",
            "poverty": "49.1",
            "district": "Khulna"
        },
        {
            "upazilla": "PAIKGACHHA",
            "poverty": "42.4",
            "district": "Khulna"
        },
        {
            "upazilla": "PHULTALA",
            "poverty": "33.7",
            "district": "Khulna"
        },
        {
            "upazilla": "RUPSA",
            "poverty": "36.9",
            "district": "Khulna"
        },
        {
            "upazilla": "SONAGANGA",
            "poverty": "19.3",
            "district": "Khulna"
        },
        {
            "upazilla": "TEROKHADA",
            "poverty": "49.6",
            "district": "Khulna"
        },
        {
            "upazilla": "AUSTAGRAM",
            "poverty": "33.7",
            "district": "Kishorgonj"
        },
        {
            "upazilla": "BAJITPUR",
            "poverty": "28.2",
            "district": "Kishorgonj"
        },
        {
            "upazilla": "BHAIRAB",
            "poverty": "33.9",
            "district": "Kishorgonj"
        },
        {
            "upazilla": "HOSSAINPUR",
            "poverty": "33",
            "district": "Kishorgonj"
        },
        {
            "upazilla": "ITNA",
            "poverty": "34.9",
            "district": "Kishorgonj"
        },
        {
            "upazilla": "KARIMGANJ",
            "poverty": "27.1",
            "district": "Kishorgonj"
        },
        {
            "upazilla": "KATIADI",
            "poverty": "31.6",
            "district": "Kishorgonj"
        },
        {
            "upazilla": "KISHOREGANJSADAR",
            "poverty": "27.6",
            "district": "Kishorgonj"
        },
        {
            "upazilla": "KULIARCHAR",
            "poverty": "32.7",
            "district": "Kishorgonj"
        },
        {
            "upazilla": "MITHAMAIN",
            "poverty": "35.2",
            "district": "Kishorgonj"
        },
        {
            "upazilla": "NIKLI",
            "poverty": "30",
            "district": "Kishorgonj"
        },
        {
            "upazilla": "PAKUNDIA",
            "poverty": "26.1",
            "district": "Kishorgonj"
        },
        {
            "upazilla": "TARIL",
            "poverty": "26.1",
            "district": "Kishorgonj"
        },
        {
            "upazilla": "BHURUNGAMARI",
            "poverty": "65.1",
            "district": "Kurigram"
        },
        {
            "upazilla": "CHARRAJIBPUR",
            "poverty": "68.8",
            "district": "Kurigram"
        },
        {
            "upazilla": "CHILMARI",
            "poverty": "61.1",
            "district": "Kurigram"
        },
        {
            "upazilla": "PHULBARI",
            "poverty": "68.5",
            "district": "Kurigram"
        },
        {
            "upazilla": "KURIGRAM",
            "poverty": "58",
            "district": "Kurigram"
        },
        {
            "upazilla": "NAGSHWARI",
            "poverty": "65",
            "district": "Kurigram"
        },
        {
            "upazilla": "RAJARHAT",
            "poverty": "67.7",
            "district": "Kurigram"
        },
        {
            "upazilla": "RAUMARI",
            "poverty": "57",
            "district": "Kurigram"
        },
        {
            "upazilla": "ULIPUR",
            "poverty": "65.3",
            "district": "Kurigram"
        },
        {
            "upazilla": "BHERAMARA",
            "poverty": "3.4",
            "district": "Kushtia"
        },
        {
            "upazilla": "DAULATPUR",
            "poverty": "4",
            "district": "Kushtia"
        },
        {
            "upazilla": "KHOKSA",
            "poverty": "4.7",
            "district": "Kushtia"
        },
        {
            "upazilla": "KUMARKHALI",
            "poverty": "4",
            "district": "Kushtia"
        },
        {
            "upazilla": "KUSHTIA",
            "poverty": "3",
            "district": "Kushtia"
        },
        {
            "upazilla": "MIRPUR",
            "poverty": "3.3",
            "district": "Kushtia"
        },
        {
            "upazilla": "KAMALNAGAR",
            "poverty": "18.7",
            "district": "Lakshmipur"
        },
        {
            "upazilla": "LAKSHMIPURSADAR",
            "poverty": "45.6",
            "district": "Lakshmipur"
        },
        {
            "upazilla": "ROYPUR",
            "poverty": "16.7",
            "district": "Lakshmipur"
        },
        {
            "upazilla": "RAMGANJ",
            "poverty": "21.4",
            "district": "Lakshmipur"
        },
        {
            "upazilla": "RAMGATI",
            "poverty": "30.4",
            "district": "Lakshmipur"
        },
        {
            "upazilla": "ADITMARI",
            "poverty": "36",
            "district": "Lalmonirhat"
        },
        {
            "upazilla": "HATIBANDHA",
            "poverty": "38.1",
            "district": "Lalmonirhat"
        },
        {
            "upazilla": "KALIGANJ",
            "poverty": "35.3",
            "district": "Lalmonirhat"
        },
        {
            "upazilla": "LALMONIRHAT",
            "poverty": "31.3",
            "district": "Lalmonirhat"
        },
        {
            "upazilla": "PATGRAM",
            "poverty": "33.3",
            "district": "Lalmonirhat"
        },
        {
            "upazilla": "KALKINI",
            "poverty": "33.2",
            "district": "Madaripur"
        },
        {
            "upazilla": "MADARIPUR",
            "poverty": "35",
            "district": "Madaripur"
        },
        {
            "upazilla": "RAJOIR",
            "poverty": "31.4",
            "district": "Madaripur"
        },
        {
            "upazilla": "SHIBCHAR",
            "poverty": "38.8",
            "district": "Madaripur"
        },
        {
            "upazilla": "MAGURA",
            "poverty": "43",
            "district": "Magura"
        },
        {
            "upazilla": "MOHAMMADPUR",
            "poverty": "50.8",
            "district": "Magura"
        },
        {
            "upazilla": "SHALIKHA",
            "poverty": "44.2",
            "district": "Magura"
        },
        {
            "upazilla": "SREEPUR",
            "poverty": "45",
            "district": "Magura"
        },
        {
            "upazilla": "DAULATPUR",
            "poverty": "29.4",
            "district": "Manikganj"
        },
        {
            "upazilla": "GHIOR",
            "poverty": "13.7",
            "district": "Manikganj"
        },
        {
            "upazilla": "HAIRAMPUR",
            "poverty": "18.1",
            "district": "Manikganj"
        },
        {
            "upazilla": "MANIKGANJ",
            "poverty": "18.7",
            "district": "Manikganj"
        },
        {
            "upazilla": "SATURIA",
            "poverty": "15",
            "district": "Manikganj"
        },
        {
            "upazilla": "SHIBALAYA",
            "poverty": "15.8",
            "district": "Manikganj"
        },
        {
            "upazilla": "NINGAIR",
            "poverty": "18.1",
            "district": "Manikganj"
        },
        {
            "upazilla": "GANGNI",
            "poverty": "15.8",
            "district": "Meherpur"
        },
        {
            "upazilla": "MUJIBNAGAR",
            "poverty": "13.6",
            "district": "Meherpur"
        },
        {
            "upazilla": "MEHERPUR",
            "poverty": "15.1",
            "district": "Meherpur"
        },
        {
            "upazilla": "BARLEKHA",
            "poverty": "25.7",
            "district": "Maulvibazar"
        },
        {
            "upazilla": "JURI",
            "poverty": "36.3",
            "district": "Maulvibazar"
        },
        {
            "upazilla": "KAMALGANJ",
            "poverty": "25.7",
            "district": "Maulvibazar"
        },
        {
            "upazilla": "KULAURA",
            "poverty": "28.1",
            "district": "Maulvibazar"
        },
        {
            "upazilla": "MAULVIBAZARSADAR",
            "poverty": "16.7",
            "district": "Maulvibazar"
        },
        {
            "upazilla": "RAJNAGAR",
            "poverty": "22.3",
            "district": "Maulvibazar"
        },
        {
            "upazilla": "SREEMANGAL",
            "poverty": "29.3",
            "district": "Maulvibazar"
        },
        {
            "upazilla": "GAZARIA",
            "poverty": "26.8",
            "district": "Munshiganj"
        },
        {
            "upazilla": "LOHAJANG",
            "poverty": "33.6",
            "district": "Munshiganj"
        },
        {
            "upazilla": "MUNSHIGAN",
            "poverty": "30.8",
            "district": "Munshiganj"
        },
        {
            "upazilla": "SERAJDIKHAN",
            "poverty": "28.8",
            "district": "Munshiganj"
        },
        {
            "upazilla": "SREENAGAR",
            "poverty": "26.3",
            "district": "Munshiganj"
        },
        {
            "upazilla": "TONGIBARI",
            "poverty": "25.1",
            "district": "Munshiganj"
        },
        {
            "upazilla": "BHALUKA",
            "poverty": "31.1",
            "district": "Mymensingh"
        },
        {
            "upazilla": "DHOBAURA",
            "poverty": "58.2",
            "district": "Mymensingh"
        },
        {
            "upazilla": "FULBARIA",
            "poverty": "52.6",
            "district": "Mymensingh"
        },
        {
            "upazilla": "GAFFARGAON",
            "poverty": "43.9",
            "district": "Mymensingh"
        },
        {
            "upazilla": "GAURIPUR",
            "poverty": "50.6",
            "district": "Mymensingh"
        },
        {
            "upazilla": "HALUAGHAT",
            "poverty": "50.3",
            "district": "Mymensingh"
        },
        {
            "upazilla": "ISHWARGANJ",
            "poverty": "56",
            "district": "Mymensingh"
        },
        {
            "upazilla": "MYMENSINGHSADAR",
            "poverty": "52.3",
            "district": "Mymensingh"
        },
        {
            "upazilla": "MUKTAGACHHA",
            "poverty": "43.3",
            "district": "Mymensingh"
        },
        {
            "upazilla": "NANDAIL",
            "poverty": "60.7",
            "district": "Mymensingh"
        },
        {
            "upazilla": "PHULPUR",
            "poverty": "58.8",
            "district": "Mymensingh"
        },
        {
            "upazilla": "TRISHAL",
            "poverty": "47.8",
            "district": "Mymensingh"
        },
        {
            "upazilla": "ATRAI",
            "poverty": "13.5",
            "district": "Naogaon"
        },
        {
            "upazilla": "BADALDACHHI",
            "poverty": "15",
            "district": "Naogaon"
        },
        {
            "upazilla": "DHAMOIRHAT",
            "poverty": "17.9",
            "district": "Naogaon"
        },
        {
            "upazilla": "MANDA",
            "poverty": "14.7",
            "district": "Naogaon"
        },
        {
            "upazilla": "MAHADEBPUR",
            "poverty": "15.6",
            "district": "Naogaon"
        },
        {
            "upazilla": "NAOGAON",
            "poverty": "17.4",
            "district": "Naogaon"
        },
        {
            "upazilla": "NIAMATPUR",
            "poverty": "19.4",
            "district": "Naogaon"
        },
        {
            "upazilla": "PATNITALA",
            "poverty": "18.6",
            "district": "Naogaon"
        },
        {
            "upazilla": "PORSHA",
            "poverty": "21.7",
            "district": "Naogaon"
        },
        {
            "upazilla": "RANINAGAR",
            "poverty": "13.3",
            "district": "Naogaon"
        },
        {
            "upazilla": "SAPAHAR",
            "poverty": "21.4",
            "district": "Naogaon"
        },
        {
            "upazilla": "KALIA",
            "poverty": "23.3",
            "district": "Narail"
        },
        {
            "upazilla": "LOHAGARA",
            "poverty": "19.9",
            "district": "Narail"
        },
        {
            "upazilla": "NARAIL",
            "poverty": "17.3",
            "district": "Narail"
        },
        {
            "upazilla": "ARAIHAZAR",
            "poverty": "34.4",
            "district": "Narayanganj"
        },
        {
            "upazilla": "SONARGAON",
            "poverty": "21.3",
            "district": "Narayanganj"
        },
        {
            "upazilla": "BANDAR",
            "poverty": "20.9",
            "district": "Narayanganj"
        },
        {
            "upazilla": "NARAYANGANJ",
            "poverty": "27.9",
            "district": "Narayanganj"
        },
        {
            "upazilla": "RUPGANJ",
            "poverty": "22.5",
            "district": "Narayanganj"
        },
        {
            "upazilla": "BELABO",
            "poverty": "21.9",
            "district": "Narsingdi"
        },
        {
            "upazilla": "MANOHARDI",
            "poverty": "22.7",
            "district": "Narsingdi"
        },
        {
            "upazilla": "NARSINGDI",
            "poverty": "22.8",
            "district": "Narsingdi"
        },
        {
            "upazilla": "PALASH",
            "poverty": "22.2",
            "district": "Narsingdi"
        },
        {
            "upazilla": "ROYPURA",
            "poverty": "29.4",
            "district": "Narsingdi"
        },
        {
            "upazilla": "SHIBPUR",
            "poverty": "18.9",
            "district": "Narsingdi"
        },
        {
            "upazilla": "BAGATUOARA",
            "poverty": "31.6",
            "district": "Natore"
        },
        {
            "upazilla": "BARAIGRAM",
            "poverty": "36.1",
            "district": "Natore"
        },
        {
            "upazilla": "GURUDASPUR",
            "poverty": "37",
            "district": "Natore"
        },
        {
            "upazilla": "LALPUR",
            "poverty": "35.7",
            "district": "Natore"
        },
        {
            "upazilla": "NATORE",
            "poverty": "31.8",
            "district": "Natore"
        },
        {
            "upazilla": "SINGRA",
            "poverty": "37.8",
            "district": "Natore"
        },
        {
            "upazilla": "BHOLAHAT",
            "poverty": "20.8",
            "district": "Nawabganj"
        },
        {
            "upazilla": "GOMASTAPUR",
            "poverty": "26.1",
            "district": "Nawabganj"
        },
        {
            "upazilla": "NACHOLE",
            "poverty": "24.2",
            "district": "Nawabganj"
        },
        {
            "upazilla": "CHAPAI",
            "poverty": "25.4",
            "district": "Nawabganj"
        },
        {
            "upazilla": "SHIBGANJ",
            "poverty": "26",
            "district": "Nawabganj"
        },
        {
            "upazilla": "ATPARA",
            "poverty": "31.6",
            "district": "Netrakona"
        },
        {
            "upazilla": "BARHATTA",
            "poverty": "35.2",
            "district": "Netrakona"
        },
        {
            "upazilla": "DURGAPUR",
            "poverty": "30.2",
            "district": "Netrakona"
        },
        {
            "upazilla": "KHALIAJURI",
            "poverty": "37.2",
            "district": "Netrakona"
        },
        {
            "upazilla": "KALMAKANDA",
            "poverty": "37.6",
            "district": "Netrakona"
        },
        {
            "upazilla": "KENDUA",
            "poverty": "40.9",
            "district": "Netrakona"
        },
        {
            "upazilla": "MADAN",
            "poverty": "41.6",
            "district": "Netrakona"
        },
        {
            "upazilla": "MOHANGANJ",
            "poverty": "34.3",
            "district": "Netrakona"
        },
        {
            "upazilla": "NETROKONA",
            "poverty": "30.8",
            "district": "Netrakona"
        },
        {
            "upazilla": "PURBADHALA",
            "poverty": "35.4",
            "district": "Netrakona"
        },
        {
            "upazilla": "DIMLA",
            "poverty": "35.2",
            "district": "Nilphamari"
        },
        {
            "upazilla": "DOMAR",
            "poverty": "31.3",
            "district": "Nilphamari"
        },
        {
            "upazilla": "JALDHAKA",
            "poverty": "43.5",
            "district": "Nilphamari"
        },
        {
            "upazilla": "KISHOREGANJ",
            "poverty": "30.9",
            "district": "Nilphamari"
        },
        {
            "upazilla": "NILPHAMARI",
            "poverty": "36.4",
            "district": "Nilphamari"
        },
        {
            "upazilla": "SAIDPUR",
            "poverty": "27.7",
            "district": "Nilphamari"
        },
        {
            "upazilla": "BEBEGUMGANJ",
            "poverty": "5.9",
            "district": "Noakhali"
        },
        {
            "upazilla": "CHATKHIL",
            "poverty": "4.8",
            "district": "Noakhali"
        },
        {
            "upazilla": "COMPANIGANJ",
            "poverty": "7.6",
            "district": "Noakhali"
        },
        {
            "upazilla": "HATIYA",
            "poverty": "16",
            "district": "Noakhali"
        },
        {
            "upazilla": "KABIRHAT",
            "poverty": "12.4",
            "district": "Noakhali"
        },
        {
            "upazilla": "SENBAGH",
            "poverty": "5.4",
            "district": "Noakhali"
        },
        {
            "upazilla": "SONAIMURI",
            "poverty": "5",
            "district": "Noakhali"
        },
        {
            "upazilla": "SUBARNACHAR",
            "poverty": "18.7",
            "district": "Noakhali"
        },
        {
            "upazilla": "NOAKHALI",
            "poverty": "10.2",
            "district": "Noakhali"
        },
        {
            "upazilla": "ATGHARIA",
            "poverty": "31.2",
            "district": "Pabna"
        },
        {
            "upazilla": "BERA",
            "poverty": "39.4",
            "district": "Pabna"
        },
        {
            "upazilla": "BHANGURA",
            "poverty": "33.5",
            "district": "Pabna"
        },
        {
            "upazilla": "CHATMOHAR",
            "poverty": "31.4",
            "district": "Pabna"
        },
        {
            "upazilla": "RARIDPUR",
            "poverty": "31.5",
            "district": "Pabna"
        },
        {
            "upazilla": "ISHWARDI",
            "poverty": "26.2",
            "district": "Pabna"
        },
        {
            "upazilla": "PABNA",
            "poverty": "27.8",
            "district": "Pabna"
        },
        {
            "upazilla": "SANTHIA",
            "poverty": "33.1",
            "district": "Pabna"
        },
        {
            "upazilla": "SUJANAGAR",
            "poverty": "35.4",
            "district": "Pabna"
        },
        {
            "upazilla": "ATWARI",
            "poverty": "24.1",
            "district": "Panchagarh"
        },
        {
            "upazilla": "BODA12.0",
            "poverty": "26.6",
            "district": "Panchagarh"
        },
        {
            "upazilla": "DEBIGANJ",
            "poverty": "34.2",
            "district": "Panchagarh"
        },
        {
            "upazilla": "PANCHAGARH",
            "poverty": "24.2",
            "district": "Panchagarh"
        },
        {
            "upazilla": "TENTULIA",
            "poverty": "21.5",
            "district": "Panchagarh"
        },
        {
            "upazilla": "BAUPHAL",
            "poverty": "24",
            "district": "Patuakhali"
        },
        {
            "upazilla": "DASHMINA",
            "poverty": "21.8",
            "district": "Patuakhali"
        },
        {
            "upazilla": "DUMKI",
            "poverty": "22",
            "district": "Patuakhali"
        },
        {
            "upazilla": "GALACHIPA",
            "poverty": "26",
            "district": "Patuakhali"
        },
        {
            "upazilla": "KALAPARA",
            "poverty": "20.3",
            "district": "Patuakhali"
        },
        {
            "upazilla": "MIRZAGANJ",
            "poverty": "17.8",
            "district": "Patuakhali"
        },
        {
            "upazilla": "PATUAKHALI",
            "poverty": "36.9",
            "district": "Patuakhali"
        },
        {
            "upazilla": "BHANDARIA",
            "poverty": "42",
            "district": "Pirojpur"
        },
        {
            "upazilla": "KAWKHALI",
            "poverty": "52.2",
            "district": "Pirojpur"
        },
        {
            "upazilla": "MATHBARIA",
            "poverty": "38",
            "district": "Pirojpur"
        },
        {
            "upazilla": "NAZIRPUR",
            "poverty": "51.5",
            "district": "Pirojpur"
        },
        {
            "upazilla": "PIROJPUR",
            "poverty": "42.7",
            "district": "Pirojpur"
        },
        {
            "upazilla": "NESARABAD(SWARUPKATI",
            "poverty": "43.3",
            "district": "Pirojpur"
        },
        {
            "upazilla": "ZIANAGAR",
            "poverty": "49.1",
            "district": "Pirojpur"
        },
        {
            "upazilla": "BAGHA",
            "poverty": "33.6",
            "district": "Rajshahi"
        },
        {
            "upazilla": "BAGHMARA",
            "poverty": "29.4",
            "district": "Rajshahi"
        },
        {
            "upazilla": "BOALIA",
            "poverty": "24.1",
            "district": "Rajshahi"
        },
        {
            "upazilla": "CHARGHAT",
            "poverty": "31.4",
            "district": "Rajshahi"
        },
        {
            "upazilla": "DURGAPUR",
            "poverty": "25.7",
            "district": "Rajshahi"
        },
        {
            "upazilla": "GODAGARI",
            "poverty": "44.1",
            "district": "Rajshahi"
        },
        {
            "upazilla": "MATIHAR",
            "poverty": "33.3",
            "district": "Rajshahi"
        },
        {
            "upazilla": "MOHANPUR",
            "poverty": "24.9",
            "district": "Rajshahi"
        },
        {
            "upazilla": "PABA",
            "poverty": "33.4",
            "district": "Rajshahi"
        },
        {
            "upazilla": "PUTHIA",
            "poverty": "26.8",
            "district": "Rajshahi"
        },
        {
            "upazilla": "RAJPARA",
            "poverty": "24.4",
            "district": "Rajshahi"
        },
        {
            "upazilla": "SHAHMAKHDUM",
            "poverty": "30.9",
            "district": "Rajshahi"
        },
        {
            "upazilla": "TANORE",
            "poverty": "35.7",
            "district": "Rajshahi"
        },
        {
            "upazilla": "BALIAKANDI",
            "poverty": "39.7",
            "district": "Rajbari"
        },
        {
            "upazilla": "GOALANDA",
            "poverty": "50.5",
            "district": "Rajbari"
        },
        {
            "upazilla": "KALUKHALI",
            "poverty": "39.6",
            "district": "Rajbari"
        },
        {
            "upazilla": "PANGSHA",
            "poverty": "45.7",
            "district": "Rajbari"
        },
        {
            "upazilla": "RAJBARI",
            "poverty": "38.7",
            "district": "Rajbari"
        },
        {
            "upazilla": "BAGHAICHHARI",
            "poverty": "24.8",
            "district": "Rangamati"
        },
        {
            "upazilla": "BARKAL",
            "poverty": "26.1",
            "district": "Rangamati"
        },
        {
            "upazilla": "KAWKHALI(BETBUNIA)",
            "poverty": "23.4",
            "district": "Rangamati"
        },
        {
            "upazilla": "0",
            "poverty": "0",
            "district": "Rangamati"
        },
        {
            "upazilla": "Belai Chhari",
            "poverty": "34.7",
            "district": "Rangamati"
        },
        {
            "upazilla": "Kaptal",
            "poverty": "12.2",
            "district": "Rangamati"
        },
        {
            "upazilla": "Jurai Chhaari",
            "poverty": "19.3",
            "district": "Rangamati"
        },
        {
            "upazilla": "Langadu",
            "poverty": "29.3",
            "district": "Rangamati"
        },
        {
            "upazilla": "Naniarchar",
            "poverty": "21.2",
            "district": "Rangamati"
        },
        {
            "upazilla": "Rahasthali",
            "poverty": "20.5",
            "district": "Rangamati"
        },
        {
            "upazilla": "Rangamati",
            "poverty": "7.3",
            "district": "Rangamati"
        },
        {
            "upazilla": "Badarganj",
            "poverty": "48.3",
            "district": "Rangpur"
        },
        {
            "upazilla": "Gangachara",
            "poverty": "58.3",
            "district": "Rangpur"
        },
        {
            "upazilla": "Kaunia",
            "poverty": "45",
            "district": "Rangpur"
        },
        {
            "upazilla": "Rangpur",
            "poverty": "37.1",
            "district": "Rangpur"
        },
        {
            "upazilla": "Mitha Pukur",
            "poverty": "45",
            "district": "Rangpur"
        },
        {
            "upazilla": "Pirgachha",
            "poverty": "49",
            "district": "Rangpur"
        },
        {
            "upazilla": "Pirganj",
            "poverty": "46.9",
            "district": "Rangpur"
        },
        {
            "upazilla": "Taraganj ",
            "poverty": "52.4",
            "district": "Rangpur"
        },
        {
            "upazilla": "Bhedarganj",
            "poverty": "56.3",
            "district": "Shariatpur"
        },
        {
            "upazilla": "Damudya",
            "poverty": "47.9",
            "district": "Shariatpur"
        },
        {
            "upazilla": "Gosairihat",
            "poverty": "58.3",
            "district": "Shariatpur"
        },
        {
            "upazilla": "Naria",
            "poverty": "48.1",
            "district": "Shariatpur"
        },
        {
            "upazilla": "Shariatpur",
            "poverty": "49.8",
            "district": "Shariatpur"
        },
        {
            "upazilla": "Zanjira ",
            "poverty": "54",
            "district": "Shariatpur"
        },
        {
            "upazilla": "Assasuni",
            "poverty": "48.4",
            "district": "Satkhira "
        },
        {
            "upazilla": "Debhata",
            "poverty": "43.1",
            "district": "Satkhira "
        },
        {
            "upazilla": "Kalaroa",
            "poverty": "46",
            "district": "Satkhira "
        },
        {
            "upazilla": "Kaliganj",
            "poverty": "48",
            "district": "Satkhira "
        },
        {
            "upazilla": "Satkhira",
            "poverty": "43.1",
            "district": "Satkhira "
        },
        {
            "upazilla": "Shyamnagar",
            "poverty": "50.2",
            "district": "Satkhira "
        },
        {
            "upazilla": "Tala",
            "poverty": "45.2",
            "district": "Satkhira "
        },
        {
            "upazilla": "Belkuchi",
            "poverty": "42.5",
            "district": "Sirajganj"
        },
        {
            "upazilla": "Chauhali",
            "poverty": "45.5",
            "district": "Sirajganj"
        },
        {
            "upazilla": "Kamarkhanda",
            "poverty": "32.5",
            "district": "Sirajganj"
        },
        {
            "upazilla": "Kazipur",
            "poverty": "36.2",
            "district": "Sirajganj"
        },
        {
            "upazilla": "Royganj",
            "poverty": "39.4",
            "district": "Sirajganj"
        },
        {
            "upazilla": "Shahjadpur",
            "poverty": "41.1",
            "district": "Sirajganj"
        },
        {
            "upazilla": "Sirajganj",
            "poverty": "36.7",
            "district": "Sirajganj"
        },
        {
            "upazilla": "Tarash",
            "poverty": "35.8",
            "district": "Sirajganj"
        },
        {
            "upazilla": "Ulaah para",
            "poverty": "36.6",
            "district": "Sirajganj"
        },
        {
            "upazilla": "jhnaigati",
            "poverty": "36.9",
            "district": "Sherpur"
        },
        {
            "upazilla": "Nakla",
            "poverty": "46.8",
            "district": "Sherpur"
        },
        {
            "upazilla": "Nalitabari",
            "poverty": "48.1",
            "district": "Sherpur"
        },
        {
            "upazilla": "Sherpur",
            "poverty": "55.8",
            "district": "Sherpur"
        },
        {
            "upazilla": "Sreebardi",
            "poverty": "49.1",
            "district": "Sherpur"
        },
        {
            "upazilla": "Bishwambarpur",
            "poverty": "30.4",
            "district": "Sunamganj"
        },
        {
            "upazilla": "Chhatak",
            "poverty": "23.6",
            "district": "Sunamganj"
        },
        {
            "upazilla": "Dakshin Sunamganj",
            "poverty": "24.4",
            "district": "Sunamganj"
        },
        {
            "upazilla": "Derai",
            "poverty": "26.2",
            "district": "Sunamganj"
        },
        {
            "upazilla": "Dharampasha",
            "poverty": "25.5",
            "district": "Sunamganj"
        },
        {
            "upazilla": "Dowarabazar",
            "poverty": "29.9",
            "district": "Sunamganj"
        },
        {
            "upazilla": "Jagannathpur",
            "poverty": "21",
            "district": "Sunamganj"
        },
        {
            "upazilla": "Jamalganj",
            "poverty": "24.6",
            "district": "Sunamganj"
        },
        {
            "upazilla": "Sulla",
            "poverty": "28.3",
            "district": "Sunamganj"
        },
        {
            "upazilla": "Sunamganj",
            "poverty": "25.1",
            "district": "Sunamganj"
        },
        {
            "upazilla": "Tahirpur",
            "poverty": "31.2",
            "district": "Sunamganj"
        },
        {
            "upazilla": "Balaganj",
            "poverty": "19.7",
            "district": "Sylhet "
        },
        {
            "upazilla": "Beani Bazar",
            "poverty": "15.9",
            "district": "Sylhet "
        },
        {
            "upazilla": "Bishwanath",
            "poverty": "12.5",
            "district": "Sylhet "
        },
        {
            "upazilla": "Companiganj",
            "poverty": "34.5",
            "district": "Sylhet "
        },
        {
            "upazilla": "Dakshin Surma",
            "poverty": "10.3",
            "district": "Sylhet "
        },
        {
            "upazilla": "Fenchuganj",
            "poverty": "16.9",
            "district": "Sylhet "
        },
        {
            "upazilla": "Golapganj",
            "poverty": "14.9",
            "district": "Sylhet "
        },
        {
            "upazilla": "Gowanghat",
            "poverty": "52.6",
            "district": "Sylhet "
        },
        {
            "upazilla": "Jaintiapur",
            "poverty": "34.7",
            "district": "Sylhet "
        },
        {
            "upazilla": "Kanaighat",
            "poverty": "45.8",
            "district": "Sylhet "
        },
        {
            "upazilla": "Sylhet",
            "poverty": "14.3",
            "district": "Sylhet "
        },
        {
            "upazilla": "Zakiganj",
            "poverty": "39",
            "district": "Sylhet "
        },
        {
            "upazilla": "Basil",
            "poverty": "19.7",
            "district": "Tangail"
        },
        {
            "upazilla": "Bhuzpur",
            "poverty": "34.4",
            "district": "Tangail"
        },
        {
            "upazilla": "Delduar",
            "poverty": "24.3",
            "district": "Tangail"
        },
        {
            "upazilla": "Dhanbari",
            "poverty": "37",
            "district": "Tangail"
        },
        {
            "upazilla": "Ghatail",
            "poverty": "28.7",
            "district": "Tangail"
        },
        {
            "upazilla": "Gopalpur",
            "poverty": "29.3",
            "district": "Tangail"
        },
        {
            "upazilla": "Kalihati",
            "poverty": "23.5",
            "district": "Tangail"
        },
        {
            "upazilla": "Madhupur",
            "poverty": "36.4",
            "district": "Tangail"
        },
        {
            "upazilla": "Mirzapur",
            "poverty": "26.7",
            "district": "Tangail"
        },
        {
            "upazilla": "Nagarpur",
            "poverty": "39.9",
            "district": "Tangail"
        },
        {
            "upazilla": "Sakhipur",
            "poverty": "26",
            "district": "Tangail"
        },
        {
            "upazilla": "Tangail",
            "poverty": "31.7",
            "district": "Tangail"
        },
        {
            "upazilla": "Baliadangi",
            "poverty": "26.5",
            "district": "Thakurgaon"
        },
        {
            "upazilla": "Haripur",
            "poverty": "29.7",
            "district": "Thakurgaon"
        },
        {
            "upazilla": "Pirganj",
            "poverty": "23.3",
            "district": "Thakurgaon"
        },
        {
            "upazilla": "Ranisankail",
            "poverty": "25.8",
            "district": "Thakurgaon"
        },
        {
            "upazilla": "Thakurgaon",
            "poverty": "28.6",
            "district": "Thakurgaon"
        }
    ]
    for item in poverty:
        collection.update({'district':item['district'],'upazila':item['upazilla'].lower().title()},{"$set":{'poverty': float(item['poverty'])}}, upsert=True)
parse()
parsePoverty()
