import company
import truck
import client
import numpy as np

def setupWorld():
    client1 = client.Client("Joao", "Lisboa")
    truck1 = truck.Truck("M1", 10, "Porto")
    company1 = company.Company("Rede Expresso", [truck1])

    client1.makeOffer("Coimbra", 10, 20)
    
