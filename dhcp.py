assignedIPAddresses = {}
retiredIPAddresses = []
ipGenerator = [0,0,0,0]
currIndex = 3

import sys
import time

def ask(inputIP:str) -> str:
	if checkValidIP(inputIP):
		if inputIP in assignedIPAddresses:
			print("This IP address is already assigned.")
		else:
			assignedIPAddresses[inputIP] = time.time()
			print("Offer " + inputIP)
	else:
		print("The inputted string does not resemble an IP address.")

def status(inputIP:str) -> str:
	if(checkValidIP(inputIP)):
		if inputIP in assignedIPAddresses:
			print(inputIP + " ASSIGNED")
		else:
			print(inputIP + " AVAILABLE")
	else:
		print("The inputted string does not resemble an IP address.")

def release(inputIP:str) -> str:
	if(checkValidIP(inputIP)):
		if inputIP in assignedIPAddresses:
			assignedIPAddresses.pop(inputIP)
			retiredIPAddresses.append(inputIP)
			print("RELEASED for " + inputIP)
		else:
			print("This IP address is not assigned.")
	else:
		print("The inputted string does not resemble an IP address.")

def renew(inputIP:str) -> str:
	if(checkValidIP(inputIP)):
		if inputIP in assignedIPAddresses:
			assignedIPAddresses[inputIP] = time.time()
			print("RENEWED for " + inputIP)
		else:
			print("This IP address is not assigned.")
	else:
		print("The inputted string does not resemble an IP address.")


def checkValidIP(inputIP: str) -> bool:
	IPSegments = inputIP.split('.')
	if len(IPSegments) != 4:
		return False
	for segment in IPSegments:
		if not (segment.isnumeric()):
			return False
		if int(segment) < 0 or int(segment) > 255:
			return False
	return True

def generateIP() -> str:
	if len(retiredIPAddresses) > 0:
		newIP = retiredIPAddresses[0]
		retiredIPAddresses.remove(newIP)
		return newIP
	else:
		if ipGenerator[currIndex] > 255:
			ipGenerator[currIndex] = 0
			currIndex -= 1
			ipGenerator[currIndex] 


def main():
	print("Welcome to the DHCP server! Type in a command to get started. Type 0 to exit.\n")
	userInput = input("> ")
	while(userInput != "0"):
		if userInput.startswith("ASK"):
			ask(userInput[4:])
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




if __name__ == "__main__":
    main()