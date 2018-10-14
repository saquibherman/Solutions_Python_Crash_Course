import unittest
from city_functions import get_city_country

class NamesTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'."""

	def test_city_country(self):
		"""Do names like 'Santiago, Chile' work?"""
		city_country = get_city_country('santiago', 'chile')
		self.assertEqual(city_country, 'Santiago, Chile')
		
	def test_city_country_population(self):
		"""Do names like 'Santiago, Chile - population 5000000' work?"""
		city_country = get_city_country('santiago', 'chile', 5000000)
		self.assertEqual(city_country, 'Santiago, Chile - population 5000000')
		
unittest.main()
