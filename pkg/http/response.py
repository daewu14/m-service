from flask import jsonify, Response as FlaskResponse
import http
from collections import OrderedDict
import json


class Response:

    def __init__(self,
                 status: http.HTTPStatus = http.HTTPStatus.OK,
                 message: str = "SUCCESS",
                 data: dict = None,
                 meta: dict = None):
        self.status = status
        self.message = message
        self.data = data
        self.meta = meta

    def build(self):
        res = [
            ('status', self.status.name),
            ('message', self.message),
        ]

        if self.data is not None:
            res.append(('data', self.data))

        if self.meta is not None:
            res.append(('meta', self.meta))

        return FlaskResponse(
            json.dumps(OrderedDict(res), sort_keys=False),
            status=self.status,
            mimetype='application/json'
        )
