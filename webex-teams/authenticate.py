# Fill in this file with the authentication code from the Webex Teams exercise

import requests
import json
# This access token may be a (limited duration) personal access token, a Bot token, or an OAuth token from an Integration or Guest Issuer application.
# IMPORTANT
# Make sure to replace access_token with YOUR access token.
access_token = 'YTY4NWIyMzEtMGY0NC00YjNmLTkyZjQtMjU4Yzg2NDlkZTgyYjFmMGNkZDMtYjAz_P0A1_41a4a6c5-2edc-44ef-b4fc-2fbfe8959f4c'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
