#!/usr/bin/env python3

def getCommands(vlan, name):
    """Get commands to configure a VLAN

    Args:
        vlan (int): vlan id
        name (str): name of the VLAN
    
    Returns:
        A list of commands in returned.
    """
    commands = []
    commands.append('vlan ' + vlan)
    commands.append('name ' + name)
    return commands

def pushCommands(device, commands):
    print('Connecting to device:', device)
    for cmd in commands:
        print('Sending command:', cmd)


if __name__ == '__main__':
    devices = ['switch1', 'switch2', 'switch3']
    vlans = [{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'}, {'id': '30', 'name': 'WLAN'}]

    for vlan in vlans:
        id = vlan.get('id')
        name = vlan.get('name')
        print('\n')
        print('Configuring vlan:', id)

        commands = getCommands(id, name)

        for device in devices:
            pushCommands(device, commands)
            print('\n')

