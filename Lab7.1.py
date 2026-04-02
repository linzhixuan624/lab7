import json
import requests


city_name = 'Beijing'
key = ' '
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
result = json.loads(response.text)
weather_desc=result["weather"][0]["main"]
humidity=result["main"]["humidity"]
pressure=result["main"]["pressure"]
print("weather:",weather_desc)
print("humidity:",humidity)
print("pressure:",pressure)