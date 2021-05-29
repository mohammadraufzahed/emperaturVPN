import stdiomask
import sys
import pexpect
import time


class OpenVpn:
    def __init__(self):
        self.__servers = [
            {
                "country": "Canada",
                "serverCount": 2
            }, {
                "country": "England",
                "serverCount": 3
            }, {
                "country": "German",
                "serverCount": 2
            }, {
                "country": "Netherland",
                "serverCount": 4
            }, {
                "country": "Singapore",
                "serverCount": 1
            }, {
                "country": "Turkey",
                "serverCount": 1
            }, {
                "country": "USA",
                "serverCount": 1
            },
        ]
        self.__connectionTypes = [
            "UDP",
            "TCP"
        ]
        self.__location = self.__getLocation()
        self.__connectionType = self.__getConnectionType()
        self.__connect(self.__location, self.__connectionType)

    # Get the location
    def __getLocation(self):
        print("Locations")
        for key, country in enumerate(self.__servers):
            print(f"{key + 1}-{country['country']}")
        userInput = int(input("Enter the location code: "))
        return self.__servers[userInput - 1]

    # Get Connection type
    def __getConnectionType(self):
        print("Connection Type")
        for key, connection in enumerate(self.__connectionTypes):
            print(f"{key + 1}-{connection}")
        connectionType = int(input("Enter the connection type: "))
        if connectionType == 1:
            connectionType = "UDP"
        elif connectionType == 2:
            connectionType = "TCP"
        else:
            print("You Entered wrong option")
            sys.exit(1)

        return connectionType
    # Connect to the OpenVpn Server

    def __connect(self, location, connectionType):
        # If the country had 1 server connect to it directly
        if(location['serverCount'] == 1):
            try:
                # Spawn the process
                process = pexpect.spawn(
                    f"openvpn --config 'src/configs/{location['country'].upper()}/{connectionType}.ovpn'")
                # Handle the inputs
                self.__handleAuthInputs(process)
                process.expect("Initialization")
                print('Connected')
            except pexpect.EOF:
                process.kill(0)
                print("Connection lost")
                sys.exit(1)
            try:
                while True:
                    time.sleep(6000)
            except KeyboardInterrupt:
                process.kill(0)
                print("Connection closed")
        else:
            try:
                # Get the server number
                server = self.__getServerNumber(
                    location['serverCount'], location['country'])
                # Spawn the process
                process = pexpect.spawn(
                    f"openvpn --config 'src/configs/{location['country'].upper()}/{server}/{connectionType}.ovpn'")
                # Handle the inputs
                self.__handleAuthInputs(process)
                process.expect("Initialization")
                print('Connected')
            except pexpect.EOF:
                process.kill(0)
                print("Connection lost")
                sys.exit(1)
            try:
                while True:
                    time.sleep(6000)
            except KeyboardInterrupt:
                process.kill(0)
                print("Connection closed")

    # Handle the inputs

    def __handleAuthInputs(self, process):
        username = input("Please enter your username: ")
        password = stdiomask.getpass(prompt="Please enter your password: ")
        # Handle the username input
        process.expect("Enter Auth Username:")
        process.sendline(username)
        # Handle the password input
        process.expect("Enter Auth Password:")
        process.sendline(password)

    # Get the server number
    def __getServerNumber(self, serverCount, country):
        print("Server number")
        for count in range(1, serverCount + 1):
            print(f"{count}-{country} #{count}")
        return input("Enter the server number: ")
