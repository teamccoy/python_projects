#Password generator, asks for inputs from the user and will generate password
import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
number = input("How many passwords do you need to generate? ")
#cast the input as a integer
number = int(number)
length = input("What is the password length needed? ")
#cast the input as a integer
length = int(length)
for character in range(number):
	password = '' 
	for item in range(length):
		password += random.choice(chars)
	print(password)
