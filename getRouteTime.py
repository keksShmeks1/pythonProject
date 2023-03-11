from getTimeTwoAdresses import getTimeHours
from getTimeTwoAdresses import getDistanceKilometers

adresses = []
adresses.append('Саратов, проспект строителей 1')
adresses.append('Москва, красная площадь')

def getTravelTime(address1, address2):
    return round(getTimeHours(address1, address2), 1)

#Считаем время в пути всего марштура, НАчало - точка- точка - начало в часах, делая остановку по часу на разгрузку\загрузку
def getRouteTimeWithoutStops(adresses):
    totalTime = {}
    for i in range(0, len(adresses)):
        if i == len(adresses) - 1:
            totalTime[f'{adresses[i]} - {adresses[0]}'] = round(getTimeHours(adresses[i], adresses[0]), 1)
        else:
            totalTime[f'{adresses[i]} - {adresses[i+1]}'] = round(getTimeHours(adresses[i], adresses[i + 1]), 1)
    return totalTime

def getRouteDistanceKilometers(adresses):
    distance = 0
    for i in range(0, len(adresses)):
        if i == len(adresses) - 1:
            distance += getDistanceKilometers(adresses[i], adresses[0])
        else:
            distance += getDistanceKilometers(adresses[i], adresses[i+1])
    return distance