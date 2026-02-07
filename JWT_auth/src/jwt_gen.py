from datetime import datetime, timedelta
import jwt
from typing import Dict

class JwtGen:

    def __init__(self, secret_key: str, algorithm: str, exp_hours: int, refresh_when_lacking_minutes: int):
        self.__SECRET_KEY: str = secret_key
        self.__ALGORITHM: str = algorithm
        self.__EXP_HOURS: int = exp_hours
        self.__REFRESH_WHEN_LACKING_MINUTES: int = refresh_when_lacking_minutes
    
    def create(self, uid: int) -> str:
        return self.__encode_jwt_token(uid)

    def __encode_jwt_token(self, uid: int) -> str:
        return jwt.encode({'uid' : uid, 'exp' : datetime.utcnow() + timedelta(hours = self.__EXP_HOURS)}, key = self.__SECRET_KEY, algorithm = self.__ALGORITHM)
    
    #This method wasn't used, but I wrote it because it can be useful if I wish to go further with this project.
    def refresh(self, jwt_token: str) -> str:
        self.__PAYLOAD: Dict[str, int | datetime] = jwt.decode(jwt_token, key = self.__SECRET_KEY, algorithms = self.__ALGORITHM)
        if self.__PAYLOAD['exp'] - datetime.utcnow() < timedelta(minutes = self.__REFRESH_WHEN_LACKING_MINUTES):
            return self.__enconde_jwt_token(self.__PAYLOAD['uid'])
        else:
            return jwt_token