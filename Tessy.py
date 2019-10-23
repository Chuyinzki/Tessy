import requests
import json
from myconfig import *

s = requests.Session()
s.headers.update({'Authorization': 'Bearer ' + access_token})

response = s.get('https://owner-api.teslamotors.com/api/1/vehicles/15372580391886096/data_request/vehicle_state')
data = response.json()
odometer = data['response']['odometer']
print(odometer)

