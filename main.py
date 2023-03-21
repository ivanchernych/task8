import sys
from io import BytesIO
import requests
from PIL import Image
from getting_coordinates import getting


toponym_to_find = ' '.join(sys.argv[1:])


geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)
print(response.url)


tompony = getting(response)


search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

address_ll = ','.join(tompony)

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)

json_response = response.json()

organization = json_response["features"][0]

org_name = organization["properties"]["CompanyMetaData"]["name"]
org_address = organization["properties"]["CompanyMetaData"]["address"]

point = organization["geometry"]["coordinates"]


print('название', org_name)
print('адрес', org_address)
print(tompony, point)
print('расстояние', ((float(tompony[0]) - point[0]) ** 2 + (float(tompony[1]) - point[1]) ** 2) ** 0.5 * 1000, 'м')

org_point = "{0},{1}".format(point[0], point[1])
delta = "0.009"

map_params = {
    "ll": address_ll,
    "spn": ",".join([delta, delta]),
    "l": "map",
    "pt": f'{org_point},pm2dgl~{address_ll},pm2dgl',
    "pl": f'{org_point},{address_ll}'
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
