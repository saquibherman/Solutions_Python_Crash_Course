import pygal

from random_walk import RandomWalk

while True:
	# Make a random walk, and plot the points
	rw = RandomWalk()
	rw.fill_walk()
	
	point_numbers = list(range(rw.num_points))

	# Visualize the results.
	random_walk = pygal.XY(stroke=False)

	random_walk.title = "Results of random walk of 100 steps."
	random_walk.x_title = "x direction"
	random_walk.y_title = "y direction"

	for x in range(rw.num_points):
		random_walk.add('steps', [{'value': (rw.x_values[x], rw.y_values[x])}])
	random_walk.render_to_file('walk_visual.svg')
	
	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
"""
xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'A Made Up Correlation Between Search Engines'
xy_chart.add('Group A', [{'value': (0, 0), 'label': 'google', 'xlink':'http://www.google.com'}, {'value': (22, 2), 'tooltip': 'bing', 'xlink':'http://www.bing.com'}])
xy_chart.add('Group B', [{'value': (12, 20), 'label': 'yahoo', 'xlink':'http://www.yahoo.com'}, {'value': (33, 12), 'tooltip': 'duckduckgo', 'xlink':'http://www.duckduckgo.com'}])
xy_chart.render_to_file('dice_visual.svg')
"""
