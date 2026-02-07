import pprint
import requests
URL = 'http://127.0.0.1:5000/actual_environment'

resp = requests.get(URL, params = {"latitude": 52.5200, "longitude": 13.4050, "detail" : True}, headers = {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjEsImV4cCI6MTc3MDQzMDE4NH0.6OB0XRrKD3kn95a9dihPq2RyHL_1mDldo79K6KszzYc'})
print(resp.status_code)
pprint.pprint(resp.json())