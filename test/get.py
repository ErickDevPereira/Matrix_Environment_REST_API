import pprint
import requests
URL = 'http://127.0.0.1:5000/my_opinion'

resp = requests.get(URL, params = {"latitude": 23.4558, "longitude": 45.6396}, headers = {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjMsImV4cCI6MTc3MDQ5MTU3MH0.0_tEWqogoeXuqDL3d3xUY1OeBfXSRZ2f8krJnBRnANU'})
print(resp.status_code)
pprint.pprint(resp.json())