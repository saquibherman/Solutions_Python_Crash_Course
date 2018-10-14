def make_car(manufacturer, model_name, **car_info):
	""""Build a dictionary containig everything we know about a car."""
	car = {}
	car['first_name'] = manufacturer
	car['last_name'] = model_name
	for key, value in car_info.items():
		car[key] = value
	return car
	
car = make_car('subaru', 'outback', color = 'blue', tow_package = True)

print(car)

