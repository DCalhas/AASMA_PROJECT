import auction
import numpy as np

class Client:
	#remove local from client, what if client wants it sent to another local?
	def __init__(self, id):
		self.id = id
		self.valuations = [10, 40]#, 20, 15, 25] #so interessa a valoração que faz para bens e pessoas????

	def getId(self):
		return self.id

	def makeOffer(self, source, dest, amount, base):
		return [source, dest, amount, base]

	def getUtility(self, good, start, finish):
		#why does the distance matter to the client??
		distance = auction.distance(start, finish)
		moodPeople = np.random.uniform(0.5, 1)
		moodGoods = np.random.uniform(0, 0.5)

		return (moodPeople*good[0] + moodGoods*good[1]) * (distance)
