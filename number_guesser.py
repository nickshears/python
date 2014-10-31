import random

play_again = True;

while (play_again):

	# generate a random number
	correct_number = random.randint(0, 100)

	# fake a guessed number that's wrong so the loop can start
	guessed_number    = None
	number_of_guesses = 0
	
	while (guessed_number != correct_number):

		guessed_number = int(input("Try and guess the correct number between 0 and 100"))
		number_of_guesses = number_of_guesses+1

		# calculate the distance between the 2 numbers first to avoid long conditions
		if correct_number>guessed_number:
			difference = correct_number-guessed_number
		else:
			difference = guessed_number-correct_number

		if (difference > 10):
			print("cold")
		else:
			if (difference >= 5 and difference <= 10):
				print("warm")
			else:
				# it can only be hot now
				print("hot")

	print("you took {0} guesses to get the correct number of {1}".format(number_of_guesses, correct_number))

	decision = input("play again? y/n")

	if (decision != 'y'):

		play_again = False
