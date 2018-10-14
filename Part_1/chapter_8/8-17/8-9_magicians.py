def show_magicians(magician_names):
	""""Displays all the magicians name."""
	for name in magician_names:
		print(name.title())
		
names = ['harry blackstone jr.', 'ricky jay', 'derren brown', 
			'harry august jansen', 'david blaine', 'penn & teller', 
			'criss angel', 'david copperfield', 'dynamo', 
			'harry houdini']

show_magicians(names)
