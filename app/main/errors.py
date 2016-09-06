from . import main
from flask import request, jsonify, abort


# 如果是json请求,返回json,否则,返回默认html,反正本程序仅支持json
@main.errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    abort(404)
