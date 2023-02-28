import subprocess
import re

def change_mac_address(interface, new_mac):
    # Shut down the interface
    subprocess.call(["ifconfig", interface, "down"])
    # Change the MAC address
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    # Bring up the interface
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac_address(interface):
    # Run the ifconfig command and capture the output
    output = subprocess.check_output(["ifconfig", interface])
    # Search for the MAC address in the output using a regular expression
    mac_address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
    if mac_address_search:
        return mac_address_search.group(0)
    else:
        return None

if __name__ == "__main__":
    # Get the interface name and new MAC address from the user
    interface = input("Enter the interface name: ")
    new_mac = input("Enter the new MAC address: ")

    # Print the current MAC address
    print("Current MAC address: " + str(get_current_mac_address(interface)))

    # Change the MAC address
    change_mac_address(interface, new_mac)

    # Print the new MAC address
    print("New MAC address: " + str(get_current_mac_address(interface)))
