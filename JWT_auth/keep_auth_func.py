from flask import request, abort
from typing import Dict, Any
import jwt
import os
from typing import Tuple

def auth_jwt() -> Tuple[int, str]:
    jwt_token: str | None = request.headers.get("token")
        
    if jwt_token is None:
        abort(401, message =  "you must provide a jwt token to access this endpoint")
        
    try:
        payload: Dict[str, Any] = jwt.decode(jwt_token, algorithms = os.getenv("ALGORITHM"), key = os.getenv("SECRET_KEY"))
    except jwt.ExpiredSignatureError:
        abort(401, message = "The JWT token has expired. You can catch a new one by logging into your account again")
    except jwt.InvalidSignatureError:
        abort(401, message = "Check the JWT token you send. It doesn't seem to be the correct token")
    except Exception as err:
        abort(500, message = "Internal server error >>" + str(err))
    else:
        uid: int = int(payload['uid'])
        exp_time: Any = payload['exp']
        return uid, exp_time
