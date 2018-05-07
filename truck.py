class Truck:

    def __init__(self, id, capacity):
        _id = id
        _capacity = capacity
        _gas = 0
        _available = True

    def getID(self):
        return _id

    def getCapacity(self):
        return _capacity

    def setCapacity(self, capacity):
        _capacity = capacity

    def fillGas(self, amount):
        _gas += amount
    
