from collections import OrderedDict

glossary = OrderedDict()

glossary['pep'] = 'Python Enhancement Proposal process, the primary mechanism for proposing major new features.'
glossary['list comprehension'] = 'list comprehension is an elegant way to define and create list in Python.'
glossary['tuple'] = 'tuple is immutable unlike lists.'
glossary['slice'] = 'slicing can not only be used for lists, tuples or arrays, but custom data structures as well, with the slice object.'
glossary['zen of python'] = 'the Zen of Python is a collection of 20 software principles that influences the design of python programming language'
glossary['sort()'] = 'sort() method sorts the list permanently'

for keys, values in glossary.items():
	print(keys + "\n    " + values)
