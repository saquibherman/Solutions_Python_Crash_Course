def build_profile(first, last, **user_info):
	""""Build a dictionary containig everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('saquib', 'herman', location = 'malmo', occupation = 'scientist', department = 'compter science')

print(user_profile)
