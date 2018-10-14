class Restaurant():
	"""To model a restaurant"""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""Initializing name and type attributes"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def describe_restaurant(self):
		"""Displaying the name and type attributes"""
		print("name of the restaurant is " + self.restaurant_name)
		print("cuisine type is " + self.cuisine_type)
		
	def open_restaurant(self):
		"""Showing the open/close status of restaurant"""
		print("restaurant is open")
		
	def set_number_served(self, number_served):
		"""set the number of customers served"""
		self.number_served = number_served
		
	def increment_number_served(self, number_served):
		"""increment the number of customers served"""
		self.number_served += number_served

class IceCreamStand(Restaurant):
	"""Inherits from the Restaurant class"""
	
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['vanilla']
		
	def display_flavors(self):
		print(self.flavors)
		
icecream = IceCreamStand('mughlai', 'indian')
print(icecream.display_flavors())
