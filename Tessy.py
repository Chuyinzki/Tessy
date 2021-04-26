import requests
from myconfig import *

CONST_TESSY_ID = 15372580391886096


def get_vehicle_ids(session):
    ret_object = {}
    response = {}
    try:
        response = do_session_get(session, 'https://owner-api.teslamotors.com/api/1/vehicles')['response']
    except:
        print("Could not get list of vehicles. Tesla API token might be invalid.")
    for obj in response:
        ret_object[obj['id']] = obj['display_name']
    return ret_object


def get_vehicle_odometer(vehicle_id, vehicle_name, session):
    print("Getting odometer reading for " + vehicle_name)
    response = do_session_get(session,
        'https://owner-api.teslamotors.com/api/1/vehicles/' + str(vehicle_id) + '/data_request/vehicle_state')
    data = response.json()

    try:
        ret = data['response']['odometer']
    except TypeError as error:
        print(error)
    else:
        print("Odometer reading is: " + str(ret))
        return ret


def do_session_get(session, url):
    response = session.get(url)
    print("Session get response: " + str(response.status_code))
    if response.status_code == 401:
        print("Authentication error. Tesla API token might be invalid.")
        raise
    if response.status_code != 200:
        print("Response was not 200. Try to wake it using your phone")
        raise
    return response


def get_first_odometer_reading():
    s = prepare_session()
    vehicles = get_vehicle_ids(s)
    first_id = next(iter(vehicles))
    odometer = get_vehicle_odometer(first_id, vehicles[first_id], s)
    return odometer


def get_tessy_odometer_reading():
    return get_vehicle_odometer(15372580391886096, "Tessy", prepare_session())


def prepare_session():
    s = requests.Session()
    s.headers.update({'Authorization': 'Bearer ' + access_token})
    return s
