#! usr/bin/env python
# This is a sample code from OCG to generate a JWT(JSON Web Token)

import base64
import time
import math
import jwt

EXPIRATION = math.floor(time.time()) + 3600  # Set expiration at 1 hour(3600s) from now
PAYLOAD = {
    "sub": "devASC",
    "name": "devASC-guest",
    "iss": "GUEST_ISSUER_ID",
    "exp": EXPIRATION
}
SECRET = base64.b64decode('GUEST_ISSUE_SECRET')

TOKEN = jwt.encode(PAYLOAD, SECRET)

print(TOKEN.decode('utf-8'))
HEADERS = {
    'Authorization': 'Bearer ' + TOKEN.decode('utf-8')
}