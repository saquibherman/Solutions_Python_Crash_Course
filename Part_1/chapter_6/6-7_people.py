noor = {
	'first_name' : 'noor',
	'last_name' : 'khan',
	'age' : '6',
	'city' : 'stockholm',
	}

herman = {
	'first_name' : 'saquib',
	'last_name' : 'herman',
	'age' : '37',
	'city' : 'stockholm',
	}

people = [noor, herman]

for person in people:
	print("\n")
	for key, value in person.items():
		print(key + " is " + value)
