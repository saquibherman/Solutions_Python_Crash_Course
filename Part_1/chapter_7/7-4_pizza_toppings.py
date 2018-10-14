prompt = "\nPlease enter your pizza toppings." 	
prompt += "\nEnter 'quit' to end the program. "

while True:
	message = input(prompt)
	
	if message == 'quit':
		break
	else:
		print("I'll add " + message + " topping to your pizza")
		
