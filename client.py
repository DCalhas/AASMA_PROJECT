class Client:

    def __init__(self, id, local):
        _id = id
        _local = local

    def getId(self, id):
        return _id

    def getLocal(self, local):
        return _local

    def makeOffer(self, start, finish, amount):
        return list(start, finish, amount)
