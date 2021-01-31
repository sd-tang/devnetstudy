#! /usr/bin/env python3
from meraki_sdk.meraki_sdk_client import MerakiSdkClient

#Cisco DevNet Sandbox Meraki API Key
X_CISCO_MERAKI_API_KEY = '15da0c6ffff295f16267f88f98694cf29a86ed87'

#Establish a new client connection with Meraki REST API
#Pass the API Key for authentication
meraki = MerakiSdkClient(X_CISCO_MERAKI_API_KEY)

#Get a list of all the organizations for the Cisco DevNet account
orgs = meraki.organizations.get_organizations()
for org in orgs:
    print(f"Org ID: {org['id']}     Org Name: {org['name']}")


params = {}
params["organization_id"] = "549236"    #Demo Organization "DevNet Sandbox"

#Get a list of all the networks for the Cisco DevNet organization
nets = meraki.networks.get_organization_networks(params)
for net in nets:
    print("Network ID: {0:20s}, Name: {1:45s}, Tags: {2:<10s}".format(\
        net['id'], net['name'], str(net['tags'])))


#Get a list of all the devices that are part of the Always On Network
devices = meraki.devices.get_network_devices("L_646829496481107379")
for device in devices:
    print("Device Model: {0:9s}, Serial: {1:14s}, MAC: {2:17s}, Firmware: {3:12s}"\
        .format(device['model'], device['serial'], device['mac'], device['firmware']))