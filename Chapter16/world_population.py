import json
import pygal.maps.world
import pygal.style
import csv
import pygal_maps_world.maps
from pygal.style import RotateStyle, LightColorizedStyle
from country_codes import get_country_code


filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
cc_population = {}
no_code_country = []
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population
        else:
            no_code_country.append(country_name)

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Populations in 2010, by Country'

wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('world_population.svg')

f = open("no_code_country.txt", "w")
f.write("Countries Without Code\n")
f.write(str(no_code_country))
f.close()
