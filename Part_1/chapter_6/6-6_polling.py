people = ['herman', 'jen', 'sarah', 'john', 'edward', 'phil']

favorite_language = {
	'jen' : 'python',
	'sarah': 'c',
	'edward' : 'ruby',
	'phil' : 'python',
	}

for name in people:
	if name in favorite_language.keys():
		print(name.title() + ", thanks for participating in the poll!")
	else:
		print(name.title() + ", please take our poll!") 
