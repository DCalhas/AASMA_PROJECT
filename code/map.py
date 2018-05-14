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

#normalize the coordinates to be within the range of [0, 1]
for k in districts:
    districts[k] = ((districts[k][0]+10)/40, (districts[k][1]+10)/120)
    print(k, districts[k])


fig = plt.figure()



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




#this function is the animation, is called with an interval of 40 ms 
def animate(i):
    #clear figure at each iteration
    fig.clf()
    p = []
    for k in districts:
        #https://matplotlib.org/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle package explanation
        #these are supposed to be the location (each district)
        p += [patches.Circle((districts[k][0],districts[k][1]), radius=0.01, transform=fig.transFigure, figure=fig)]

    for d in districts_connections:
        #https://matplotlib.org/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch package explanation
        p += [patches.ConnectionPatch(xyA=districts[d[0]], 
                                    xyB=districts[d[1]], 
                                    coordsA='figure fraction', coordsB='figure fraction', arrowstyle="-", transform=fig.transFigure, figure=fig)]

    #moving between Setubal and Evora ####### this is just a demo (a point moving) TODO: implement the movement of the trucks #######
    global actual, finish, t
    #https://matplotlib.org/api/_as_gen/matplotlib.patches.RegularPolygon.html#matplotlib.patches.RegularPolygon package explanation
    p += [patches.RegularPolygon(actual, 4, radius=0.01, color='r', transform=fig.transFigure, figure=fig)]
    actual = updatePosition(actual, finish)
    t += 0.05


    #Add the objects updated to the figure
    fig.patches.extend(p)

    return fig


ani = animation.FuncAnimation(fig, animate, interval=40)


plt.show()