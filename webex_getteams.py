#! usr/bin/env python3
import json
import requests

base_url = "https://webexapis.com/api/v1/teams"
myheaders = {
    "Authorization": "Bearer \
        NGI5OWVkZGYtZDNkYi00MDM1LTlmN2YtZjlhZmNkZTBmMGZkYjcxOTM4NGMtMDc5_P0A1_41a4a6c5-2edc-44ef-b4fc-2fbfe8959f4c",
    "Content-Type": "application/json"
}

response = requests.request("GET", url=base_url, headers=myheaders)
print(response.text)