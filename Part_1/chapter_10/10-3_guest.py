filename = 'guest.txt'

guest_name = input("Enter your name: ")

with open(filename, 'w') as file_object:
	file_object.write(guest_name)
