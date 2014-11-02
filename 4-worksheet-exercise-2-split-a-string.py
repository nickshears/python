comma_string = input("Please enter a string of items: ")

count = 0;

word_list = []
current_word = '';

string_length = len(comma_string)

while (string_length > count):

	# the current character
	char = comma_string[count]

	# if the character is a comma
	if (char == ','):

		# then a new word has started, put the current word into a list
		word_list.append(current_word)

		# and reset the current word string
		current_word = ''

	else:

		# append the char to the current word as its not a comma 
		current_word+= char

		# then if this is the final loop, add the current word because we won't encounter another comma
		if (count == string_length-1):

			word_list.append(current_word)

	count = count+1

item_count = len(word_list)
print(str(item_count)+" items total");

for item in word_list:

	print(item)