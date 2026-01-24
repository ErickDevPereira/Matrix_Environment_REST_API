from flask import Flask
from flask_restful import Api
from typing import Dict, List

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
        FILE = open("src/tokens.txt")
        lines: List[str] = FILE.readlines()
        safe_api_token: str = lines[1][:-1]
        weather_api_token: str = lines[-1]
    except Exception as err:
        #Reading the tokens through I/O if the file isn't defined or has a problem.
        print(f"Couldn't read a file with the tokens. Please, give the correct tokens.\n{err}")
        safe_api_token: str = input("Your token to safe API:  ")
        weather_api_token: str = input("Your token to weather API:  ")
    finally:
        server: __Main = __Main(safe_api_token = safe_api_token, weather_api_token = weather_api_token)
        from http_logic import HTTP
        EnvironmentDataNow = HTTP.EnvironmentDataNow #importing the class that has the HTTP methods for the /actual_environment route.
        http_initializer = HTTP(server.api, EnvironmentDataNow = EnvironmentDataNow)
        server.app.run(debug = True)