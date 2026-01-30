import pprint
import requests
URL = 'http://127.0.0.1:5000/my_opinion'

resp = requests.post(URL, params = {"latitude": 23.4558, "longitude": 45.6396}, json = {"text": "A test", "name" : "testname"})
print(resp.status_code)
pprint.pprint(resp.json())