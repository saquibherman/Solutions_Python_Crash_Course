def make_great(magician_names):
	""""Adds string 'Great' with magician names."""
	great_names = []
	while magician_names:
		names = "Great " + magician_names.pop()
		great_names.append(names)
	return great_names

	
def show_magicians(magician_names):
	"""Displays all the magician names."""
	for name in magician_names:
		print(name.title())

		
list_of_magicians = ['harry blackstone jr.', 'ricky jay', 
						'derren brown', 'harry august jansen', 
						'david blaine', 'penn & teller', 'criss angel', 
						'david copperfield', 'dynamo', 'harry houdini']

						
new_list_of_magicians = make_great(list_of_magicians[:])


show_magicians(list_of_magicians)
show_magicians(new_list_of_magicians)


