import http
from abc import abstractmethod
from flask import jsonify, request, session

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
        self.request = request
        self.session = session
        self.response = jsonify


    @abstractmethod
    def serve(self): 
        pass
    

def serve(case=UCase):
    return case().serve()