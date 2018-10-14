pizzas = ["onions", "pepperoni", "sausage"]
friend_pizzas = pizzas[:]

pizzas.append("neapolitan ")
friend_pizzas.append("detroit")

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizzas in friend_pizzas:
	print(pizzas)
