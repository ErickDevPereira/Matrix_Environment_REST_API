from flask import Flask
from flask_restful import Api
from typing import Dict, List
import os

class __Main:

    def __init__(self, safe_api_token: str, weather_api_token: str):
        self.__app: Flask = Flask(__name__)
        self.__api: Api = Api(self.__app)
        self.__safe_api_token: str = safe_api_token
        self.__weather_api_token: str = weather_api_token
    
    @property
    def app(self) -> Flask:
        return self.__app
    
    @property
    def api(self) -> Api:
        return self.__api
    
    def token_gate(self) -> Dict[str, str]:
        tokens = {
                "radiationAPI": self.__safe_api_token,
                "weatherAPI": self.__weather_api_token
                }
        return tokens

if __name__ == "__main__":
    try:
        FILE = open("src/tokens.txt", 'r')
        LINES: List[str] = FILE.readlines()
        FILE.close()
        safe_api_token: str = LINES[1][:-1]
        weather_api_token: str = LINES[-1]
    except Exception as err:
        #Reading the tokens through I/O if the file isn't defined or has a problem.
        print(f"Couldn't read a file with the tokens. Please, give the correct tokens.\n{err}")
        safe_api_token: str = input("Your token to safe API:  ")
        weather_api_token: str = input("Your token to weather API:  ")
        
        if not os.path.exists('src'):
            os.mkdir("src")
        
        FILE = open("src/tokens.txt", 'w')
        FILE.write("safeapi\n" + safe_api_token + "weatherapi\n" + weather_api_token)
        FILE.close()
    finally:
        server: __Main = __Main(safe_api_token = safe_api_token, weather_api_token = weather_api_token)
        from http_logic import HTTP
        ENVIRONMENT_DATA_NOW = HTTP.EnvironmentDataNow #importing the class that has the HTTP methods for the /actual_environment route.
        FORECAST_ENVIRONMENT_DATA_NOW = HTTP.ForecastEnvironmentDataNow
        http_initializer = HTTP(server.api, EnvironmentDataNow = ENVIRONMENT_DATA_NOW, ForecastEnvironmentDataNow = FORECAST_ENVIRONMENT_DATA_NOW)
        server.app.run(debug = True)