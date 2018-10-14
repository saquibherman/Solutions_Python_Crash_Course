import matplotlib.pyplot as plt
from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)
	
# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)
	
# Visualize the results
x_values = [x for x in range(1, die.num_sides+1)]
y_values = frequencies

fig, ax = plt.subplots()
bar_width = 0.35

rects = ax.bar(x_values, y_values, bar_width, color='b', label='Occurances')
                
ax.set_title("Results of rolling D6 dice 1000 times.", fontsize=20)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Frequency of Result", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

ax.legend()
fig.tight_layout()
plt.show()

