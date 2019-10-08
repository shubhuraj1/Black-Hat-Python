import os
import subprocess

host = input("Enter The Host Add:-")
print("."*50)
subprocess.check_call(['nmap','-n','-V','-Pn','-sn','-sL','PE','-PP','-oN', 'host.txt', host])

port_range = input("Enter The Host Add:-")
print("."*50)
subprocess.check_call(['nmap','-p','-l-500','-oN', 'port_range.txt', port_range])
