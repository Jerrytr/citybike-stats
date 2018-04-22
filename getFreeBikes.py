#!/usr/bin/python3.6

"""
This file is used to populate the Bikestations table
with entries so that we have information on them for later use.
Run only one
"""

import os
import requests
import json
import datetime
from pprint import pprint
import pymysql

workingDirectory = os.path.dirname(os.path.abspath(__file__)) + '/'
url = 'https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'

# Define database connection
dbAddr = open(workingDirectory + 'mariadb/freebikes-dbAddr','r').readline().rstrip()
dbUser = open(workingDirectory + 'mariadb/freebikes-dbUser','r').readline().rstrip()
dbPw = open(workingDirectory + 'mariadb/freebikes-dbPw','r').readline().rstrip()
db = pymysql.connect(dbAddr,dbUser,dbPw,'bike_info_db',autocommit = True)
cursor = db.cursor()

# Function to create SQL statements
def constructSQL(ID, bikesFree, timestamp):
    SQL = 'INSERT INTO Bikestats(StationID, Bikesfree, Timestamp) VALUES("'+ID+'",'+bikesFree+',"'+timestamp+'");'
    return(SQL)

# Get the parameters from request.json
payload = open(workingDirectory + 'getFreeBikes.json')

# Post the API query
headers = {'Content-Type': 'application/graphql'}
r = requests.post(url=url, data=payload, headers=headers)
jsonResponse = r.content
result = json.loads(jsonResponse)

data = result['data']['bikeRentalStations']
pprint(len(result['data']['bikeRentalStations']))
SQL = ''

for i in data:
    stationID = str(i['stationId'])
    bikesAvailable = str(i['bikesAvailable'])
    timestamp = str(datetime.datetime.now()).split('.')[0]
    SQL = constructSQL(stationID, bikesAvailable, timestamp)
    cursor.execute(SQL)



    

