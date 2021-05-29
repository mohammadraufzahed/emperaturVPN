from classes.ChooseVPN import ChooseVPN
from classes.Connections.OpenVpn import OpenVpn

if __name__ == "__main__":
    vpnConnections = ChooseVPN()
    vpnConnections.setVPNConnection()
    vpnConnection = vpnConnections.getVPNConnection()
    if vpnConnection == "Openvpn":
        openvpn = OpenVpn()
