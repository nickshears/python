string = input("Please enter a string")

number_of_letters = 0
number_of_digits  = 0
count = 0

while (len(string) > count):
	
	char = string[count]

	if (char.isdigit()):

		number_of_digits = number_of_digits+1

	if (char.isalpha()):

		number_of_letters = number_of_letters+1

	count = count+1

print("numbers: "+str(number_of_digits))

print("letters: "+str(number_of_letters))