
import requests
from adressToCoords import getCoords

# Задаем адреса начальной и конечной точек
origin = 'Саратов, проспект строителей 1'
destination = 'Саратов улица Лунная 41а'

# originCoords = getCoords(origin)
# destinationCoords = getCoords(destination)
# print(originCoords)
# print(destinationCoords)

# Задаем ключ API
api_key = '3FMbqq8CXlmYwxzrALFPFZn4CGnRVIGifPzflGAhY6E'

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






# Формируем URL для запроса маршрута

# url = f'https://router.hereapi.com/v8/routes?origin={originCoords[0]},{originCoords[1]}&destination={destinationCoords[0]},{destinationCoords[1]}&return=summary,typicalDuration&transportMode=car&apikey={api_key}'
#
# # Отправляем запрос и получаем ответ
# response = requests.get(url)
# route = response.json()
#
# # Получаем информацию о маршруте
# travel_time = route["routes"][0]["sections"][0]["summary"]["typicalDuration"]
# # Выводим результат
# print(f"Время в пути от {origin} до {destination} на основе типичного времени дня: {round(travel_time/60/60, 1)} Часов")
