from . import main
from .forms import NameForm
from flask import render_template, request, abort, jsonify
from ..models import Device, Sensor, Number
from app import db


@main.route('/', methods=['get', 'post'])
def index():
    # d = request.form
    # if d:
    #     l = [i + "=" + d[i] for i in d]
    #     print(l)
    json = request.json
    print(json)
    print(json.get('name'))
    return '<h1>Hello world!</h1>\n'


