import truck

class Company:

    def __init__(self, id, list_trucks, budget, local):
        self.id = id
        self.trucks = list_trucks
        self.profit = budget
        self.local = local

    def getID(self):
        return self.id

    def addTruck(self, truck):
        self.trucks.append(truck)

    def delTruck(self, truck):
        self.trucks.remove(truck)

    def getProfit(self):
        return self.profit

    def setProfit(self, budget):
        self.profit = budget

    def getLocal(self):
        return self.local

    def setLocal(self, local):
        self.local = local

    def evaluateOffer(self, offer):
        start = offer[0]
        finish = offer[1]
        amount = offer[2]
        money = offer[3]

    def getUtility(money, distance):
        return money * distance

    def buyTrucks(self, policy):

    #[1,2,3,4] 1: curto pessoas, 2: curto mercadorias, 3: longo pessoas, 4: longo mercadorias
        if policy == 1:
            x = truck.FiftyBus()
        elif policy == 2:
            x = truck.FiftyTruck()
        elif policy == 3:
            x = truck.SeventyBus()
        elif policy == 4:
            x = truck.SeventyTruck()

        self.profit -= x.getPrice()
        addTruck(x)
