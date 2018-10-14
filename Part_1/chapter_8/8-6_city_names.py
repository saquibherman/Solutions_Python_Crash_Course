def city_country(city, country):
	""""Returns formatted city, country"""
	formatted = '"' + city.title() + ', ' + country.title() + '"'
	return formatted
	
city1 = city_country('malmo', 'sweden')
city2 = city_country('nice', 'france')
city3 = city_country('san jose', 'united states')

print(city1)
print(city2)
print(city3)
