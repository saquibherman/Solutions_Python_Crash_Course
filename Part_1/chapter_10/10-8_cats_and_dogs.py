cats_file = 'cats.txt'
dogs_file = 'dogs.txt'

filenames = [cats_file, dogs_file]
for files in filenames:
	try:
		with open(files,'r') as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		print("File" + files + " is missing")
	else:
		print(contents)
	
