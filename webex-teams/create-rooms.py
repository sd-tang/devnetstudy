#! usr/bin/env python
import requests
import json

url = "https://webexapis.com/v1/rooms"
access_token = "YTY4NWIyMzEtMGY0NC00YjNmLTkyZjQtMjU4Yzg2NDlkZTgyYjFmMGNkZDMtYjAz_P0A1_41a4a6c5-2edc-44ef-b4fc-2fbfe8959f4c"
headers = {
    "Authorization": "Bearer {}".format(access_token),
    "Content-Type": "application/json"
}
params = {"title": "DevNet Training Room 1"}

response = requests.post(url, headers=headers, json=params)
print(json.dumps(response.json(), indent=4))