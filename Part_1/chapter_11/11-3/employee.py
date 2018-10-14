class Employee():
	"""Contains Employee Details"""
	
	def __init__(self, first_name, last_name, annual_salary):
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = annual_salary

	def give_raise(self, increase = 5000):
		self.annual_salary += increase
		return self.annual_salary
