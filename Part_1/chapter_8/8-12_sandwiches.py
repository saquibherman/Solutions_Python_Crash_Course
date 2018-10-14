def make_sandwiches(*items):
	print("\nThe sandwich you ordered has the following items in it.")
	for item in items:
		print(item)
	
make_sandwiches('cheese')
make_sandwiches('butter', 'potato')
