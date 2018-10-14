glossary = {
	'pep' : 'Python Enhancement Proposal process, the primary mechanism for proposing major new features.',
	'list comprehension' : 'list comprehension is an elegant way to define and create list in Python.',
	'tuple' : 'tuple is immutable unlike lists.',
	'slice' : 'slicing can not only be used for lists, tuples or arrays, but custom data structures as well, with the slice object.',
	'zen of python' : 'the Zen of Python is a collection of 20 software principles that influences the design of python programming language',
	'sort()' : 'sort() method sorts the list permanently'
	}

for keys, values in glossary.items():
	print(keys + "\n    " + values)
