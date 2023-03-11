
import requests
from adressToCoords import getCoords

# Задаем ключ API
api_key = ''

def getTimeHours(origin, destination):
    originCoords = getCoords(origin)
    destinationCoords = getCoords(destination)
    url = f'https://router.hereapi.com/v8/routes?origin={originCoords[0]},{originCoords[1]}&destination={destinationCoords[0]},{destinationCoords[1]}&return=summary,typicalDuration&transportMode=car&apikey={api_key}'
    response = requests.get(url)
    route = response.json()
    travel_time = route["routes"][0]["sections"][0]["summary"]["typicalDuration"]
    if 1 > round(travel_time/60/60, 1) > 0:
        return 1
    else:
        return round(travel_time/60/60, 1)

def getDistanceKilometers(origin, destination):
    originCoords = getCoords(origin)
    destinationCoords = getCoords(destination)
    url = f'https://router.hereapi.com/v8/routes?origin={originCoords[0]},{originCoords[1]}&destination={destinationCoords[0]},{destinationCoords[1]}&return=summary,typicalDuration&transportMode=car&apikey={api_key}'
    response = requests.get(url)
    route = response.json()
    distance = route["routes"][0]["sections"][0]["summary"]["length"] / 1000
    return round(distance, 1)


