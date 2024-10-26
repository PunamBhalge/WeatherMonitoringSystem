import requests
from config import API_KEY, BASE_URL

def get_weather_data(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    print(response)
    data = response.json()
    print(data)
    return {
        "city": city,
        "main": data['weather'][0]['main'],
        "temp": data['main']['temp'],
        "feels_like": data['main']['feels_like'],
        "dt": data['dt']
    }
# get_weather_data("Delhi")