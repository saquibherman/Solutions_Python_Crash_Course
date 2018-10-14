people = ['herman', 'jen', 'sarah', 'john', 'edward', 'phil']

favorite_language = {
	'jen' : {'static' : ['c++', 'java'], 'dynamic' : ['python', 'java script'],},
	'sarah': {'static' : ['c#', 'c'], 'dynamic' : ['lua', 'java script'],},
	'edward' : {'static' : ['c', 'c++'], 'dynamic' : ['python', 'lua'],},
	'phil' : {'static' : ['c#', 'java'], 'dynamic' : ['python', 'ruby'],},
	}

for name in people:
	if name in favorite_language.keys():
		print(name.title() + ", thanks for participating in the poll!")
		print("your favorite languages are ")
		print("static languages are")
		print(name[])
	else:
		print(name.title() + ", please take our poll!") 
