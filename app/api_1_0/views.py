from . import api
from flask import request, abort, jsonify
from app import db
from ..models import Device, Sensor, Number
from ..exceptions import ValidationError
from .errors import return_success, bad_request


def json_error():
    return bad_request('json error')


@api.route('/', methods=['post', 'get'])
def index():
    return jsonify({'form': 'api', 'success': True, 'method': request.method})


@api.route('/devices', methods=['post', 'get'])
def query_or_add_device():
    if request.method == 'POST':
        device = Device.from_json(request.json)
        if not device:
            return json_error()
        db.session.add(device)
        db.session.commit()
        return device.to_json()
    elif request.method == 'GET':
        l = Device.query.all()
        d = {i: l[i].to_dict() for i in range(len(l))}
        return jsonify(d)


@api.route('/device/<device_id>/sensors', methods=['post', 'get'])
def query_or_add_sensor(device_id):
    device = Device.query.filter_by(id=int(device_id)).first()
    if not device:
        return json_error()
    if request.method == 'POST':
        sensor = Sensor.from_json(request.json)
        sensor.device = device
        db.session.add(sensor)
        db.session.commit()
        return sensor.to_json()
    elif request.method == 'GET':
        l = device.sensors.all()
        d = {i: l[i].to_dict() for i in range(len(l))}
        return jsonify(d)


@api.route('/device/<device_id>/sensor/<sensor_id>', methods=['post', 'get'])
def query_or_add_data(device_id, sensor_id):
    sensor = Device.query.filter_by(id=int(device_id)).first().sensors.filter_by(id=int(sensor_id)).first()
    if not sensor:
        return json_error()
    if request.method == 'POST':
        number = Number.from_json(request.json)
        number.sensor = sensor
        db.session.add(number)
        db.session.commit()
        return number.to_json()
    elif request.method == 'GET':
        l = sensor.numbers.all()
        d = {i: l[i].to_dict() for i in range(len(l))}
        return jsonify(d)
