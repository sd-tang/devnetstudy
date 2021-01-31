#! usr/bin/env python3
import sys
import acitoolkit.acitoolkit as aci 

# Assign initial variables
apic_url = "https://sandboxapicdc.cisco.com"
username = "admin"
password = "ciscopsdt"

# Establish connection session with APIC
session = aci.Session(apic_url, username, password)
# Login to that session
response = session.login()
if not response.ok:
    print("Login unsuccessful, please try again")
    sys.exit()


# GET Endpoints using aci.Endpoint.get(session_name)
endpoints = aci.Endpoint.get(session)

# Print table outline and headers
print("="*86)
print("{0:1s}{1:18s}{2:1s}{3:15s}{4:1s}{5:10s}{6:1s}{7:8s}{8:1s}{9:16s}{10:1s}{11:12s}{12:1s}".\
    format("|", "MAC ADDRESS", "|", "IP ADDRESS", "|", "ENCAP", "|", "TENANT", "|", "APP PROFILE", \
        "|", "EPG", "|"))
print("-"*86)

# Print endpoints
for endpoint in endpoints:
    epg = endpoint.get_parent()
    app_profile = epg.get_parent()
    tenant = app_profile.get_parent()
    print("{0:1s}{1:18s}{2:1s}{3:15s}{4:1s}{5:10s}{6:1s}{7:8s}{8:1s}{9:16s}{10:1s}{11:12s}{12:1s}".\
    format("|", endpoint.mac, "|", endpoint.ip, "|", endpoint.encap, "|", tenant.name, "|", \
        app_profile.name, "|", epg.name, "|"))
print("="*86)