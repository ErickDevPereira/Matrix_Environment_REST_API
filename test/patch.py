import pprint
import requests
URL = 'http://127.0.0.1:5000/my_opinion'

resp = requests.patch(URL, json = {'text': "Testinnnggggg", "token": "ef61d79514c02428"}, headers = {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjEsImV4cCI6MTc3MDQzMDE4NH0.6OB0XRrKD3kn95a9dihPq2RyHL_1mDldo79K6KszzYc'})
print(resp.status_code)
pprint.pprint(resp.json())