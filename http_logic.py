from flask import request
from flask_restful import reqparse, Resource, abort, Api
from typing import Dict, Tuple

class HTTP:

    class EnvironmentDataNow(Resource):

        def get(self) -> Tuple[Dict[str, str], int]:

            latitude: float = request.args.get("latitude", type = float)
            longitude: float = request.args.get("longitude", type = float)
            detail: str = request.args.get("detail")
            
            if latitude is None or longitude is None or detail is None: #Validating the presence of value.
                abort(400, message = "Invalid request. You must define a value for latitude, longitude and detail parameters.")

            if detail in ("true", "True"): #Validating if detail has correct value.
                detail_bool: bool = True
            elif detail in ("False", "false"):
                detail_bool: bool = False
            else:
                #This case should have a response with 400 (bad request) as status code.
                abort(400, message = "Invalid request for detail parameter. You must provide either True or False, nothing else!")
            
            if latitude < -90 or latitude > 90: #Validating the range of latitude.
                abort(400, message = "Invalid value for latitude! It ranges from -90 deg to 90 deg")
            
            if longitude < -180 or longitude > 180: #Validating the range of longitude.
                abort(400, message = "Invalid value for longitude! It must range from -180 deg to 180 deg")
            
            if detail:
                #Here will be the detailed data
                return {"message": "You've chosen the detailed option"}, 200
            else:
                return {"message": "You've chosen the detailed option"}, 200
                pass #Here will be the overall data without much detail.
        
    def __init__(self, api: Api, **kwargs):
        self.__now_data_rsc = api.add_resource(kwargs['EnvironmentDataNow'], "/actual_environment")