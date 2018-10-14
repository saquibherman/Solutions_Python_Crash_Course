def count_common_words(filename):
	"""Count occurances of the word 'the' in the file"""
	try:
		with open(filename, encoding='utf-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exist."
		print(msg)
	else:
		# Count the number of 'the' in the file
		print("the word 'the' occurs in file " + filename + " is " + str(contents.lower().count('the')) + " times")

filenames = ['Luncheons.txt', 'The_Story_of_the_Highland_Regiments.txt', 'Decisive_Battles_of_America.txt']
for filename in filenames:
	count_common_words(filename)
