class Client:

    def __init__(self, id, local):
        self.id = id
        self.local = local

    def getId(self, id):
        return self.id

    def getLocal(self, local):
        return self.local

    def makeOffer(self, start, amount, money):
        return list(start, self.local, amount, money)
