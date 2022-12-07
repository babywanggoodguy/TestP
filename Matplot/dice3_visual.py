import pygal
from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()
results = [die_1.roll()+die_2.roll()+die_3.roll() for roll_num in range(1000)]
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result+1)]

hist = pygal.Bar()
hist.title = "Results fo rolling 3 D6 1000 times."
hist.x_labels = list(range(3, max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('3times D6', frequencies)
hist.render_to_file('dice3_visual.svg')
