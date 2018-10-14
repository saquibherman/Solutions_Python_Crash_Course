prompt = "\nPlease enter your age: "

while True:
	age = input(prompt)
	age = int(age)
	
	if age < 3:
		print("The ticket is free!")
	elif age >= 3 and age <= 12:
		print("The ticket is $10!")
	else:
		print("The ticket is $15!")
