class ChooseVPN:

    def __init__(self):
        self.vpnConnections = ["Openvpn"]
        self.__vpnConnection = None

    # Take the VPN connection from the user
    def setVPNConnection(self):
        print("VPN connection")
        for key, vpnConnection in enumerate(self.vpnConnections):
            print(f"{key + 1}-{vpnConnection}")
        getOption = int(input("Enter Connection code: "))
        if getOption == 1:
            self.__vpnConnection = "Openvpn"

    # Return the VPN connection

    def getVPNConnection(self) -> str:
        return self.__vpnConnection
