#!/usr/bin/python3.6

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

def constructSQL(ID, name, bikes, lon, lat, time):
    SQL = 'INSERT INTO Bikestations(StationID, StationName, StationFreeBikes, Lon, Lat, Timestamp) VALUES("'+ID+'", "'+name+'",'+bikes+',"'+lon+'","'+lat+'","'+time+'");'
    return(SQL)

# Get the parameters from request.json
payload = open(workingDirectory + 'getAllStations.json')
headers = {'Content-Type': 'application/graphql'}
r = requests.post(url=url, data=payload, headers=headers)
jsonResponse = r.content
result = json.loads(jsonResponse)

data = result['data']['bikeRentalStations']
#pprint(data)
pprint(len(result['data']['bikeRentalStations']))
SQL = ''

for i in data:
    stationID = str(i['stationId'])
    stationName = i['name']
    bikesAvailable = str(i['bikesAvailable'])
    stationLon = str(i['lon'])
    stationLat = str(i['lat'])
    timestamp = str(datetime.datetime.now()).split('.')[0]
    SQL += constructSQL(stationID, stationName, bikesAvailable, stationLon, stationLat, timestamp)
cursor.execute(SQL)



    

