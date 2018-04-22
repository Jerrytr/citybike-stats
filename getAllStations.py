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
def constructSQL(ID, name, lon, lat):
    SQL = 'INSERT INTO Bikestations(StationID, StationName, StationLon, StationLat) VALUES("'+ID+'","'+name+'","'+lon+'","'+lat+'");'
    return(SQL)

# Get the parameters from request.json
payload = open(workingDirectory + 'getAllStations.json')

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
    stationName = i['name']
    stationLon = str(i['lon'])
    stationLat = str(i['lat'])
    SQL = constructSQL(stationID, stationName, stationLon, stationLat)
    cursor.execute(SQL)



    

