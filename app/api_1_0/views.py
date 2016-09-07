from . import api
from flask import request, abort, jsonify
from app import db
from ..models import Device, Sensor, Number
from ..exceptions import ValidationError
from .errors import return_success


@api.route('/devices', methods=['post'])
def add_device():
    device = Device.from_json(request.json)
    db.session.add(device)
    return return_success()

    # return 200


@api.route('/device/<device_id>/sensors', methods=['post'])
def add_sensor(device_id):
    device = Device.query.filter_by(id=int(device_id)).first()
    if not device:
        raise ValidationError('no such device')
    sensor = Sensor.from_json(request.json)
    sensor.device = device
    db.session.add(sensor)
    return return_success()


@api.route('/device/<device_id>/sensor/<sensor_id>', methods=['post'])
def add_data(device_id, sensor_id):
    sensor = Device.query.filter_by(id=int(device_id)).first().sensors.filter_by(id=int(sensor_id)).first()
    if not sensor:
        raise ValidationError('no such sensor')
    number = Number.from_json(request.json)
    number.sensor = sensor
    db.session.add(number)
    return return_success()
