favorite_numbers = {
	'herman' : [19, 12, 30],
	'hasnain' : [17, 2, 15],
	'anu' : [18, 20, 30],
	'aalu' : [20, 12, 29],
	'affu' : [15, 30, 17],
	}

for name, numbers in favorite_numbers.items():
	print(name.title() + "'s favorite numbers are:")
	for number in numbers:
		print("\t\t\t\t" + str(number))

