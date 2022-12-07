import pygal
import matplotlib.pyplot as plt
from die import Die

die_1 = Die()
die_2 = Die()
results = [die_1.roll()+die_2.roll() for roll_num in range(100)]
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# hist = pygal.Bar()
# hist.title = "Results fo rolling a D6 and a D10 50000 times."
# hist.x_labels = list(range(2, max_result+1))
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"
# hist.add('D6+D10', frequencies)
# # hist.render_to_file('dice_visual.svg')

x_values = list(range(1, len(results)+1))
y_values = results
plt.plot(x_values, y_values, linewidth=1)
plt.scatter(x_values, y_values, c='none', edgecolors='black', s=15)

plt.show()