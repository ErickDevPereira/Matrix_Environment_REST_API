import pprint
import requests
URL = 'http://127.0.0.1:5000/forecast_environment'

resp = requests.get(URL, params = {"latitude": 23.4558, "longitude": 45.6396})
print(resp.status_code)
pprint.pprint(resp.json())