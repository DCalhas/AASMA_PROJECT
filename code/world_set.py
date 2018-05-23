import company
import auction
import truck
import client
import numpy as np
import time
import inspect


volumeDeliveryTruck = [10, 15, 20, 25, 30]
volumeBus = [30, 40, 50, 60, 70]


#truck destination bid company - ordered by position
poolDeliveries = []

tax = 2

timestep = 0

districts = {"Lisboa": (0, 50), "Setubal": (0, 40), "Beja": (10, 20), "Evora": (10, 30), "Faro": (10, 0), "Portalegre": (20, 50), "Castelo Branco": (20, 60),
			"Santarem": (10, 60), "Coimbra": (0, 70), "Leiria": (0, 60), "Aveiro": (0, 80), "Guarda": (20, 70), "Porto": (0, 90), "Viana do Castelo": (0, 100),
			"Vila Real": (10, 100), "Viseu": (10, 70), "Braga": (10, 90), "Braganca": (20, 100)}

districts_connections = [("Lisboa", "Setubal"), ("Lisboa", "Santarem"), ("Lisboa", "Leiria"), ("Santarem", "Portalegre"), ("Portalegre", "Evora"),
						("Beja", "Evora"), ("Beja", "Faro"), ("Portalegre", "Castelo Branco"), ("Castelo Branco", "Guarda"), ("Guarda", "Viseu"),
						("Porto", "Braga"), ("Porto", "Coimbra"), ("Coimbra", "Leiria"), ("Coimbra", "Viseu"), ("Braga", "Viana do Castelo"),
						("Viana do Castelo", "Braganca"), ("Aveiro", "Leiria"), ("Aveiro", "Coimbra"), ("Vila Real", "Viana do Castelo"), ("Viana do Castelo", "Braganca"),
						("Braganca", "Guarda"), ("Santarem", "Viseu"), ("Braga", "Viseu"), ("Vila Real", "Braga"), ("Porto", "Viana do Castelo"),
						("Setubal", "Evora"), ("Santarem", "Evora")]
def checkCooperation():
	#iterate over all the offers in the pool
	for i in poolDeliveries:
		for j in poolDeliveries:
			if(i[3].getId() != j[3].getId()):

				if(isinstance(i[0], truck.Bus)):
					if(len(j[3].getAvailableBuses()) <  1):
						return False

				if(isinstance(i[0], truck.DeliveryTruck)):
					if(len(j[3].getAvailableTrucks()) <  1):
						return False

				if(isinstance(j[0], truck.Bus)):
					if(len(i[3].getAvailableBuses()) <  1):
						return False

				if(isinstance(j[0], truck.DeliveryTruck)):
					if(len(i[3].getAvailableTrucks()) <  1):
						return False

				r_one = i[2] - auction.distance(districts[i[3].getLocal()], i[1])
				r_two = j[2] - auction.distance(districts[j[3].getLocal()], j[1])

				r_one_changed = j[2] - auction.distance(districts[i[3].getLocal()], j[1])
				r_two_changed = i[2] - auction.distance(districts[j[3].getLocal()], i[1])

				if(r_one_changed > r_one and r_two_changed > r_two):

					i[3].changeDelivery(i, j)
					j[3].changeDelivery(j, i)

					print(j[3].getId() + " and " + i[3].getId() + " cooperated between each other by swaping offers")

					poolDeliveries.remove(i)
					poolDeliveries.remove(j)

					return



def step(clients, companies, verbose=True):
	global timestep, poolDeliveries
	timestep += 1


	client_offering = np.random.choice(clients)

	checkCooperation()


	for c in companies:
		c.updateProfit(-tax)
		state = c.getState()
		checkState(state, c, companies, timestep)
		c.investMidSimulation()
		c.updateTrucksSteps()
		if(verbose):
			c.printAvailableTrucks()


	results = auction.auction(companies, client_offering)

	if(results[2]):
		poolDeliveries = results[2]

	generateStates(companies)
	return results[0], results[1]

def checkState(state, c, companies, timestep):
	if(state == "broken"):
		companies.remove(c)
		c.declareBankrupcy(timestep)
	elif(state == "sellTruck"):
		auction.avoidFailure(c, companies)
	elif(state == "noTrucks"):
		companies.remove(c)
		c.declareBankrupcy(timestep)
	else:
		return True

def setupWorld(ncli, ncompanies, verbose=True):
	clients = []
	companies = []




	for i in range(ncompanies):
		c = company.Company("COMP" + str(i), 200, np.random.choice(list(districts.keys())), np.random.random())
		#c = company.Company("COMP" + str(i), 100, np.random.choice(list(districts.keys())), 0.5)
		if(verbose):
			print(c.getId() + ": ", 100, " district: " + c.getLocal(), " risk: ", c.getRisk())
			print
		c.buyTrucks()
		companies += [c]

	for i in range(ncli):

		clients += [client.Client("CL" + str(i), companies)]


	return clients, companies



def generateStates(companies):


	ranking = []

	while(len(ranking) != len(companies)):
		highest = 0
		for c in companies:	
			if(c.getProfit() > highest and not c in ranking):
				cHighest = c
				highest = c.getProfit()

		ranking += [cHighest]

	return ranking




if __name__ == "__main__":


	clients, companies = setupWorld(5, 4)

	while(1):
		print(step(clients, companies))
		for c in companies:
			print("Company " + c.getId() + " : " , c.getProfit(), "$$ tenho: ", len(c.getTrucks()), " trucks")
		time.sleep(0.01)
