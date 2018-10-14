koby = {
	'kind' : 'dog',
	'owner name' : 'affu',
	}

margo = {
	'kind' : 'dog',
	'owner name' : 'noor',
	}
	
pixie = {
	'kind' : 'cat',
	'owner name' : 'aalu',
	}
	
pets = [koby, margo, pixie]
for pet in pets:
	print("\n")
	for value in pet.values():
		print(value)
