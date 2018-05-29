import truck
import auction
from random import randint
import numpy as np
import math
import auction
import policies
import random
import world_set

class Company:

    def __init__(self, id, budget, local, risk, learning):
        self.id = id
        self.trucks = []
        self.profit = budget
        self.local = local
        self.risk = risk
        self.numberDeliveries = 0
        self.learning = learning

    def getLearning(self):
        return self.learning


    def updateRiskAccordingToQ(self, companies):
        rankings = world_set.generateStates(companies)

        if(not self in rankings):
            return
        state = rankings.index(self)




        action = self.actions[np.argmin(self.Q[state])]
        if(action == 0):
            self.setRisk(0.1)
            print("Learning company updated the risk to: ", self.getRisk())
        elif(action == 1):
            self.setRisk(0.25)
            print("Learning company updated the risk to: ", self.getRisk())
        elif(action == 2):
            self.setRisk(0.5)
            print("Learning company updated the risk to: ", self.getRisk())
        elif(action == 3):
            self.setRisk(0.75)
            print("Learning company updated the risk to: ", self.getRisk())
        elif(action == 4):
            self.setRisk(0.9)
            print("Learning company updated the risk to: ", self.getRisk())


    def getId(self):
        return self.id

    def getTrucksMiles(self):
        trucks = self.getTrucks()
        miles = 0

        for t in trucks:
            miles += t.getMiles()

        return miles

    def getNumberDeliveries(self):
        return self.numberDeliveries

    def addTruck(self, truck):
        self.trucks.append(truck)


    def delTruck(self, truck):
        self.trucks.remove(truck)

    def setTrucks(self, l):
        self.trucks = l

    def getTrucks(self):
        return self.trucks

    def declareBankrupcy(self, t):
        print(self.getId() + " entered bankrupcy at timestep ", t, " it was located at " + self.getLocal() + " with  risk of ", self.getRisk())

    def getRisk(self):
        return self.risk

    def setRisk(self, risk):
        self.risk = risk

    def setProfit(self, p):
        self.profit = p

    def getProfit(self):
        return self.profit

    def updateProfit(self, budget):
        self.profit += budget

    def getState(self):
        if(self.profit <= world_set.tax and len(self.getTrucksNotOnTheMove()) == 0):
            return "broken"
        elif(self.profit <= world_set.tax and len(self.getTrucksNotOnTheMove())):
            return "sellTruck"
        elif(len(self.getTrucks()) == 0):
            return "noTrucks"
        else:
            return "stable"

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

        dist = auction.distance(start, finish) + auction.distance(start, world_set.districts[self.getLocal()])
        priceGood = np.random.uniform(0.3, 0.6)
        pricePeople =  np.random.uniform(0.6, 1.2)

        bid = ((pricePeople*goods[0] + priceGood*goods[1]) * (dist)) * (1+self.risk)
        if(bid>base):
            return bid


    def valueAssets(self):
        value = self.getProfit()

        for i in self.getTrucks():
            if(isinstance(i, truck.FiftyBus)):
                value += 50
            if(isinstance(i, truck.SeventyBus)):
                value += 70
            if(isinstance(i, truck.FiftyTruck)):
                value += 25
            if(isinstance(i, truck.SeventyTruck)):
                value += 50

        return value

    def getActivePlusBalance(self):
        return self.valueAssets() + self.getProfit()


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

    def getTrucksNotOnTheMove(self):
        trucks = self.getTrucks()

        home = []
        for t in trucks:
            if(t.getAvailability()):
                home += [t]

        return home

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
            self.numberDeliveries += 1
            b.setAvailability(False)
            #b.startTransportation(destination)
            world_set.poolDeliveries += [(b, destination, bid, self)]


        trucks = self.getAvailableTrucks()
        if(goods[1] > 0 and len(trucks)):
            t = np.random.choice(trucks)
            self.numberDeliveries += 1
            t.setAvailability(False)
            #t.startTransportation(destination)
            world_set.poolDeliveries += [(t, destination,bid, self)]

        return world_set.poolDeliveries


    def updateTrucksSteps(self):
        if(len(world_set.poolDeliveries)>=10):
            for offer in world_set.poolDeliveries:
                if offer[0] in self.getTrucks():
                    offer[0].startTransportation(offer[1])
                    self.updateProfit(- auction.distance(world_set.districts[self.getLocal()], offer[1]))
                    world_set.poolDeliveries.remove(offer)
                    break

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

    def investMidSimulation(self):
        #define a threshold along with a policy
        percentageTransports = policies.policyBuyMidSimulation(self, policy="percentage")
        policy = np.random.choice([1, 2, 3, 4], p=percentageTransports)

        if policy == 1 and self.getProfit() > truck.FiftyBus(randint(0, 100), self).getPrice() + 20:
            x = truck.FiftyBus(randint(0, 100), self)
            self.buyTruck(x)
        elif policy == 2 and self.getProfit() > truck.FiftyTruck(randint(0, 100), self).getPrice() + 20:
            x = truck.FiftyTruck(randint(0, 100), self)
            self.buyTruck(x)
        elif policy == 3 and self.getProfit() > truck.SeventyBus(randint(0, 100), self).getPrice() + 20:
            x = truck.SeventyBus(randint(0, 100), self)
            self.buyTruck(x)
        elif policy == 4 and self.getProfit() > truck.SeventyTruck(randint(0, 100), self).getPrice() + 20:
            x = truck.SeventyTruck(randint(0, 100), self)
            self.buyTruck(x)

    def auctionProposal(self, truck, base):
        originalPrice = truck.getPrice()

        offer = round(random.uniform(originalPrice*0.4, originalPrice*0.7), 2)

        if(offer>base):
            return offer
        else:
            return False

    def changeDelivery(self, old, new):

        #old and new are tuples that are in the pool

        #discard the truck
        old[0].setAvailability(True)

        #remove the profit gained
        self.updateProfit(- old[2])

        for t in self.getTrucksNotOnTheMove():
            if(isinstance(new[0], truck.Bus) and isinstance(t, truck.Bus)):
                t.startTransportation(new[1])
                self.updateProfit(new[2])
                return True
            if(isinstance(new[0], truck.DeliveryTruck) and isinstance(t, truck.DeliveryTruck)):
                t.startTransportation(new[1])
                self.updateProfit(new[2])
                return True
                
    def egreedyPolicy(self, state, e=0.1):
        if(isinstance(np.argmin(self.Q[state]), np.int64)):
            return np.random.choice([np.random.choice(self.actions), self.actions[np.argmin(self.Q[state])]], p=[e, 1-e])
        return np.random.choice([np.random.choice(self.actions), self.actions[np.argmin(self.Q[state])]], p=[e, 1-e])

    def sarsaRL(self):
        import gc
        cost = []

        #initialize world
        clients, companies = world_set.setupWorld(world_set.numberClients, world_set.numberCompanies - 1, learnQ=False)

        companies += [self]


        #generate the rankings to know the state of the company
        rankings = world_set.generateStates(companies)
        
        #0-increase, 1-decrease, 2-maintain
        self.actions = [0, 1, 2, 3, 4]


        for i in range(len(rankings)):
            cost += [[]]
            for j in self.actions:
                cost[i] += [j/len(self.actions)]
            print(cost[i])

        states = []
        for i in range(len(rankings)):
            states += [i]

        state = rankings.index(self)

    

        self.Q = np.zeros((len(states), len(self.actions)))

        alpha = 0.3

        gamma = 0.95

        action = self.egreedyPolicy(state, e=0.5)

        for i in range(1, 1000):
            if(i%(100-1) == 0):
                print("RESETING WORLD")
                for c in companies:
                    c.setTrucks([])
                    c.setProfit(200)
                    c.buyTrucks()

            gc.collect()
            #perform the action of increasing or decreasing the risk
            if(action == 0):
                self.setRisk(0.1)
            elif(action == 1):
                self.setRisk(0.25)
            elif(action == 2):
                self.setRisk(0.5)
            elif(action == 3):
                self.setRisk(0.75)
            elif(action == 4):
                self.setRisk(0.9)

            for c in companies:
                if(c.getState() == "broken" or c.getState() == "noTrucks"):
                    print("RESETING COMPANY ", c.getId())
                    c.setTrucks([])
                    c.setProfit(200)
                    c.buyTrucks()

            world_set.step(clients, companies, verbose=False)

            rankings = world_set.generateStates(companies)
            
            if(not self in rankings):
                self.setProfit(200)
                self.buyTrucks()
                for c in companies:
                    c.setTrucks([])
                    c.setProfit(200)
                    c.buyTrucks()

                rankings = world_set.generateStates(companies)


            nextState = rankings.index(self)

            nextAction = self.egreedyPolicy(nextState, e=1)
            
            ct = cost[state][action]

            self.Q[state][action] = self.Q[state][action] + alpha * (ct + gamma * self.Q[nextState][nextAction] - self.Q[state][action])
            
            state = nextState
            action = nextAction

            #print("New norm of the Q function: ", np.linalg.norm(self.Q))
        
        for r in self.Q:
            print(r)
        gc.collect()

        self.setProfit(200)
        self.trucks = []
        self.numberDeliveries = 0
        self.risk = 0.5
        self.buyTrucks()
