import requests
from dotenv import dotenv_values


class WeatherAPI:
    def __init__(self):
        self.API_KEY = dotenv_values(".env").get("API_KEY")
        self.url_city_name = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"

    def connection(self):
        url = self.url_city_name.format(city_name='London, uk', API_key=self.API_KEY)
        response = requests.get(url)
        return response.status_code

    def get(self, city_name: str) -> dict:
        url = self.url_city_name.format(city_name=city_name, API_key=self.API_KEY)
        response = requests.get(url)
        return response.json()