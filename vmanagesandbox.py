#! usr/bin/env python3
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Specify Cisco vManage IP, username, password
vmanage_ip = "sandboxsdwan.cisco.com"
username = "devnetuser"
password = "Cisco123!"

base_url_vmanage = "https://{}:8443/".format(vmanage_ip)

# Login API resource and login credentials
login_action = "j_security_check"
login_data = {'j_username': username, 'j_password': password}

# Combined URL for posting login data
login_url = base_url_vmanage + login_action

# Establish a new connection
mysession = requests.session()
# Connect it to Cisco vManage API server (assign to a variable)
# POST - pass args for url, data, verify
login_response = mysession.post(url=login_url, data=login_data, verify=False)

# Get list of devices that are part of the fabric and display them
# Resource URL
device_resource = "dataservice/device"
# Combined URL
device_url = base_url_vmanage + device_resource

# GET - pass args for combined url
device_response = mysession.get(url=device_url, verify=False)
device_items = json.loads(device_response.content)['data']

# Print table1 headers
print("="*106)
print("{0:1s}{1:20s}{2:1s}{3:12s}{4:1s}{5:36s}{6:1s}{7:16s}{8:1s}{9:16s}{10:1s}".\
    format("|", "Host-Name", "|", "Device Model", "|", "Device ID", "|", "System IP", "|",\
        "Site ID", "|" ))
print("-"*106)

# Print table1 content
for item in device_items:
    print("{0:1s}{1:20s}{2:1s}{3:12s}{4:1s}{5:36s}{6:1s}{7:16s}{8:1s}{9:16s}{10:1s}".\
        format("|", item['host-name'], "|", item['device-model'], "|", item['uuid'], "|", item['system-ip'], "|",\
            item['site-id'], "|" ))
print("="*106)


# GET list of templates and display them
# Template resource url
template_resource = "dataservice/template/device"
# Combined url
template_url = base_url_vmanage + template_resource

# GET - pass args of combined url and no verify (self-signed SSL)
template_response = mysession.get(url=template_url, verify=False)
# Loads json into python dictionary list
template_items = json.loads(template_response.content)['data']

# Print table2 headers
print("="*106)
print("{0:1s}{1:20s}{2:1s}{3:12s}{4:1s}{5:36s}{6:1s}{7:16s}{8:1s}{9:16s}{10:1s}".\
    format("|", "Template Name", "|", "Device Type", "|", "Template ID", "|", \
        "Attached Devices", "|", "Template Version", "|"))
print("-"*106)

# Print table2 content
for item in template_items:
    print("{0:1s}{1:20s}{2:1s}{3:12s}{4:1s}{5:36s}{6:1s}{7:<16d}{8:1s}{9:<16d}{10:1s}".\
        format("|", item['templateName'], "|", item['deviceType'], "|", item['templateId'],\
             "|", item['devicesAttached'], "|", item['templateAttached'], "|"))
print("="*106)