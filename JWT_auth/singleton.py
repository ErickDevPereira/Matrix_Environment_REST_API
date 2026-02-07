from .src import JwtGen
import os

jwt_singleton: JwtGen = JwtGen(
    secret_key = os.getenv("SECRET_KEY"),
    algorithm = os.getenv("ALGORITHM"),
    exp_hours = int(os.getenv("EXP_HOURS")),
    refresh_when_lacking_minutes = os.getenv("REFRESH_WHEN_LACKING_MINUTES")
)