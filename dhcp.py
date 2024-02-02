#written by Mars Cadieux
assignedIPAddresses = {}
retiredIPAddresses = []
ipGenerator = [0,0,0,0]

#written by Mars Cadieux
import sys
import time
from datetime import datetime

#written by Mars Cadieux
def ask() -> str:
	newIP = generateIP()
	if newIP == "-1":
			print("No available IP addresses. Please try again later.")
	else:
		assignedIPAddresses[newIP] = datetime.now()
		print("Offer " + newIP)

#written by Mars Cadieux
def status(inputIP:str) -> str:
	if(checkValidIP(inputIP)):
		if inputIP in assignedIPAddresses:
			if (datetime.now() - assignedIPAddresses[inputIP]).seconds < 60:
				print(inputIP + " ASSIGNED")
			else:
				assignedIPAddresses.pop(inputIP)
				retiredIPAddresses.append(inputIP)
				print(inputIP + " AVAILABLE")
		else:
			print(inputIP + " AVAILABLE")
	else:
		print("The inputted string does not resemble an IP address.")

#written by Mars Cadieux
def release(inputIP:str) -> str:
	if(checkValidIP(inputIP)):
		#IP is in our assigned IPs and its timer hasn't expired. we want to release it
		if inputIP in assignedIPAddresses and (datetime.now() - assignedIPAddresses[inputIP]).seconds < 60:
			assignedIPAddresses.pop(inputIP)
			retiredIPAddresses.append(inputIP)
			print("RELEASED for " + inputIP)
		#IP is in our assigned IPs but its timer has expired, so it's technically no longer an assigned IP. we want to alert the user that it is not assigned, and remove it from our assigned IPs
		elif inputIP in assignedIPAddresses and (datetime.now() - assignedIPAddresses[inputIP]).seconds >= 60:
			assignedIPAddresses.pop(inputIP)
			retiredIPAddresses.append(inputIP)
			print("This IP address is not assigned.")
		else:
			print("This IP address is not assigned.")
	else:
		print("The inputted string does not resemble an IP address.")

#written by Mars Cadieux
def renew(inputIP:str) -> str:
	if(checkValidIP(inputIP)):
		if inputIP in assignedIPAddresses:
			assignedIPAddresses[inputIP] = time.time()
			print("RENEWED for " + inputIP)
		else:
			print("This IP address is not assigned.")
	else:
		print("The inputted string does not resemble an IP address.")

#helper function to check if user inputted IP is valid
def checkValidIP(inputIP: str) -> bool:
	#first, split the user input on the '.' symbol. we should get an array with four entries (which we'll call segments)
	IPSegments = inputIP.split('.')
	#if we don't have four string segments, we know this is not an IP address
	if len(IPSegments) != 4:
		return False
	for segment in IPSegments:
		#if the segment isn't an integer, return false
		if not (segment.isnumeric()):
			return False
		#if it is an integer but is not in the valid range of 0-255, return false
		if int(segment) < 0 or int(segment) > 255:
			return False
	return True

#written by Mars Cadieux
def generateIP() -> str:
	#first, if we have any retired IP addresses, use them instead of generating a new one
	if len(retiredIPAddresses) > 0:
		newIP = retiredIPAddresses[0]
		retiredIPAddresses.remove(newIP)
		return newIP
	else:
		if ipGenerator[3] > 255:
			ipGenerator[3] = 0
			ipGenerator[2] += 1
			if ipGenerator[2] > 255:
				ipGenerator[2] = 0
				ipGenerator[1] += 1
				if ipGenerator[1] > 255:
					ipGenerator[1] = 0
					ipGenerator[0] += 1
					if ipGenerator[1] > 255:
						return "-1"
		generatedIP = str(ipGenerator[0]) + '.' + str(ipGenerator[1]) + '.' + str(ipGenerator[2]) + '.' + str(ipGenerator[3])
		ipGenerator[3] += 1
		return generatedIP

#written by Mars Cadieux
def main():
	print("Welcome to the DHCP server! Type in a command to get started. Type 0 to exit.\n")
	userInput = input("> ")
	while(userInput != "0"):
		if userInput.startswith("ASK"):
			ask()
			userInput = input("> ")
		elif userInput.startswith("RENEW"):
			renew(userInput[6:])
			userInput = input("> ")
		elif userInput.startswith("RELEASE"):
			release(userInput[8:])
			userInput = input("> ")
		elif userInput.startswith("STATUS"):
			status(userInput[7:])
			userInput = input("> ")
		else:
			print("Invalid input")
			userInput = input("> ")

#written by Mars Cadieux
if __name__ == "__main__":
    main()