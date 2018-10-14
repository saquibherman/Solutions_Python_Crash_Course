from user import User	

class Admin(User):
	"""admin class for administrators"""
	
	def __init__(self, first_name, last_name, age, sex, location):
		super().__init__(first_name, last_name, age, sex, location)
		self.privileges = Privilege()
				
class Privilege():
	"""A simple attempt to model Privileges"""
	
	privileges = ['can add post', 'can delete post', 'can ban user']
	
	def show_privileges(self):
		print(self.privileges)
