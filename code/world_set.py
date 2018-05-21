import company
import auction
import truck
import client
import numpy as np
import time


volumeDeliveryTruck = [10, 15, 20, 25, 30]
volumeBus = [30, 40, 50, 60, 70]

tax = 2

districts = {"Lisboa": (0, 50), "Setubal": (0, 40), "Beja": (10, 20), "Evora": (10, 30), "Faro": (10, 0), "Portalegre": (20, 50), "Castelo Branco": (20, 60),
			"Santarem": (10, 60), "Coimbra": (0, 70), "Leiria": (0, 60), "Aveiro": (0, 80), "Guarda": (20, 70), "Porto": (0, 90), "Viana do Castelo": (0, 100),
			"Vila Real": (10, 100), "Viseu": (10, 70), "Braga": (10, 90), "Braganca": (20, 100)}

districts_connections = [("Lisboa", "Setubal"), ("Lisboa", "Santarem"), ("Lisboa", "Leiria"), ("Santarem", "Portalegre"), ("Portalegre", "Evora"),
						("Beja", "Evora"), ("Beja", "Faro"), ("Portalegre", "Castelo Branco"), ("Castelo Branco", "Guarda"), ("Guarda", "Viseu"),
						("Porto", "Braga"), ("Porto", "Coimbra"), ("Coimbra", "Leiria"), ("Coimbra", "Viseu"), ("Braga", "Viana do Castelo"),
						("Viana do Castelo", "Braganca"), ("Aveiro", "Leiria"), ("Aveiro", "Coimbra"), ("Vila Real", "Viana do Castelo"), ("Viana do Castelo", "Braganca"),
						("Braganca", "Guarda"), ("Santarem", "Viseu"), ("Braga", "Viseu"), ("Vila Real", "Braga"), ("Porto", "Viana do Castelo"),
						("Setubal", "Evora"), ("Santarem", "Evora")]

def step(clients, companies, verbose=True):

	client_offering = np.random.choice(clients)

	for c in companies:
		c.updateProfit(-tax)
		state = c.getState()
		checkState(state, c, companies)
		c.investMidSimulation()
		c.updateTrucksSteps()
		if(verbose):
			c.printAvailableTrucks()


	return auction.auction(companies, client_offering)

def checkState(state, c, companies):
	if(state == "broken"):
		companies.remove(c)
	elif(state == "sellTruck"):
		auction.avoidFailure(c, companies)
	elif(state == "noTrucks"):
		companies.remove(c)
	else:
		return True

def setupWorld(ncli, ntrucks, nbuses, ncompanies, verbose=True):
	clients = []
	companies = []


	for i in range(ncli):

		clients += [client.Client("CL" + str(i))]


	for i in range(ncompanies):
		c = company.Company("COMP" + str(i), 100, np.random.choice(list(districts.keys())), np.random.random())
		c.buyTrucks()
		companies += [c]
		if(verbose):
			print(c.getTrucks())

	return clients, companies



if __name__ == "__main__":


	clients, companies = setupWorld(4, 4, 4, 4)

	while(1):
		print(step(clients, companies))
		for c in companies:
			print("Company " + c.getId() + " : " , c.getProfit(), "$$ tenho: ", len(c.getTrucks()), " trucks")
		time.sleep(0.5)
