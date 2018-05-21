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


c_miles = []
for c in companies:
	c_miles += [[]]


#returns false if new profits are the same and true if they are different
def compareWithPreviousIteration(previousProfits, newProfits):
	for i in range(len(previousProfits)):
		if(previousProfits[i] != newProfits[i]):
			return True
	return False

####################################################################################################
####################################################################################################
####################################################################################################
#										Companies Balance
####################################################################################################
####################################################################################################
####################################################################################################

def profit(i):

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
		plt.plot(c_profits[companies.index(c)], label=c.getId())

	plt.title("Balance of companies")
	plt.ylabel("Balance amount (euros)")
	plt.xlabel("time step")

	plt.legend(bbox_to_anchor=(0., 1.05, 1., .102), loc=3,
           ncol=len(companies), mode="expand", borderaxespad=0.)

	world_set.step(clients, companies, verbose=False)

####################################################################################################
####################################################################################################
####################################################################################################
#									MILES PER COMPANY
####################################################################################################
####################################################################################################
####################################################################################################


def milesPerCompany(i):

	global c_miles


	fig.clf()

	newMiles = []
	for c in companies:
		newMiles += [[c.getTrucksMiles()]]

	previousMiles = []

	for m in c_miles:
		if(len(m)):
			previousMiles += [m[-1]]


	if(compareWithPreviousIteration(previousMiles, newMiles) or not len(c_miles[0])):
		#add to c_profits new profits
		for c in companies:
			c_miles[companies.index(c)] += [newMiles[companies.index(c)]]
	
	for c in companies:
		plt.plot(c_miles[companies.index(c)], label=c.getId())

	plt.title("Miles ran by all the trucks of  the companies")
	plt.ylabel("Miles (km)")
	plt.xlabel("time step")

	plt.legend(bbox_to_anchor=(0., 1.05, 1., .102), loc=3,
           ncol=len(companies), mode="expand", borderaxespad=0.)
	#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

	world_set.step(clients, companies, verbose=False)



####################################################################################################
####################################################################################################
####################################################################################################
#									MILES PER COMPANY
####################################################################################################
####################################################################################################
####################################################################################################


def averageMilesPerCompany(i):

	global c_miles


	fig.clf()

	newMiles = []
	for c in companies:
		if(c.getNumberDeliveries() != 0):
			newMiles += [[c.getTrucksMiles()/c.getNumberDeliveries()]]
		else:
			newMiles += [[c.getTrucksMiles()]]

	previousMiles = []

	for m in c_miles:
		if(len(m)):
			previousMiles += [m[-1]]


	if(compareWithPreviousIteration(previousMiles, newMiles) or not len(c_miles[0])):
		#add to c_profits new profits
		for c in companies:
			c_miles[companies.index(c)] += [newMiles[companies.index(c)]]
	
	for c in companies:
		plt.plot(c_miles[companies.index(c)], label=c.getId())

	plt.title("Average miles per delivery by company")
	plt.ylabel("Miles (km)")
	plt.xlabel("time step")

	plt.legend(bbox_to_anchor=(0., 1.05, 1., .102), loc=3,
           ncol=len(companies), mode="expand", borderaxespad=0.)
	#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

	world_set.step(clients, companies, verbose=False)



ani = animation.FuncAnimation(fig, profit, interval=1)


plt.show()





