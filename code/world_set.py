import company
import auction
import truck
import client
import numpy as np
import time


volumeDeliveryTruck = [10, 15, 20, 25, 30]
volumeBus = [30, 40, 50, 60, 70]
policy = [1, 2, 3, 4]

districts = {"Lisboa": (0, 50), "Setubal": (0, 40), "Beja": (10, 30), "Evora": (10, 20), "Faro": (10, 0), "Portalegre": (20, 50), "Castelo Branco": (20, 60),
			"Santarem": (10, 60), "Coimbra": (0, 70), "Leiria": (0, 60), "Aveiro": (0, 80), "Guarda": (20, 70), "Porto": (0, 90), "Viana do Castelo": (0, 100),
			"Vila Real": (10, 100), "Viseu": (10, 70), "Braga": (10, 90), "Braganca": (20, 100)}


def step(clients, companies):

	client_offering = np.random.choice(clients)


	for c in companies:
		c.updateTrucksSteps()
		c.printAvailableTrucks()


	return auction.auction(companies, client_offering)

def setupWorld(ncli, ntrucks, nbuses, ncompanies):
	clients = []
	companies = []


	for i in range(ncli):

		clients += [client.Client("CL" + str(i))]


	for i in range(ncompanies):
		c = company.Company("COMP" + str(i), 50+i, np.random.choice(list(districts.keys())), np.random.random())
		while c.getProfit() > 0:
			c.buyTrucks(np.random.choice(policy))
		companies += [c]

		print(c.getTrucks())


	#print(clients[0].makeOffer(np.random.choice(list(districts.keys())), np.random.choice(list(districts.keys())), 10, 20))
	return clients, companies



if __name__ == "__main__":


	clients, companies = setupWorld(4, 4, 4, 4)

	while(1):
		print(step(clients, companies))
		for i in companies:
			print("i tem : " , i.getProfit())
		time.sleep(1)
