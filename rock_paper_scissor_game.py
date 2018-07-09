#import random library
import random
options = ["r", "p", "s"]
user_play = "y"

#setting counter at 0
Player_Wins = 0
Computer_wins = 0

#set up a while loop to continue to play after each game. While the input is "y" the game will ask for a choice and the IF statement will execute
while user_play == "y":
	#Ask the user for information and specify how input should be given.
	user_choice = input("May your choice: (r)ock, (p)aper, (s)cissors ?")
	# using random choice to iterate through list
	computer_choice = random.choice(options)
#use if conditionals to determine which outcome is true to determine winner
	if(user_choice =="r" and computer_choice == "p"):
		print("You choose rock and Computer chose paper")
		print("Sorry, You lose.")
		if user_choice == "r":
			Computer_wins += 1
	elif ( user_choice == "r" and computer_choice == "s"):
		print("You choose rock and Computer chose scissors")
		print("You win!")
		if user_choice == "r":
			Player_Wins +=1
	elif (user_choice == "r" and computer_choice == "r"):
		print("You choose rock and Computer chose rock")
		print("You both tie")
	elif(user_choice == "p" and computer_choice =="p"):
		print("You choose paper and Computer chose paper")
		print("You both tie")
	elif(user_choice == "p" and computer_choice =="r"):
		print("You choose paper and Computer chose rock")
		print("You win!")
		if user_choice =="p":
			Player_Wins +=1
	elif(user_choice == "p" and computer_choice == "s"):
		print("You choose paper and Computer chose scissors")
		print("Sorry, You lose.")
		if user_choice =="p":
			Computer_wins +=1
	elif(user_choice == "s" and computer_choice =="p"):
		print("You choose scissors and Computer chose paper")
		print("You win!")
		if user_choice == "s":
			Player_Wins +=1
	elif(user_choice == "s" and computer_choice == "s"):
		print("You choose scissors and Computer chose scissors")
		print("You both tie")
	elif(user_choice == "s" and computer_choice == "r"):
		print("You choose scissors and Computer chose rock")
		print("Sorry, You lose.")
		if user_choice == "s":
			Computer_wins +=1
	else:
		print("Please select (r) or (s) or (p) to play")
	#Added Counter to determine winner based who gets to 3 wins first.
	if Player_Wins == 3:
		print("Player you are the winner")
		break
	if Computer_wins == 3:
		print("Computer wins the whole Game")
		break
	user_play = input("Continue to play (y)es or (n)o?")
#Added end game result
if user_play == "n":
	print("Thank you for playing")
