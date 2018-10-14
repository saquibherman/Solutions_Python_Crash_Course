favorite_places = {
	'herman' : ['norway', 'portland', 'tokyo'],
	'hasnain' : ['turkey', 'rome', 'madrid'],
	'john' : ['switzerland', 'paris', 'new york'],
	}

for name, places in favorite_places.items():
	print(name.title() + " likes the places ")
	for place in places:
		print("\t" + place)
