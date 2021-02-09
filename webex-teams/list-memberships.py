#! usr/bin/env python
import requests
import json 

room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNjcwNWQzMDAtNjkwNS0xMWViLTk2NWUtNDdjYjE3ZTcwOTdl"
url = "https://webexapis.com/v1/memberships"
access_token = "YTY4NWIyMzEtMGY0NC00YjNmLTkyZjQtMjU4Yzg2NDlkZTgyYjFmMGNkZDMtYjAz_P0A1_41a4a6c5-2edc-44ef-b4fc-2fbfe8959f4c"
headers = {
    "Authorization": "Bearer {}".format(access_token),
    "Content-Type": "application/json"
}
params = {
    "roomId": room_id
}

response = requests.get(url, headers=headers, params=params)
print(json.dumps(response.json(), indent=4))