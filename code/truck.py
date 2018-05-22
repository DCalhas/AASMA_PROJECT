import company
import world_set
import math
from random import randint
import networkx as nx
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
        self.finalDestination = False
        self.miles = 0

    #returns if transport is available or not
    def getAvailability(self):
        return self.available

    def setAvailability(self, bool):
        self.available = bool

    def getMiles(self):
        return self.miles

    #starts a transportation
    def startTransportation(self, destination):
        self.available = False
        self.time_transportation = 0.05

        self.destination = destination

        self.miles += math.sqrt((self.destination[0] - self.current_location[0])**2 + (self.destination[1] - self.current_location[1])**2)

        self.current_location = (self.current_location[0] + self.time_transportation*(self.destination[0] - self.current_location[0]),
                                self.current_location[1] + self.time_transportation*(self.destination[1] - self.current_location[1]))

    #decreases the time of a transportation
    def stepTransportation(self):
        #condition to see if it is back home
        if(self.time_transportation >= 1 and self.finalDestination):
            self.available = True
            return True


        if(self.time_transportation >= 1):
            self.time_transportation = 0.05
            self.destination = world_set.districts[self.getLocal()]
            self.finalDestination = True

        self.time_transportation += 0.05
        #formula that was in the map class
        self.current_location = (self.current_location[0] + self.time_transportation*(self.destination[0] - self.current_location[0]),
                                self.current_location[1] + self.time_transportation*(self.destination[1] - self.current_location[1]))

        return False

    def getID(self):
        return self.id

    def fillGas(self, amount):
        self.gas += amount

    def getLocal(self):
        return self.local

    def getCoordinates(self):
        return self.current_location

    def getDestination(self):
        return self.destination
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



if __name__ == "__main__":
    G=nx.Graph()
    G.add_path([0,1,2])
    G.add_path([0,10,2])
    print([p for p in nx.all_shortest_paths(G,source=0,target=1)])
