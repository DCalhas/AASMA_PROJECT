import client
import math
import company
import world_set
import numpy as np

def distance(x, y):
	return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


def auction(companies, auctioneer): #auctioneer nao esta a ser utilizado
	start = np.random.choice(list(world_set.districts.keys()))
	finish = np.random.choice(list(world_set.districts.keys())
	while(finish == start):
		finish = np.random.choice(list(world_set.districts.keys()))
	goods = (int(np.random.uniform(0, 10)), int(np.random.uniform(0, 1))) #(pessoa, bem)
	bids = []
	for c in companies:
		if (c.getNumberAvailableTrucks()>0):
			bids += [(c.getUtility(distance(world_set.districts[c.getLocal()], world_set.districts[destination])), c)]

	winnerBid = min(bids, key = lambda t: t[0])[0]
	company = min(bids, key = lambda t: t[0])[1]

	company.delivery(winnerBid, distance(world_set.districts[company.getLocal()], world_set.districts[destination]))

	return company, winnerBid


if __name__ == "__main__":
	clients = []
	clients += [client.Client("Joao")]
	clients += [client.Client("Pedro")]
	clients += [client.Client("Joana")]
	clients += [client.Client("Ana")]

	companies = []
	companies += [company.Company("C1", 0, np.random.choice(list(world_set.districts.keys())))]
	companies += [company.Company("C2", 0, np.random.choice(list(world_set.districts.keys())))]
	companies += [company.Company("C3", 0, np.random.choice(list(world_set.districts.keys())))]
	companies += [company.Company("C4", 0, np.random.choice(list(world_set.districts.keys())))]


	print(auction(companies, np.random.choice(clients)))
