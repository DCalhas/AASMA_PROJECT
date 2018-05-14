class Client:
	#remove local from client, what if client wants it sent to another local?
    def __init__(self, id):
        self.id = id
        self.valuations = [10, 40]#, 20, 15, 25] #so interessa a valoração que faz para bens e pessoas????

    def getId(self):
        return self.id

    def makeOffer(self, source, dest, amount, money):
        return [source, dest, amount, money]

    def getUtility(good, distance):
    	moodPeople = np.random.uniform(0, 1)
        #moodGoods

    	return mood * (self.valuations[good] * distance**2)
