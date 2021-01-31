class Router:
    def __init__(self):
        '''This function serves to initialise a Router object
        No initial argument is needed.
        Enter arguments only when prompted'''
        self.hostname = input('Hostname: ')
        self.model = input('Model: ')
        self.swversion = input('Software version: ')
        self.ip_addr = input('IPv4 address: ')

    def printdesc(self):
        '''This function serves to print description of the device.
        No initial argument is needed'''
        print(self.hostname)
        print(f'Router Model                : {self.model}')
        print(f'Software Version            : {self.swversion}')
        print(f'Router Management Address   : {self.ip_addr}')

    
class Switch(Router):
    def printdesc(self):
        '''This function serves to print description of the device.
        No initial argument is needed'''
        print(self.hostname)
        print(f'Switch Model                : {self.model}')
        print(f'Software Version            : {self.swversion}')
        print(f'Switch Management Address   : {self.ip_addr}')

