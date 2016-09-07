from . import db
from datetime import datetime
from flask import jsonify


class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    about = db.Column(db.String(64))

    sensors = db.relationship('Sensor', backref='device', lazy='dynamic')

    def to_json(self):
        return jsonify({
            'id': self.id,
            'name': self.name,
            'about': self.about,
            'sensor_num': self.sensors.count()
        })

    @staticmethod
    def from_json(json_device):
        name = json_device.get('name')
        about = json_device.get('about')
        return Device(name=name, about=about)

    def __repr__(self):
        return '<Device {}>'.format(self.name)


class Sensor(db.Model):
    __tablename__ = 'sensors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.String(64))

    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'))
    numbers = db.relationship('Number', backref='sensor', lazy='dynamic')

    def to_json(self):
        return jsonify({
            'id': self.id,
            'name': self.name,
            'about': self.about,
            'device_id': self.device_id,
            'data_num': self.numbers.count()
        })

    @staticmethod
    def from_json(json_sensor):
        name = json_sensor.get('name')
        about = json_sensor.get('about')
        return Sensor(name=name, about=about)

    def __repr__(self):
        return '<Sensor {}>'.format(self.name)


class Number(db.Model):
    __tablename__ = 'numbers'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    value = db.Column(db.Float, nullable=False)

    sensor_id = db.Column(db.Integer, db.ForeignKey('sensors.id'))

    def to_json(self):
        return jsonify({
            'id': self.id,
            'timestamp': self.timestamp,
            'value': self.value,
            'sensor_id': self.sensor_id
        })

    @staticmethod
    def from_json(json_data):
        value = json_data.get('value')
        timestamp = json_data.get('timestamp')
        return Number(value=value, timestamp=timestamp)

    def __repr__(self):
        return '<Number {}={}>'.format(self.timestamp, self.value)
