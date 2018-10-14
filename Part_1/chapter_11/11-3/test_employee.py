import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Tests for the class Employee"""
	
	def setUp(self):
		"""
		Create a set of employee record for use in all test methods.
		"""
		self.employee_survey = Employee('Saquib', 'Herman', 700000)
		
	def test_give_default_raise(self):
		"""Test the default raise in annual salary"""
		self.assertEqual(700000 + 5000, self.employee_survey.give_raise())
		
	def test_give_custom_raise(self):
		"""Test the custom raise in annual salary"""
		self.assertEqual(700000+ 7000, self.employee_survey.give_raise(7000))
		
unittest.main()
