import company
import world_set
from random import randint

class Truck:

    def __init__(self, id, owner):
        self.id = owner.getId() + str(id)
        self.gas = 0
        self.available = True
        self.home = owner.getLocal()
        self.local = owner.getLocal()
        self.current_location = world_set.districts[owner.getLocal()]

        self.time_transportation = 0
        #destination is undefined in the beginning 
        self.destination = (-1, -1)

    #returns if transport is available or not
    def getAvailability(self):
        return self.available

    #starts a transportation
    def startTransportation(self, destination):
        self.available = False
        self.time_transportation = 0.9

        self.destination = destination

        self.current_location = (self.current_location[0] + self.time_transportation*(destination[0] - self.current_location[0]), 
                                self.current_location[1] + self.time_transportation*(destination[1] - self.current_location[1]))

    #decreases the time of a transportation
    def stepTransportation(self):
        if(self.time_transportation == 1):
            self.time_transportation = 0.8
            self.destination = world_set.districts[self.home]

        self.time_transportation += 0.1
        #formula that was in the map class
        self.current_location = (self.current_location[0] + self.time_transportation*(self.destination[0] - self.current_location[0]), 
                                self.current_location[1] + self.time_transportation*(self.destination[1] - self.current_location[1]))

        if(self.current_location == world_set.districts[self.home]):
            self.available = True
            return True

        return False

    def getID(self):
        return self.id

    def fillGas(self, amount):
        self.gas += amount

    def getLocal(self):
        return self.local

    def getCoordinates(self):
        return self.current_location

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

