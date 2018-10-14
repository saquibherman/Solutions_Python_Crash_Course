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

restaurant1 = Restaurant('Fäviken Magasinet', 'Swedish')
restaurant2 = Restaurant('Mukut', 'Indian')
restaurant3 = Restaurant('Orchid', 'Thai')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
