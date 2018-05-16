import math
import time
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import world_set
import company


fig = plt.figure()

clients, companies = world_set.setupWorld(4, 4, 4, 4, verbose=False)

c_profits = []

for c in companies:
	c_profits += [[]]

#returns false if new profits are the same and true if they are different
def compareWithPreviousIteration(previousProfits, newProfits):
	for i in range(len(previousProfits)):
		if(previousProfits[i] != newProfits[i]):
			return True
	return False


def animate(i):

	global c_profits


	fig.clf()

	newProfits = []
	for c in companies:
		newProfits += [[c.getProfit()]]

	previousProfits = []

	#previousProfits
	for p in c_profits:
		if(len(p)):
			previousProfits += [p[-1]]


	if(compareWithPreviousIteration(previousProfits, newProfits) or not len(c_profits[0])):
		#add to c_profits new profits
		for c in companies:
			c_profits[companies.index(c)] += [newProfits[companies.index(c)]]
	
	for c in companies:
		plt.plot(c_profits[companies.index(c)])

	world_set.step(clients, companies, verbose=False)


ani = animation.FuncAnimation(fig, animate, interval=1)


plt.show()





