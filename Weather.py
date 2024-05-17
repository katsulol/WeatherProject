import requests as req
from key import key

inp = input("Enter your Place: ")

data = req.get(f"https://api.openweathermap.org/data/2.5/weather?q={inp}&units=metric&APPID={key}")

if data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = data.json()['weather'][0]['main']
    temp = round(data.json()['main']['temp'])

    print(f"The weather in {inp} is: {weather}")
    print(f"The temperature in {inp} is: {temp}ºC")
