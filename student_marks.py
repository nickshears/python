# create a list of acceptable numbers
acceptable_range = range(0, 100)

# define an empty list
numbers = []

# define a random acceptable number so the loop can start
number = 0

# keep asking the user for a number and appending it as long as they do not enter "-1"
while number != -1:

	number = int(input("please enter a number"))

	if number in acceptable_range:

		numbers.append(number)

	else:
		# not sure why this is neccesary :s
		if number != -1:

			print("Number is not within the range of 0-100")


# if the program made it this far, then its time to do some calculations

# calculate the lowest and highest numbers entered
lowest_number  = 100
highest_number = 0
total_value = 0

for number in numbers:

	if number < lowest_number:

		lowest_number = number

	if number > highest_number:

		highest_number = number

	total_value = total_value+number

# calculate mean value, average of all numbers entered
mean_value = total_value/len(numbers)

print("Exiting. Mean value is "+str(mean_value)+", Minimum is "+str(lowest_number)+", Maximum is "+str(highest_number))
