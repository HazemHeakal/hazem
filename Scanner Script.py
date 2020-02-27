#!/bin/python3

import sys  #allows us to enter command line arguments, among other things
import socket
from datetime import datetime

#Define our target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate the hostname to IPV4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit()

#Add a pretty banner

print("-" * 50)
print("Scanning Target " + target)
print("Time Started: " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,88):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(.2) #is a float
		result = s.connect_ex((target , port)) #returns error indecator
		print("Checking port {}".format(port))
		if result == 0:
			print("port {} is open".format(port))
		s.close()

except KeyboardInterrupt :
	print("\nExiting program.")
	sys.exit()

except socket.gaierror :
	print("\nHostname could not be resolved")
	sys.exit()

except socket.error :
	print("\nCould not connect to server")
	sys.exit()
