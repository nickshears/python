string = input("Please enter a string")

number_of_letters = 0
number_of_digits  = 0

for letter in string:

	if (letter.isdigit()):

		number_of_digits = number_of_digits+1

	if (letter.isalpha()):

		number_of_letters = number_of_letters+1

print("numbers: "+str(number_of_digits))
print("letters: "+str(number_of_letters))