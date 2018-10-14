from random import randint

class Die():
	"""A simple example of dice random number generation"""
	def __init__(self, sides = 6):
		self.sides = sides
		
	def roll_die(self):
		x = randint(1, self.sides)
		print(x)
		
die = Die()
die.roll_die()
print('\n')

die = Die(6)
die.roll_die()
print('\n')

die = Die(10)
for x in range(10):
	die.roll_die()
print('\n')

die = Die(20)
for x in range(10):
	die.roll_die()
