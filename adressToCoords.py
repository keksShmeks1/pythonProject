import requests

# Задайте свой API-ключ от Mapbox
api_key = 'pk.eyJ1Ijoia2Vrc2luZyIsImEiOiJjbGU0czV1MnkwNXliM29vN2s5NnlsbzVwIn0.oymQxZFX2sKAXN1I77wA4Q'

# Задайте адрес, который нужно преобразовать
address = 'Москва, Красная площадь'

# Формируем запрос к API геокодера
# url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json?access_token={api_key}'

# Отправляем запрос и получаем ответ в формате JSON
# response = requests.get(url).json()

# Извлекаем координаты из ответа
# longitude, latitude = response['features'][0]['center']

def getCoords(address):
    url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json?access_token={api_key}'
    response = requests.get(url).json()
    longitude, latitude = response['features'][0]['center']
    return latitude, longitude




# print(f'Координаты адреса "{address}": {latitude}, {longitude}')
