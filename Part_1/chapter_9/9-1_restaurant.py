class Restaurant():
	"""To model a restaurant"""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""Initializing name and type attributes"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		"""Displaying the name and type attributes"""
		print("name of the restaurant is " + self.restaurant_name)
		print("cuisine type is " + self.cuisine_type)
		
	def open_restaurant(self):
		"""Showing the open/close status of restaurant"""
		print("restaurant is open")

restaurant = Restaurant('mughlai', 'indian')

restaurant.describe_restaurant()
restaurant.open_restaurant()
