import truck
import auction
from random import randint
import numpy as np
import math

class Company:

    def __init__(self, id, budget, local, risk):
        self.id = id
        self.trucks = []
        self.profit = budget
        self.local = local
        self.risk = risk

    def getId(self):
        return self.id

    def addTruck(self, truck):
        self.trucks.append(truck)

    def delTruck(self, truck):
        self.trucks.remove(truck)

    def getTrucks(self):
        return self.trucks

    def getProfit(self):
        return self.profit

    def updateProfit(self, budget):
        self.profit += budget

    def getLocal(self):
        return self.local

    def setLocal(self, local):
        self.local = local

    def evaluateOffer(self, offer):
        start = offer[0]
        finish = offer[1]
        goods = offer[2]
        base = offer[3]
        if(goods[0] > 0 and not(self.getAvailableBusForOffer())):
            return False
        if(goods[1] > 0 and not(self.getAvailableTrucksForOffer())):
            return False

        dist = auction.distance(start, finish)
        priceGood = np.random.uniform(0.4, 0.9)
        pricePeople =  np.random.uniform(0.9, 1.4)

        return ((pricePeople*goods[0] + priceGood*goods[1]) * (dist)) * (1+self.risk)




    def getUtility(self, distance):
        #put 0.2 after, if we organize the trucks with the products
        return distance * (1+self.risk) + 5

    def getNumberAvailableTrucks(self):
        s = 0
        trucks = self.getTrucks()
        for t in trucks:
            if(t.getAvailability()):
                s += 1
        return s

    def getAvailableBuses(self):
        busesAvailable = []

        buses = self.getTrucks()

        for b in buses:
            if(b.getAvailability() and (type(b) is truck.FiftyBus or type(b) is truck.SeventyBus)):
                busesAvailable += [b]
        return busesAvailable

    def getAvailableTrucks(self):
        trucksAvailable = []

        trucks = self.getTrucks()

        for t in trucks:
            if(t.getAvailability() and (type(t) is truck.FiftyTruck or type(t) is truck.SeventyTruck)):
                trucksAvailable += [t]
        return trucksAvailable


    def getAvailableBusForOffer(self):

        buses = self.getTrucks()

        for t in buses:
            if(type(t) is truck.FiftyBus or type(t) is truck.SeventyBus):
                return True
        return False

    def getAvailableTrucksForOffer(self):

        trucks = self.getTrucks()

        for t in trucks:
            if(type(t) is truck.FiftyTruck or type(t) is truck.SeventyTruck):
                return True
        return False

    def printAvailableTrucks(self):
        s = 0
        trucks = self.getTrucks()
        for t in trucks:
            if(t.getAvailability()):
                s += 1
        print("Company " + self.getId() + " has " + str(s) + " trucks available")



    def delivery(self, bid, destination, goods):
        self.updateProfit(bid)

        #melhorar isto
        try:
            if(goods[0] > 0):
                print(self.getAvailableBuses())
                b = np.random.choice(self.getAvailableBuses())
                b.startTransportation(destination)
            if(goods[1] > 0):
                t = np.random.choice(self.getAvailableTrucks())
                t.startTransportation(destination)
        except Exception as e:
            print("type error: " + str(e))

    def updateTrucksSteps(self):
        trucks = self.getTrucks()
        for t in trucks:
            t.stepTransportation()


    def buyTrucks(self, policy):

    #[1,2,3,4] 1: curto pessoas, 2: curto mercadorias, 3: longo pessoas, 4: longo mercadorias
        if policy == 1:
            x = truck.FiftyBus(randint(0, 100), self)
        elif policy == 2:
            x = truck.FiftyTruck(randint(0, 100), self)
        elif policy == 3:
            x = truck.SeventyBus(randint(0, 100), self)
        elif policy == 4:
            x = truck.SeventyTruck(randint(0, 100), self)

        self.profit -= x.getPrice()
        self.addTruck(x)

    def __repr__(self):
        return str("company com id: " + self.id)
