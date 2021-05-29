from classes.ChooseVPN import ChooseVPN

if __name__ == "__main__":
    vpnConnections = ChooseVPN()
    vpnConnections.setVPNConnection()
    vpnConnection = vpnConnections.getVPNConnection()
    print(vpnConnection)
