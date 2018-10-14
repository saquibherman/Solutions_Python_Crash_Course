while True:
	number_1 = input("Enter first number: ")
	number_2 = input("Enter second number: ")

	try:
		x = int(number_1) 
		y = int(number_2)
	except ValueError:
		print("Please enter numerical values")
	else:
		result = x + y
		print("sum is: " + str(result))
