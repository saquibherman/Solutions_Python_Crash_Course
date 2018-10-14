filename = 'guest_book.txt'

while True:
	with open(filename, 'a') as file_object:
		guest_name = input("Enter your name: ")
		file_object.write(guest_name + "\n")
		print("Welcome " + guest_name)
		
