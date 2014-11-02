items = input("Please enter a string of items: ")

count = 0;

# this list will end up containing each item that has been seperated by a comma
word_list = []

# append characters to this word through the loop, and reset it when a comma occurs
current_word = '';

items_length = len(items)

while (items_length > count):

	# the current character
	char = items[count]

	# if the character is a comma
	if (char == ','):

		# then a new word has started, so put the current word variable into a list
		word_list.append(current_word)

		# and reset the current word string to start building the next word
		current_word = ''

	# if the character is not a comma
	else:

		# append the character to the current word
		current_word+= char

		# and if this is the final loop, add the current word because we won't encounter another comma
		if (count == items_length-1):

			word_list.append(current_word)

	count = count+1

item_count = len(word_list)
print(str(item_count)+" items total");

for item in word_list:

	print(item)