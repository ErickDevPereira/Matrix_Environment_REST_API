import pprint
import requests
URL = 'http://127.0.0.1:5000/actual_environment'

resp = requests.get(URL, params = {"latitude": 52.5200, "longitude": 13.4050, "detail" : True})
print(resp.status_code)
pprint.pprint(resp.json())