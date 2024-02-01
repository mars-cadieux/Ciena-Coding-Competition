assignedIPAddresses = {}



import sys
import re
import time

def ask(inputIP:str) -> str:
	if checkValidIP(inputIP):
		if inputIP in assignedIPAddresses:
			print("This IP address is already assigned.")
		else:
			assignedIPAddresses[inputIP] = "assigned"
	else:
		print("The inputted IP is not valid")

def status(inputIP:str) -> str:
	if(checkValidIP(inputIP)):
		if inputIP in assignedIPAddresses:
			print(inputIP + " ASSIGNED")
		else:
			print(inputIP + " AVAILABLE")


def checkValidIP(inputIP: str) -> bool:
	IPSegments = inputIP.split('.')
	if len(IPSegments) != 4:
		return False
	for segment in IPSegments:
		if not (segment.isnumeric()):
			return False
		if segment < 0 or segment > 255:
			return False
	return True