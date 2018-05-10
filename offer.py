class Offer:

    def __init__(self, start, finish, amount, value):
        self.start = start
        self.finish = finish
        self.amount = amount
        self.value = value

    def getStart(self):
        return self.start

    def setStart(self, start):
        self.start = start

    def getFinish(self):
        return self.finish

    def setFinish(self, finish):
        self.finish = finish

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value 
