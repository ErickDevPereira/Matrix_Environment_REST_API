from flask import request
from flask_restful import reqparse, Resource, abort, Api
from typing import Dict, Tuple, Any
from abc import ABC, abstractmethod

class HTTP:

    class ForceGET(ABC):

        @abstractmethod
        def get(self): #Forcing a polymorphism over the GET HTTP method.
            pass

    class Util:

        def auth(self):
            if self.latitude is None or self.longitude is None or self.detail is None: #Validating the presence of value.
                abort(400, message = "Invalid request. You must define a value for latitude, longitude and detail parameters.")

            if self.detail in ("true", "True"): #Validating if detail has correct value.
                self.detail_bool: bool = True
            elif self.detail in ("False", "false"):
                self.detail_bool: bool = False
            else:
                #This case should have a response with 400 (bad request) as status code.
                abort(400, message = "Invalid request for detail parameter. You must provide either True or False, nothing else!")
            
            if self.latitude < -90 or self.latitude > 90: #Validating the range of latitude.
                abort(400, message = "Invalid value for latitude! It ranges from -90 deg to 90 deg")
            
            if self.longitude < -180 or self.longitude > 180: #Validating the range of longitude.
                abort(400, message = "Invalid value for longitude! It must range from -180 deg to 180 deg")

    class EnvironmentDataNow(ForceGET, Util, Resource):

        def get(self) -> Tuple[Dict[str, Any], int]:

            self.latitude: float = request.args.get("latitude", type = float)
            self.longitude: float = request.args.get("longitude", type = float)
            self.detail: str = request.args.get("detail")
            
            self.auth() #Authenticating data given by the user and creating the self.detail_bool
            
            if self.detail_bool:
                #Here will be the detailed data
                return {"message": "You've chosen the detailed option"}, 200
            else:
                return {"message": "You've not chosen the detailed option"}, 200
                #Here will be the overall data without much detail.
    
    class ForecastEnvironmentDataNow(ForceGET, Util, Resource):

        def get(self) -> Tuple[Dict[str, Any], int]:

            self.latitude: float = request.args.get("latitude", type = float)
            self.longitude: float = request.args.get("longitude", type = float)
            self.detail: str = request.args.get("detail")

            self.auth()

            if self.detail_bool:
                return {"message": "You've chosen the datailed option for forecast"}, 200
            else:
                return {"message": "You've not chosen the detailed option for forecast"}, 200

    def __init__(self, api: Api, **kwargs):
        self.__now_data_rsc = api.add_resource(kwargs['EnvironmentDataNow'], "/actual_environment")
        self.__forecast_data_rsc = api.add_resource(kwargs['ForecastEnvironmentDataNow'], "/forecast_environment")