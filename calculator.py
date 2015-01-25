from calculatorFunctions import *

print("Hello and Welcome to Python Calculator")

print("Choose an option!")
printMenu()

userChoice = int(userInput())

while(userChoice != 6):
	if(userChoice == 1):
		addCall()
	if(userChoice == 2):
		subCall()
	if(userChoice == 3):
		multiCall()
	if(userChoice == 4):
		divideCall()
	if(userChoice == 5):
		reverseString()
	print("")
	printMenu()
	userChoice = int(userInput())
