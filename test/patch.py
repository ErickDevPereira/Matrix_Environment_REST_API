import pprint
import requests
URL = 'http://127.0.0.1:5000/my_opinion'

resp = requests.patch(URL, json = {'text': "Testinnnggggg", "token": "6a2574ba1545e7b7"})
print(resp.status_code)
pprint.pprint(resp.json())