class Truck:

    def __init__(self, id, capacity, local):
        self.id = id
        self.capacity = capacity
        self.gas = 0
        self.available = True
        self.local = local

    def getID(self):
        return self.id

    def getCapacity(self):
        return self.capacity

    def setCapacity(self, capacity):
        self.capacity = capacity

    def fillGas(self, amount):
        self.gas += amount

    def getLocal(self):
        return self.local

    def setLocal(self, local):
        self.local = local
