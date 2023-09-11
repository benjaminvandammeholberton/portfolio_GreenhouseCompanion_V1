"""This script defines Flask view functions for handling
CRUD operations on the "sensors" resource."""

from api.views import app_views
from flask import jsonify, request, abort, render_template
from models import storage
from models.sensors import Sensors


@app_views.route('/sensors', methods=['GET'], strict_slashes=False)
def get_all_sensors():
    """
    Retrieves all sensor areas from the storage and returns them as a list
    of JSON objects.
    """
    sensors = storage.all(Sensors).values()
    # garden_area = storage.all(GardenArea).values()
    # return render_template('sensors.html', sensors=sensors)

    # Combine the data from both dictionaries
    # combined_data = list(sensors) + list(garden_area)
    return jsonify([data.to_dict() for data in sensors])

@app_views.route('/sensors/last', methods=['GET'], strict_slashes=False)
def get_last_sensor():
    """
    Retrieves the last added sensor data and returns it as a JSON object.
    """
    sensors = storage.all(Sensors).values()

    # Sort the sensors by timestamp in descending order
    sorted_sensors = sorted(sensors, key=lambda sensor: sensor.created_at, reverse=True)

    if sorted_sensors:
        last_sensor = sorted_sensors[0]
        return jsonify(last_sensor.to_dict())
    else:
        # Handle the case where there are no sensors
        return jsonify({"message": "No sensor data available"}), 404

@app_views.route('/sensors/<sensors_id>', methods=['GET'],
                 strict_slashes=False)
def get_sensors(sensors_id):
    """
    Retrieves a specific sensor area based on the provided ID and returns its
    details as a JSON object.
    """
    sensor = storage.get(Sensors, sensors_id)
    if sensor:
        return jsonify(sensor.to_dict())
    abort(404)



@app_views.route('/sensors', methods=['POST'], strict_slashes=False)
def create_sensors():
    """
    Creates a new sensor area based on the provided details and returns
    its details as a JSON object.
    """
    sensors_list = ["soil_humidity_1", "soil_humidity_2", "soil_humidity_3"]
    data = request.get_json()
    response = data.copy()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    new_sensor = Sensors(**data)
    new_sensor.save()
    # for key, value in data.items():
    if data["soil_humidity_1"] > 2300:
        response['relay'] = True
        print(response)
        return jsonify(response) , 201
        # if key in sensors_list and int(value) > 2300:
            # response['relay'] = True
        #     response['right'] = response['soil_humidity_3']
        #     response['left'] = response['soil_humidity_1']
        #     response['middle'] = response['soil_humidity_2']
    #         print(response)
    #         return jsonify(response) , 201
    response['right'] = response['soil_humidity_3']
    response['left'] = response['soil_humidity_1']
    response['middle'] = response['soil_humidity_2']
    print(response)
    return jsonify(new_sensor.to_dict()) , 201
