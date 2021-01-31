#! /usr/bin/env python3
from dnacentersdk import DNACenterAPI

# Create a DNACenterAPI connection object
# Pass arguments of username and password
myapi = DNACenterAPI(username="devnetuser", password="Cisco123!", \
    base_url="https://sandboxdnac2.cisco.com")

# Get list of all devices
devices = myapi.devices.get_device_list()

# Print table 1 headers
print("="*96)
print("{0:25s}{1:1s}{2:46s}{3:1s}{4:23s}".\
    format("Device Name", "|", "Device Type", "|","Up Time"))
print("-"*96)

# Print table 1 content
for device in devices.response:
    print("{0:25s}{1:1s}{2:46s}{3:1s}{4:23s}".\
        format(device.hostname, "|", device.type, "|", device.upTime))
print("="*96)

# Get health of all clients on Thursday 21st January 2021, 2:27:00 PM ACT Adelaide
# Pass args of timestamp in UNIX epoch milliseconds
clients = myapi.clients.get_overall_client_health(timestamp="1611201420000")

# Print table 2 headers
print("{0:25s}{1:1s}{2:46s}{3:1s}{4:23s}".\
    format("Client Category", "|", "Number of Clients", "|","Clients Score"))
print("-"*96)

# Print table 2 content
for client in clients.response:
    for score in client.scoreDetail:
        print("{0:25s}{1:1s}{2:46s}{3:1s}{4:23s}".\
                format(score.scoreCategory.value, "|", str(score.clientCount), "|", str(score.scoreValue)))
print("="*96) # Bottom border
