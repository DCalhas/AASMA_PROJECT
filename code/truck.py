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
    def __init__(self, id, local):
        Truck.__init__(self, id, local)


class FiftyBus(Bus):
    def __init__(self, id, local, capacity):
        Truck.__init__(self, id, local)

        self.capacity = capacity


    def getCapacity(self):
        return self.capacity

    def getPrice():
        return 50

class SeventyBus(Bus):
    def __init__(self, id, local, capacity):
        Truck.__init__(self, id, local)

        self.capacity = capacity


    def getCapacity(self):
        return self.capacity

    def getPrice():
        return 70






class DeliveryTruck(Truck):
    def __init__(self, id, local):
        Truck.__init__(self, id, local)


class FiftyTruck(DeliveryTruck):
    def __init__(self, id, local, volume_capacity):
        Truck.__init__(self, id, local)
        self.volume_capacity = volume_capacity

    def getCapacity(self):
        return self.volume_capacity

    def getPrice():
        25

class SeventyTruck(DeliveryTruck):
    def __init__(self, id, local, volume_capacity):
        Truck.__init__(self, id, local)

    def getCapacity(self):
        return self.volume_capacity

    def getPrice():
        50



