username = input("What is your name?")

numbers = []
count = 1;
while (count < 3):

	count_string = str(count);
	number = input("Please provide number "+count_string);
	
	try:
		number = int(number)
		numbers.append(number);

	except:
		print(number+" is not a number, please try again using 2 numbers")	

	count = count+1;

