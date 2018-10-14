def get_city_country(city, country, population=''):
	"""Generate city, country name pair"""
	if population:
		city_country = city.title() + ', ' + country.title() + " - population " + str(population)
	else:
		city_country = city.title() + ', ' + country.title()
	return city_country
