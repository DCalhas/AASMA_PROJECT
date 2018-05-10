import company
import truck
import client
import numpy as np


volumeDeliveryTruck = [10, 15, 20, 25, 30]
volumeBus = [30, 40, 50, 60, 70]

districts = ["Lisboa", "Setubal", "Beja", "Evora", "Faro", "Portalegre", "Castelo Branco",
			"Santarem", "Coimbra", "Leiria", "Aveiro", "Guarda", "Porto", "Viana do Castelo",
			"Vila Real", "Viseu", "Braga", "Braganca"]



#def step():


def setupWorld(ncli, ntrucks, nbuses, ncompanies):
	clients = []
	trucks = []
	buses = []
	companies = []


	for i in range(ncli):
		clients += [client.Client("CL" + str(i))]

	for i in range(ntrucks):
		trucks += [truck.DeliveryTruck("M" + str(i), np.random.choice(districts), np.random.choice(volumeDeliveryTruck))]

	for i in range(nbuses):
		buses += [truck.Bus("B" + str(i), np.random.choice(districts), np.random.choice(volumeBus))]

	company1 = company.Company("COMP1", [trucks[0], trucks[1]])
	company2 = company.Company("COMP2", [trucks[3], buses[0]])
	company3 = company.Company("COMP3", [buses[1], trucks[2]])
	company4 = company.Company("COMP4", [buses[2], buses[3]])

	print(clients[0].makeOffer(np.random.choice(districts), np.random.choice(districts), 10, 20))

	return clients, trucks, buses, companies



setupWorld(4, 4, 4, 4)