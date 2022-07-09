import nmap
import re
from collections import OrderedDict


def validate_ip_address(address: str) -> bool:
    match = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", address)

    if bool(match) is False:
        print("IP address {} is not valid".format(address))
        return False

    for part in address.split("."):
        if int(part) < 0 or int(part) > 255:
            print("IP address {} is not valid".format(address))
            return False

    print("IP address {} is valid".format(address))
    return True

# :TODO Finish this function to convert ports to ranges (if it exists)


def validate_ports(port: str) -> bool:
    # convert to list (and int)
    list_of_ports = [int(x) for x in port]
    list_of_ports.sort()

    # catch ranges
    ranges = []
    final = []
    return True


class ScanningService:
    def __init__(self, target: str, ports: str):
        self.target = target if validate_ip_address(target) else False
        self.ports = ports

    def scan(self) -> bool:
        port_scan = nmap.PortScanner()
        port_scan.scan(self.target, self.ports)
        for host in port_scan.all_hosts():
            print(f'Host: {host} ({port_scan[host].hostname()})')
            print(f'State : {port_scan[host].state()}')
            for protocol in port_scan[host].all_protocols():
                print(f'Protocol : {protocol}')

                listening = port_scan[host][protocol].keys()
                # listening.sort()
                for port in listening:
                    print(f'port : {port}\tstate : {port_scan[host][protocol][port]["state"]}')
        return True


