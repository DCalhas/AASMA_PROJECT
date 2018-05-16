import math
import time
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import world_set
import company


fig = plt.figure()

clients, companies = world_set.setupWorld(4, 4, 4, 4)

c_profits = []

for c in companies:
	c_profits += [[]]


def animate(i):

	global c_profits


	fig.clf()

	world_set.step(clients, companies)
	profits = []
	for c in companies:
		c_profits[companies.index(c)] += [c.getProfit()]


	for c in companies:
		plt.plot(c_profits[companies.index(c)])


ani = animation.FuncAnimation(fig, animate, interval=100)


plt.show()





