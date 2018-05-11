class Company:

    def __init__(self, id, list_trucks):
        self.id = id
        self.trucks = list_trucks
        self.profit = 0

    def getID(self):
        return self.id

    def addTruck(self, truck):
        self.trucks.append(truck)

    def delTruck(self, truck):
        self.trucks.remove(truck)

    def getProfit(self):
        return self.profit

    def setProfit(self, profit):
        self.profit = profit

    def evaluateOffer(self, offer):
        start = offer[0]
        finish = offer[1]
        amount = offer[2]
        money = offer[3]

    def getUtility(money, distance):
        return money * distance
