import client
import math
import company
import world_set
import numpy as np

policyAuction = [1,2,3] #1- pessoas 2-bens 3-both

def distance(x, y):
	return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


def auction(companies, auctioneer):

	start = world_set.districts[np.random.choice(list(world_set.districts.keys()))]
	finish = world_set.districts[np.random.choice(list(world_set.districts.keys()))]
	while (finish == start):
		finish = world_set.districts[np.random.choice(list(world_set.districts.keys()))]
	policy = np.random.choice(policyAuction)

	if(policy == 1):
		goods = (int(np.random.uniform(1, 10)), 0) #(pessoa, bem)
	elif(policy == 2):
		goods = (0, int(np.random.uniform(1, 10)))
	else:
		goods = (int(np.random.uniform(1, 10)), int(np.random.uniform(1, 10)))

	#print(goods)
	baseAuction = auctioneer.getUtility(goods, start, finish)
	details = auctioneer.makeOffer(start, finish, goods, baseAuction)
	bids = []
	for c in companies:
		offer = c.evaluateOffer(details)

		if(offer):
			bids += [(offer, c)]

	if(len(bids) == 0):
		return None, None

	winnerBid = min(bids, key = lambda t: t[0])[0]
	company = min(bids, key = lambda t: t[0])[1]
	company.delivery(winnerBid, finish, goods)

	return company, winnerBid

def avoidFailure(seller, companies):
	truck = seller.getTrucks()[0]
	base = (truck.getPrice())/2
	bids = []
	for i in companies:
		offer = i.auctionProposel(truck, base)
		if(offer):
			bids += [(offer,i)]

	if(len(bids) == 0):
		return None, None

	winnerBid = max(bids, key = lambda t: t[0])[0]
	buyer = max(bids, key = lambda t: t[0])[1]

	seller.delTruck(truck)
	seller.updateProfit(winnerBid)

	buyer.addTruck(truck)
	buyer.updateProfit(-winnerBid)





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
