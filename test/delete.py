import pprint
import requests
URL = 'http://127.0.0.1:5000/my_opinion'

resp = requests.delete(URL, json = {'token': 'e27166f8dd0765e9'})
print(resp.status_code)
pprint.pprint(resp.json())