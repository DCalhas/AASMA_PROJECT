import auction
import numpy as np
import company
import math

class Client:
	def __init__(self, id, companies):
		self.id = id
		self.valuations = [10, 40]#, 20, 15, 25] #so interessa a valoração que faz para bens e pessoas????
		self.companyCount = {}
		for c in companies:
			self.companyCount[c.getId()] = 0

		self.countPurchases = 0

	def getId(self):
		return self.id

	def buyFromCompany(self, companyId):
		self.companyCount[companyId] += 1
		#self.printHistory()

	def printHistory(self):
		for companyId, count in self.companyCount.items():
			print("Client " + self.getId() + " from " + companyId + " bought ", count, " times")

	def makeOffer(self, source, dest, amount, base):
		return [source, dest, amount, base]

	def chooseOffer(self, bids, verbose=True):
		#bids is a list of tuples that contain the bid and the respective company that made the bid
		minUtility = math.inf
		bidChosen = 0
		for b in bids:
			beenThere = self.companyCount[b[1].getId()]
			w = - 20
			utility = w * beenThere + b[0]
			if(utility < minUtility):
				minUtility = utility
				companyChosen = b[1]
				bidChosen = b[0]

		#if(verbose):
			#print("Company chosen was " + companyChosen.getId(), " with bid chosen ", bidChosen, " with ", self.countPurchases, " made, from client " + self.getId())

		self.countPurchases += 1

		return bidChosen, companyChosen




	def getUtility(self, good, start, finish):
		#why does the distance matter to the client??
		distance = auction.distance(start, finish)
		moodPeople = np.random.uniform(1.5, 2.5)
		moodGoods = np.random.uniform(1.5, 2.2)

		return (moodPeople*good[0] + moodGoods*good[1]) * (distance)
