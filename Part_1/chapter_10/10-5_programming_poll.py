filename = 'poll.txt'

while True:
	with open(filename, 'a') as file_object:
		reason = input("Why do you like programming? : ")
		file_object.write(reason + "\n")
		print("Welcome " + reason)
		
