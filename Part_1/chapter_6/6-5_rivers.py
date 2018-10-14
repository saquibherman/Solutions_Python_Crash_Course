rivers = {
	'nile' : 'egypt',
	'amazon' : 'peru',
	'mississippi' : 'united states',
	'columbia' : 'united states',
	}
	
for river, country in rivers.items():
	print("The " + river.title() + " runs through " + country.title())

print("\nThe name of each river included in the dictionary")
for key in rivers.keys():
	print(key.title())

print("\nThe name of each country included in the dictionary")
for value in set(rivers.values()):
	print(value.title())
