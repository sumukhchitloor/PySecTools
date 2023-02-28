import os
import sys
import socket

def is_up(host):
    # Set timeout in seconds
    timeout = 1
    try:
        # Try to resolve the host name
        host = socket.gethostbyname(host)
        # Try to connect to the host on port 80
        socket.create_connection((host, 80), timeout)
        return True
    except:
        return False

def scan_ports(host, port_range):
    start, end = [int(x) for x in port_range.split("-")]
    for port in range(start, end+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"{host}:{port} is open")
        s.close()

def scan_range(ip_address, ip_range):
    start, end = [int(x) for x in ip_range.split("-")]
    for i in range(start, end+1):
        host = ip_address.rsplit(".", 1)[0] + "." + str(i)
        if is_up(host):
            print(host + " is up")
            scan_ports_flag = input(f"Do you want to scan ports for {host}? (yes/no): ")
            if scan_ports_flag.lower() == "yes":
                port_range = input("Enter the port range to scan (e.g. 1-65535): ")
                scan_ports(host, port_range)

if __name__ == "__main__":
    # Check if the required arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <ip_address> <range>")
        sys.exit(1)
    ip_address = sys.argv[1]
    ip_range = sys.argv[2]
    scan_range(ip_address, ip_range)
