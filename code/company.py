import truck
import auction
from random import randint
import numpy as np
import math
import auction

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
        if(goods[0] > 0 and len(self.getAvailableBuses()) == 0):
            return False
        if(goods[1] > 0 and len(self.getAvailableTrucks()) == 0):
            return False
        dist = auction.distance(start, finish)
        priceGood = np.random.uniform(0.4, 0.9)
        pricePeople =  np.random.uniform(0.9, 1.4)

        return ((pricePeople*goods[0] + priceGood*goods[1]) * (dist)) * (1+self.risk)

    def getUtility(self, distance):
        #put 0.2 after, if we organize the trucks with the products
        return distance * (1+self.risk) + 5

    def getAvailableBuses(self):
        busesAvailable = []

        buses = self.getTrucks()

        for b in buses:
            if(b.getAvailability() and (type(b) is truck.FiftyBus or type(b) is truck.SeventyBus)):
                busesAvailable += [b]

        return busesAvailable

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


    def getNumberAvailableTrucks(self):
        s = 0
        trucks = self.getTrucks()
        for t in trucks:
            if(t.getAvailability()):
                s += 1
        return s

    def getTrucksOnTheMove(self):
        trucks = self.getTrucks()

        move = []
        for t in trucks:
            if(not t.getAvailability()):
                move += [t]

        return move


    def printAvailableTrucks(self):
        s = 0
        trucks = self.getTrucks()
        for t in trucks:
            if(t.getAvailability()):
                s += 1
        print("Company " + self.getId() + " has " + str(s) + " trucks available")


    def delivery(self, bid, destination, goods):
        self.updateProfit(bid)


        buses = self.getAvailableBuses()
        if(goods[0] > 0 and len(buses)):
            b = np.random.choice(buses)
            b.startTransportation(destination)

        trucks = self.getAvailableTrucks()
        if(goods[1] > 0 and len(trucks)):
            t = np.random.choice(trucks)
            t.startTransportation(destination)


    def updateTrucksSteps(self):
        trucks = self.getTrucksOnTheMove()
        for t in trucks:
            t.stepTransportation()

    def buyTrucks(self):
        canBuy = True
        while(canBuy):
            policy = np.random.choice([1, 2, 3, 4])
            #[1,2,3,4] 1: curto pessoas, 2: curto mercadorias, 3: longo pessoas, 4: longo mercadorias
            if policy == 1 and self.getProfit() > truck.FiftyBus(randint(0, 100), self).getPrice():
                x = truck.FiftyBus(randint(0, 100), self)
                self.buyTruck(x)
                continue
            elif policy == 2 and self.getProfit() > truck.FiftyTruck(randint(0, 100), self).getPrice():
                x = truck.FiftyTruck(randint(0, 100), self)
                self.buyTruck(x)
                continue
            elif policy == 3 and self.getProfit() > truck.SeventyBus(randint(0, 100), self).getPrice():
                x = truck.SeventyBus(randint(0, 100), self)
                self.buyTruck(x)
                continue
            elif policy == 4 and self.getProfit() > truck.SeventyTruck(randint(0, 100), self).getPrice():
                x = truck.SeventyTruck(randint(0, 100), self)
                self.buyTruck(x)
                continue
            canBuy = False

    def buyTruck(self, t):
        self.profit -= t.getPrice()
        self.addTruck(t)