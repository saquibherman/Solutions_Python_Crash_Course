import unittest
from city_functions import get_city_country

class NamesTestCase(unittest.TestCase):
	"""Test fro 'city_functions.py'."""

	def test_city_country(self):
		"""Do names like 'Santiago, Chile' work?"""
		city_country = get_city_country('santiago', 'chile')
		self.assertEqual(city_country, 'Santiago, Chile')
		
unittest.main()
