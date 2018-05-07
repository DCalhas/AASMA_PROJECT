class Company:

    def __init__(self, id, list_trucks, profit, list_clients):
        _id = id
        _trucks = list_trucks
        _profit = 0
        _clients = list_clients

    def getID(self):
        return _id

    def addTruck(self, truck):
        _trucks.append(truck)

    def delTruck(self, truck):
        _trucks.remove(truck)

    def addClient(self, client):
        _clients.append(client)

    def delClient(self, client):
        _clients.remove(client)

    def getProfit(self):
        return _profit

    def setProfit(self, profit):
        _profit = profit
