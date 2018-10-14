import datetime
prompt = "Enter 'quit' to end the program."
prompt += "\nPlease enter your age: "
print("Ticket can't be issued on Monday.")
active = True
day = datetime.datetime.today().weekday()
while active and day > 0:
	age = input(prompt)
	if (age == 'quit'):
		break
	age = int(age)

	if age < 3:
		print("The ticket is free!")
	elif age >= 3 and age <= 12:
		print("The ticket is $10!")
	else:
		print("The ticket is $15!")

