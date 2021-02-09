# Fill in this file with the people listing code from the Webex Teams exercise

import requests
import json

access_token = 'YTY4NWIyMzEtMGY0NC00YjNmLTkyZjQtMjU4Yzg2NDlkZTgyYjFmMGNkZDMtYjAz_P0A1_41a4a6c5-2edc-44ef-b4fc-2fbfe8959f4c'  # Make sure to add your access token here
url = 'https://api.ciscospark.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

# GET user by email
params = {
    'email': 'christopher.thg@gmail.com' # Make sure you add your users's email address here
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))

# GET user by ID
person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS8wN2NmYjhhNy0xM2UyLTRhMDAtOTFlZS0zMWIxNGZhOTg2ZDI' # Add your ID here, which you get from the prior request
url = 'https://api.ciscospark.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
 