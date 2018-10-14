import json

filename = 'number.json'

try:
	with open(filename) as f_obj:
		number = json.load(f_obj)
except FileNotFoundError:
	favorite_number = input("Enter your favorite number: ")
	with open(filename, 'w') as f_obj:
		json.dump(favorite_number, f_obj)
else:
	print("I know your favorite number! It's " + number + " .")
