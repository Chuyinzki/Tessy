import requests
from myconfig import *


def get_vehicle_ids(session):
    ret_object = {}
    response = session.get('https://owner-api.teslamotors.com/api/1/vehicles').json()['response']
    for obj in response:
        ret_object[obj['id']] = obj['display_name']
    return ret_object


def get_vehicle_odometer(vehicle_id, vehicle_name, session):
    print("Getting odometer reading for " + vehicle_name)
    response = session.get('https://owner-api.teslamotors.com/api/1/vehicles/' + str(vehicle_id) + '/data_request/vehicle_state')
    data = response.json()
    try:
        ret = data['response']['odometer']
    except TypeError as error:
        print(error)
    else:
        print("Odometer reading is: " + str(ret))
        return ret


def get_first_odometer_reading():
    s = requests.Session()
    s.headers.update({'Authorization': 'Bearer ' + access_token})
    vehicles = get_vehicle_ids(s)
    first_id = next(iter(vehicles))
    odometer = get_vehicle_odometer(first_id, vehicles[first_id], s)
    return odometer
