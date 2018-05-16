import auction
import numpy as np

class Client:
	#remove local from client, what if client wants it sent to another local?
<<<<<<< HEAD
    def __init__(self, id):
        self.id = id
        self.valuations = [10, 40]#, 20, 15, 25] #so interessa a valoração que faz para bens e pessoas????
=======
	def __init__(self, id):
		self.id = id
		self.valuations = [10, 40]#, 20, 15, 25] #so interessa a valoração que faz para bens e pessoas????

	def getId(self):
		return self.id

	def makeOffer(self, source, dest, amount, base):
		return [source, dest, amount, base]
>>>>>>> 4f41a9a4d842709501ddc7e843bf1b457ceb2826

	def getUtility(self, good, start, finish):

<<<<<<< HEAD
    def makeOffer(self, source, dest, amount, base):
        return [source, dest, amount, base]

    def getUtility(self, good, start, finish):

        distance = auction.distance(start, finish)
        moodPeople = np.random.uniform(0.5, 1)
        moodGoods = np.random.uniform(0, 0.5)

        return (moodPeople*good[0] + moodGoods*good[1]) * (distance)
=======
		#why does the distance matter to the client??
		distance = auction.distance(start, finish)
		moodPeople = np.random.uniform(0.5, 1)
		moodGoods = np.random.uniform(0, 0.5)

		return (moodPeople*good[0] + moodGoods*good[1]) * (distance)
>>>>>>> 4f41a9a4d842709501ddc7e843bf1b457ceb2826
