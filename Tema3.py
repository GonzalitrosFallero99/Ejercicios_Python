import requests

'''
api = "e3f302b04cb29b12d06ddf8a279e9e0b"
lat = "39.4697065"
lon = "-0.3763353"

ingresa = input("Ingresa la ciudad: ")
limit ="1"
#tiempo = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&units=metric")
coordenadas = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={ingresa},&limit={limit}&appid={api}")

lat_1 = hola.json()["coord"]["lat"]

ciudad = hola.json()['name']
celsius = hola.json()['main']['temp']

print(f"hacen {ciudad} {celsius}ºC")

print(coordenadas.json())
'''

api = "e3f302b04cb29b12d06ddf8a279e9e0b"

#correo=input("Introduzca el correo ")
hola = requests.get(f"https://leakcheck.io/api/public?check=example@example.com")
print(hola.status_code)
print(hola.json())

