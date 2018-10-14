import json

favorite_number = input("Input your favorite number : ")

filename = 'number.json'

with open(filename, 'w') as f_obj:
	json.dump(favorite_number, f_obj)
