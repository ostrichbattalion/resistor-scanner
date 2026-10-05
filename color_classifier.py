#Create a visualization for the color bands.
#Maybe it’s time to separate the subplots.

import json
import matplotlib.pyplot as plt
import numpy as np


data = {}
x_coordinate = []
R, B, G = [], [], []




#color_ranges
#the ?brighter? values of colors
bright_codes = [(0, 0, 0), #black
(156, 102, 51), #brown
(255, 0, 0),       #red
(255, 102, 0),     #orange
(255, 255, 0),     #yellow
(0, 255, 0),       #green
(0, 0, 255),       #blue
(200, 0, 255),     #violet
(128, 128, 128),   #gray
(255, 255, 255)]   #white

#the ?darker? values of colors
dark_codes = [(20, 20, 20), #black
(71, 53, 38),      #brown
(204, 0, 0),       #red
(255, 51, 0),     #orange
(255, 204, 102), #yellow
(30, 200, 50), #green
(40, 73, 86),      #blue
(110, 0, 51),      #violet
(73, 65, 62),      #gray
(250, 250, 250)]   #white
color_name = ["black","brown","red","orange","yellow","green","blue","violet","gray","white"]

color_list_len = len(color_name)
iteration = 0


with open("line_of_color.json","r") as f:

    data.update(json.load(f))

for x, c in data.items():
    x_coordinate.append(int(x))
    B.append(int(c[0]))
    R.append(int(c[2]))
    G.append(int(c[1]))

fig, ax1 = plt.subplots(1,1,sharex=True, sharey=True)

ax1.plot(x_coordinate,R,color="Red")
ax1.plot(x_coordinate,G,color="Green")
ax1.plot(x_coordinate,B,color="Blue")
plt.tight_layout()
plt.show()