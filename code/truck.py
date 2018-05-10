class Truck:

    def __init__(self, id, local):
        self.id = id
        self.gas = 0
        self.available = True
        self.local = local

    def getID(self):
        return self.id

    def fillGas(self, amount):
        self.gas += amount

    def getLocal(self):
        return self.local

    def setLocal(self, local):
        self.local = local


class Bus(Truck):


    def __init__(self, id, local, capacity):
        Truck.__init__(id, local)

        self.capacity = capacity


    def getCapacity(self):
        return self.capacity




class DeliveryTruck(Truck):
    def __init__(self, id, local, volume_capacity):
        Truck.__init__(id, local)

        self.volume_capacity = volume_capacity


    def getCapacity(self):
        return self.volume_capacity

