import random

# set an empty array/(list in python)
lottery_numbers = []

count = 0;

while len(lottery_numbers) < 7:

	# generate a random number
	random_number = random.randint(1, 49)

	# if the random number doesn't already exist in the list
	if random_number not in lottery_numbers:

		# add it to the list
		lottery_numbers.append(random_number)

print(lottery_numbers)