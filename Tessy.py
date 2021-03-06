import requests
from myconfig import *


def get_vehicle_ids(session):
    ret_object = {}
    response = {}
    try:
        response = session.get('https://owner-api.teslamotors.com/api/1/vehicles').json()['response']
    except:
        print("Could not get list of vehicles. Tesla API token might be invalid.")
    for obj in response:
        ret_object[obj['id']] = obj['display_name']
    return ret_object


def get_vehicle_odometer(vehicle_id, vehicle_name, session):
    print("Getting odometer reading for " + vehicle_name)
    response = session.get('https://owner-api.teslamotors.com/api/1/vehicles/' + str(vehicle_id) + '/data_request/vehicle_state')
    data = response.json()
    if response.status_code != 200:
        print("Response from " + vehicle_name + " was not 200: " + str(response.status_code) + " " + response.text)
        print("Try to wake it using your phone")
        raise
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
