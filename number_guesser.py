import random

# generate a random number
correct_number = random.randint(0, 100)

# fake a guessed number that's wrong so the loop can start
guessed_number = None

while (guessed_number != correct_number):

	guessed_number = int(input("Take a guess"))

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


print("your guess is correct!")
