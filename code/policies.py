import company
import truck



def policyPercentageEachTruckType(c):
    trucks = c.getTrucks()


    percentageByType = [0, 0, 0, 0]
    numberTranports = len(trucks)
    for t in trucks:
        if type(t) is truck.FiftyBus:
            percentageByType[0] += 1
        elif type(t) is truck.SeventyBus:
            percentageByType[2] += 1
        elif type(t) is truck.FiftyTruck:
            percentageByType[1] += 1
        elif type(t) is truck.SeventyTruck:
            percentageByType[3] += 1

    if(numberTranports == 0):
        return [0.25, 0.25, 0.25, 0.25]
    
    summ = 0
    for i in range(len(percentageByType)):       
        percentageByType[i] = 1 - percentageByType[i]/numberTranports
        summ += percentageByType[i]
    
    #normalize
    for i in range(len(percentageByType)):
        percentageByType[i] /= summ

    return percentageByType

def policyBuyMidSimulation(c, policy="uniform"):
    if(policy == "uniform"):
        return [0.25, 0.25, 0.25, 0.25]
    elif(policy == "percentage"):
        return policyPercentageEachTruckType(c)


    return [0.25, 0.25, 0.25, 0.25]
