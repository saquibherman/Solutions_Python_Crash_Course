current_users = ['majid', 'saquib', 'reshma', 'Noor', 'Anum']

new_users = ['noor', 'ANUM', 'aaliya', 'afsheen', 'reshma']

for user in new_users:
	if user.lower() in [cur_user.lower() for cur_user in current_users]:
		print("The username " + user + " is already been used, you will need to enter a new username!")
	else:
		print("The username " + user + " is available")
