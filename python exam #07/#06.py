import requests

def getWeatherData(city):
    apiKey = 'bfe9aeba44ff473c4d703a750f3b9ce5'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}'
    response = requests.get(url)
    data = response.json()
    return data

def displayWeatherData(data):
    temperature = round(data['main']['temp'] - 273.15)
    location = data['name']
    print(f"Harorat: {temperature}°C\nYaqin Manzil: {location}")
    
city = input("Shahar nomini kiriting: ")
data = getWeatherData(city)
displayWeatherData(data)