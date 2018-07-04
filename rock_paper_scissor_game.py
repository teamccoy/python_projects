#import random library
import random
options = ["r", "p", "s"]
user_play = "y"
# using random choice to iterate through list
computer_choice = random.choice(options)
#Ask the user for information and specify how input should be given.


#set up a while loop to continue to play after each game. While the input is "y" the game will ask for a choice and the IF statement will execute
while user_play == "y":
	user_choice = input("May your choice: (r)ock, (p)aper, (s)cissors ?")
#use if conditionals to determine which outcome is true to determine winner
	if(user_choice =="r" and computer_choice == "p"):
		print("You choose rock and Computer chose paper")
		print("Sorry, You lose.")
	elif ( user_choice == "r" and computer_choice == "s"):
		print("You choose rock and Computer chose scissors")
		print("You win!")
	elif (user_choice == "r" and computer_choice == "r"):
		print("You choose rock and Computer chose rock")
		print("You both tie")
	elif(user_choice == "p" and computer_choice =="p"):
		print("You choose paper and Computer chose paper")
		print("You both tie")
	elif(user_choice == "p" and computer_choice =="r"):
		print("You choose paper and Computer chose rock")
		print("You win!")
	elif(user_choice == "p" and computer_choice == "s"):
		print("You choose paper and Computer chose scissors")
		print("Sorry, You lose.")
	elif(user_choice == "s" and computer_choice =="p"):
		print("You choose scissors and Computer chose paper")
		print("You win!")
	elif(user_choice == "s" and computer_choice == "s"):
		print("You choose scissors and Computer chose scissors")
		print("You both tie")
	elif(user_choice == "s" and computer_choice == "r"):
		print("You choose scissors and Computer chose rock")
		print("Sorry, You lose.")
	user_play = input("Continue to play (y)es or (n)o?")
#Added end game result
if user_play == "n":
	print("Thank you for playing")