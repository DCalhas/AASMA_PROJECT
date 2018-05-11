import company
import truck
import client
import numpy as np


volumeDeliveryTruck = [10, 15, 20, 25, 30]
volumeBus = [30, 40, 50, 60, 70]

districts = {"Lisboa": (0, 50), "Setubal": (0, 40), "Beja": (10, 30), "Evora": (10, 20), "Faro": (10, 10), "Portalegre": (20, 50), "Castelo Branco": (20, 60),
			"Santarem": (10, 60), "Coimbra": (0, 70), "Leiria": (0, 60), "Aveiro": (0, 80), "Guarda": (20, 70), "Porto": (0, 90), "Viana do Castelo": (0, 100),
			"Vila Real": (10, 100), "Viseu": (10, 70), "Braga": (10, 90), "Braganca": (20, 100)}


#def step():

def setupWorld(ncli, ntrucks, nbuses, ncompanies):
	clients = []
	trucks = []
	buses = []
	companies = []


	for i in range(ncli):
		clients += [client.Client("CL" + str(i))]

	for i in range(ntrucks):
		trucks += [truck.FiftyTruck("M" + str(i), np.random.choice(list(districts.keys())), np.random.choice(volumeDeliveryTruck))]

	for i in range(nbuses):
		buses += [truck.FiftyBus("B" + str(i), np.random.choice(list(districts.keys())), np.random.choice(volumeBus))]

	company1 = company.Company("COMP1", [trucks[0], trucks[1]])
	company2 = company.Company("COMP2", [trucks[3], buses[0]])
	company3 = company.Company("COMP3", [buses[1], trucks[2]])
	company4 = company.Company("COMP4", [buses[2], buses[3]])

	print(clients[0].makeOffer(np.random.choice(list(districts.keys())), np.random.choice(list(districts.keys())), 10, 20))

	return clients, trucks, buses, companies



setupWorld(4, 4, 4, 4)