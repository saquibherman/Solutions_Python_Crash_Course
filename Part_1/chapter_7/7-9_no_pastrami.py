sandwich_orders = ['bacon', 'pastrami', 'beef',  'pastrami', 'cheese', 'grilled cheese', 'pastrami','chicken']
finished_sandwiches = []

print("The deli has run out of pastrami!!")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
	
while sandwich_orders:
	current_order = sandwich_orders.pop()
	print("Processing order: " + current_order + " sandwich")
	
	finished_sandwiches.append(current_order)
	
for sandwich in finished_sandwiches:
	print("I made your " + sandwich + " sandwich")

