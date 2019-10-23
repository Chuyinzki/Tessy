import requests
import json
from myconfig import *


def get_vehicle_ids():
    ret_object = {}
    response = s.get('https://owner-api.teslamotors.com/api/1/vehicles').json()['response']
    for obj in response:
        ret_object[obj['id']] = obj['display_name']
    return ret_object


def get_vehicle_odometer(vehicle_id, vehicle_name):
    print("Getting odometer reading for " + vehicle_name)
    response = s.get('https://owner-api.teslamotors.com/api/1/vehicles/' + str(vehicle_id) + '/data_request/vehicle_state')
    data = response.json()
    return data['response']['odometer']


s = requests.Session()
s.headers.update({'Authorization': 'Bearer ' + access_token})
vehicles = get_vehicle_ids()
firstID = next(iter(vehicles))
odometer = get_vehicle_odometer(firstID, vehicles[firstID])
print(odometer)