"""Webex Devices - Get Session Cookie"""
# This is a sample code from OCG, the credentials do not work
import requests

myurl = "https://10.10.20.159/xmlapi/session/begin"
myheaders = {
    'Authorization': "Basic ZGV2YXNjOkMxc2NvITIz"
}

response = requests.request("POST", myurl, headers=myheaders)
print(response.headers["Set-Cookie"])