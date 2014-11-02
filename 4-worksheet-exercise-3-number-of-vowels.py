# define a dictionary of vowels with a corresponding count
vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

# define a word anything other than stop to start the loop
word = 'start'

while (word != "stop"):

	word = input("Enter a word to input: ")

	# loop through each letter in the word
	for letter in word:

		# lowercase each letter the user has input to see if its a vowel in the dictionary
		low_letter = letter.lower()

		if (low_letter in vowels):

			# if its a vowel, then incremenet the count for that letter
			vowels[low_letter] = vowels[low_letter]+1


# only problem is the ordering of the list, would be better if a, e, i, o, u
for vowel, count in vowels.items():

	upper_vowel = vowel.upper()

	print("Instances of {0}/{1}: {2}".format(vowel, upper_vowel, count))