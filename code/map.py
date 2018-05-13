import random
import pylab
import math
import time
from matplotlib.pyplot import pause
from matplotlib import patches
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib.animation as animation
from world_set import districts, districts_connections


for k in districts:
    districts[k] = ((districts[k][0]+10)/40, (districts[k][1]+10)/120)
    print(k, districts[k])


fig = plt.figure()

fig.patches.extend([plt.Rectangle((0,0.5),0.1,0.1,
                                  fill=True, color='grey', alpha=0.5, zorder=1000,
                                  transform=fig.transFigure, figure=fig)])


fig.patches.extend([plt.Rectangle((0.5,0),0.1,0.1,
                                  fill=True, color='grey', alpha=0.5, zorder=1000,
                                  transform=fig.transFigure, figure=fig)])



#####################################################################
actual = districts["Setubal"]
finish = districts["Evora"]
t = 0

def updatePosition(p, dest):
    global actual, finish, districts, t
    if(actual[0] == finish[0] and actual[1] == finish[1]):
        actual = districts["Setubal"]
        finish = districts["Evora"]
        t = 0
        return actual
    p = (p[0] + t*(dest[0] - p[0]), p[1] + t*(dest[1] - p[1]))
    return p
######################################################################





def animate(i):
    fig.clf()
    p = []
    for k in districts:
        p += [patches.Circle((districts[k][0],districts[k][1]), radius=0.01, transform=fig.transFigure, figure=fig)]

    for d in districts_connections:
        p += [patches.ConnectionPatch(xyA=districts[d[0]], 
                                    xyB=districts[d[1]], 
                                    coordsA='figure fraction', coordsB='figure fraction', arrowstyle="-", transform=fig.transFigure, figure=fig)]

    #moving between Setubal and Evora
    global actual, finish, t
    p += [patches.RegularPolygon(actual, 4, radius=0.01, color='r', transform=fig.transFigure, figure=fig)]
    actual = updatePosition(actual, finish)
    t += 0.05
    fig.patches.extend(p)
    """fig.patches.extend([plt.Rectangle((np.random.random(),np.random.random()),0.01,0.01,
                                  fill=True, color='grey', alpha=0.5, zorder=1000,
                                  transform=fig.transFigure, figure=fig), 
                        patches.RegularPolygon((0.5,0.5), 4, radius=0.01, color='r', transform=fig.transFigure, figure=fig),
                        patches.Circle((0.1,0.5), radius=0.01, transform=fig.transFigure, figure=fig),
                        patches.Circle((0.9,0.5), radius=0.01, transform=fig.transFigure, figure=fig),
                        patches.ConnectionPatch(xyA=(0.1, 0.5), xyB=(0.9, 0.5), coordsA='figure fraction', coordsB='figure fraction', arrowstyle="-", transform=fig.transFigure, figure=fig)])
"""
    return fig


ani = animation.FuncAnimation(fig, animate, interval=40)


plt.show()
"""
pylab.ion()

graph = nx.Graph()

graph.add_node(0, Position=(random.randrange(0, 100), random.randrange(0, 100)))
graph.add_node(1, Position=(random.randrange(0, 100), random.randrange(0, 100)))
graph.add_node(2, Position=(random.randrange(0, 100), random.randrange(0, 100)))
graph.add_node(3, Position=(50, 50))

graph.add_node(4, Position=(50, 50))


graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)

def get_fig():
    global node_number
    graph.remove_node(4)
    graph.node[4]['Position'] = (random.randrange(0, 100), random.randrange(0, 100))
    nx.draw(graph, pos=nx.get_node_attributes(graph,'Position'))

num_plots = 50;
pylab.show()

for i in range(num_plots):

    get_fig()
    pylab.draw()
    pause(0.3)
"""