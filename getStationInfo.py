#!/usr/bin/python3.6

import os
import requests
import json
from pprint import pprint

workingDirectory = os.path.dirname(os.path.abspath(__file__)) + '/'
url = 'https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'

# Get the parameters from request.json
payload = open(workingDirectory + 'request.json')
headers = {'Content-Type': 'application/graphql'}
r = requests.post(url=url, data=payload, headers=headers)
jsonResponse = r.content
result = json.loads(jsonResponse)

bikeStationID = result['data']['bikeRentalStation']['stationId']
bikeStationName = result['data']['bikeRentalStation']['name']
freeBikeAmount = result['data']['bikeRentalStation']['bikesAvailable']
print(bikeStationID)
print(bikeStationName)
print(freeBikeAmount)