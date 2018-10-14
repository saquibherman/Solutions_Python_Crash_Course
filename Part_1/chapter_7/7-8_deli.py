sandwich_orders = ['bacon', 'beef',  'pastrami', 'cheese', 'grilled cheese', 'chicken']
finished_sandwiches = []

while sandwich_orders:
	current_order = sandwich_orders.pop()
	print("Processing order: " + current_order + " sandwich")
	
	finished_sandwiches.append(current_order)
	
for sandwich in finished_sandwiches:
	print("I made your " + sandwich + " sandwich")

