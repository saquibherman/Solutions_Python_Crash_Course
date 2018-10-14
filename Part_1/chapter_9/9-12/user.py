class User():
	"""A simple template to represent user"""
	
	def __init__(self, first_name, last_name, age, sex, location):
		"""Initialize attributes to describe user."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.sex = sex
		self.location = location
		self.login_attempts = 0
		
		
	def describe_user(self):
		"""Describes users attributes"""
		print("User's information:")
		print("\t" + "First name is " + self.first_name)
		print("\t" + "Last name is " + self.last_name)
		print("\t" + "Age is " + str(self.age))
		print("\t" + "Sex is " + self.sex)
		print("\t" + "Locaiton is " + self.location) 
		
	def greet_user(self):
		"""Greets user"""
		print("Hello " + self.first_name + "\n")
		
	def increment_login_attempts(self):
		"""Increase login attempt value by 1 """
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		"""Increase login attempt value by 1 """
		self.login_attempts = 0	
