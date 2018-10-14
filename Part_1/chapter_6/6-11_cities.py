cities = {
	'stockholm' : { 'country' : 'sweden', 'population' : '952058', 'fact' : 'stockholm is one of the most crowded museum-cities in the world with around 100 museums.' },
	'paris' : { 'country' : 'france', 'population' : '2206488', 'fact' : 'major centres of finance, commerce, fashion, science, music and painting.' },
	'new york' : { 'country' : 'united states', 'population' : '8175133', 'fact' : 'new york city has been described as the cultural capital of the world.' },
	}

for city, details in cities.items():
	print("know about the city " + city.title())
	for key,value in details.items():
		print("\t\t" + key + " : " + value)
		
