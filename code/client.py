import auction
import numpy as np
import company

class Client:
	def __init__(self, id, companies):
		self.id = id
		self.valuations = [10, 40]#, 20, 15, 25] #so interessa a valoração que faz para bens e pessoas????
		self.companyCount = {}
		for c in companies:
			self.companyCount[c.getId()] = 0

	def getId(self):
		return self.id

	def buyFromCompany(self, companyId):
		self.companyCount[companyId] += 1
		self.printHistory()

	def printHistory(self):
		for companyId, count in self.companyCount.items():
			print("Client " + self.getId() + " from " + companyId + " bought ", count, " times")

	def makeOffer(self, source, dest, amount, base):
		return [source, dest, amount, base]

	def chooseOffer(self, bids):
		#bids is a list of tuples that contain the bid and the respective company that made the bid
		return bids[0]

	def getUtility(self, good, start, finish):
		#why does the distance matter to the client??
		print("\n\n\n\n\n\n\n\n\n\n\n\n")
		distance = auction.distance(start, finish)
		moodPeople = np.random.uniform(1.2, 1.7)
		moodGoods = np.random.uniform(0.8, 1.3)

		return (moodPeople*good[0] + moodGoods*good[1]) * (distance)
