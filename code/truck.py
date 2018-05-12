import company
from random import randint

class Truck:

    def __init__(self, id, owner):
        self.id = owner.getId() + str(id)
        self.gas = 0
        self.available = True
        self.local = owner.getLocal()
        self.time_to_available = 0

    #returns if transport is available or not
    def getAvailability(self):
        return self.time_to_available == 0

    #starts a transportation
    def startTransportation(self, distance):
        if(self.getAvailability()):
            self.time_to_available = 2 * round(10 * (distance/110))

    #decreases the time of a transportation
    def stepTransportation(self):
        if(not self.getAvailability()):
            self.time_to_available -= 1

    def getID(self):
        return self.id

    def fillGas(self, amount):
        self.gas += amount

    def getLocal(self):
        return self.local

    def setLocal(self, local):
        self.local = local





class Bus(Truck):
    def __init__(self, id, owner):
        Truck.__init__(self, id, owner)

class FiftyBus(Bus):
    def __init__(self, id, owner):
        Truck.__init__(self, id, owner)

        self.capacity = 5


    def getCapacity(self):
        return self.capacity

    def getPrice(self):
        return 50

    def __repr__(self):
        return str(self.id + ' capacidade: ' + str(self.capacity))


class SeventyBus(Bus):
    def __init__(self, id, owner):
        Truck.__init__(self, id, owner)

        self.capacity = 10


    def getCapacity(self):
        return self.capacity

    def getPrice(self):
        return 70

    def __repr__(self):
        return str(self.id + ' capacidade: ' + str(self.capacity))








class DeliveryTruck(Truck):
    def __init__(self, id, owner):
        Truck.__init__(self, id, owner)

class FiftyTruck(DeliveryTruck):
    def __init__(self, id, owner):
        Truck.__init__(self, id, owner)
        self.volume_capacity = 7

    def getCapacity(self):
        return self.volume_capacity

    def getPrice(self):
        return 25

    def __repr__(self):
        return str(self.id + " capacidade: " + str(self.volume_capacity))


class SeventyTruck(DeliveryTruck):
    def __init__(self, id, owner):
        Truck.__init__(self, id, owner)
        self.volume_capacity = 14

    def getCapacity(self):
        return self.volume_capacity

    def getPrice(self):
        return 50

    def __repr__(self):
        return str(self.id + " capacidade: " + str(self.volume_capacity))

