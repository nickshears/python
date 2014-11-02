# define a list of vowels with a corresponding count
vowels = {'a':10, 'e':11, 'i':15, 'o':17, 'u':3}

# define a word anything other than stop to start the loop
word = 'start'

while (word != "stop"):

	word = input("Enter a word to input: ")

	# loop through each letter in the word
	for letter in word:

		# lowercase each letter the user has input to see if its a vowel
		low_letter = letter.lower()

		if (low_letter in vowels):

			# if its a vowel, then
			vowels[low_letter] = vowels[low_letter]+1


for vowel, count in vowels.items():

	upper_vowel = vowel.upper()

	print("Instances of {0}/{1}: {2}".format(vowel, upper_vowel, count))