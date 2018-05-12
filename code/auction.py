import client
import math
import company
import world_set
import numpy as np

def distance(x, y):
	return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


def auction(companies, auctioneer):
	destination = np.random.choice(list(world_set.districts.keys()))
	bids = []
	for c in companies:
		bids += [c.getUtility(distance(world_set.districts[c.getLocal()], world_set.districts[destination]))]
		#print(auctioneer.getUtility())
	winner = np.min(bids)
	
	return companies[bids.index(winner)], np.min(bids)


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