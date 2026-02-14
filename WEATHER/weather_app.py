
import requests

API_KEY = "8212c2c6e1764bbd52a4d6f6587e482e"

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city + ",IN",
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)
data = response.json()

if int(data["cod"]) != 200:
    print("Error:", data["message"])
else:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print("\nWeather in", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", condition)

