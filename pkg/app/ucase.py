import http
from abc import abstractmethod
from flask import request, session, Response
from pkg.http.response import Response as HttpResponse

"""
This module defines the UCase class and the serve function for handling
Flask requests and responses.
Classes:
    UCase: An abstract base class that provides a structure for handling
            Flask requests, sessions, and responses.
Functions:
    serve(case=UCase): A function that instantiates the given case class
                        and calls its serve method.
Usage:
    Subclass UCase and implement the serve method to define custom
    request handling logic. Use the serve function to execute the
    serve method of the subclass.
"""


class UCase:

    def __init__(self):
        self.http_status = http.HTTPStatus
        self.request = request
        self.session = session

    @classmethod
    def response(cls, status: http.HTTPStatus = http.HTTPStatus.OK, message: str = "SUCCESS", data: dict = None, meta: dict = None):
        return HttpResponse(data=data, status=status, message=message, meta=meta).build()

    @abstractmethod
    def serve(self) -> Response:
        pass


def serve(case=UCase):
    return case().serve()
