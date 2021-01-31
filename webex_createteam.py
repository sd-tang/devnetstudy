#! /usr/bin/env python3
"""This script is to create a new Webex Team.
Remember to obtain a Bearer personal access token from https://developer.webex.com"""

import json
import requests

base_url = "https://webexapis.com/v1/teams"
payload = {
    "name": "DevAsc Certification Team"
}
myheaders = {
    "Authorization": "Bearer \
        NGI5OWVkZGYtZDNkYi00MDM1LTlmN2YtZjlhZmNkZTBmMGZkYjcxOTM4NGMtMDc5_P0A1_41a4a6c5-2edc-44ef-b4fc-2fbfe8959f4c",
    "Content-Type": "application/json"
}

response = requests.request("POST", base_url, data=json.dumps(payload), headers=myheaders)
print(response.text)
