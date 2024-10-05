import json
import netmiko
from netmiko import ConnectHandler

# Parse the Data from Json file to python Var
with open('configcisco1.json') as config_file:
    config = json.load(config_file)
    
# Extract the configuration data:
device_info = config['device']
interface_config = config['interface_config']
new_hostname = config['new_hostname']

# Connect to Cisco via SSH:
net_connect = ConnectHandler(**device_info)

# Enter Enable mode
net_connect.enable()

# Build the configuration:
commands = [
    f"interface {interface_config['interface']}",
    f"ip address {interface_config['new_ip']} {interface_config['subnet_mask']}",
    "no shutdown", # make sure its UP
    "exit",
    f"hostname {new_hostname}"
]

# send the json Parsed Python file to Cisco
output = net_connect.send_config_set(commands)
print(output)

# always close the connection:
net_connect.disconnect
