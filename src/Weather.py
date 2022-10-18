from pprint import pprint
import requests


WEATHER_KEY = '922fa7db5e80194935a053d2bbab7354'
IP_KEY = '854633293d1654'


def get_current_ip() -> str:
    """
    Returns the current IP
    """
    url = 'https://api.ipify.org'
    return requests.get(url).content.decode('utf-8')


def get_current_location() -> tuple[float, float]:
    """ 
    Returns the current location in latitude and longitude
    """
    url = f'https://ipinfo.io/{get_current_ip()}?token={IP_KEY}'
    data = requests.get(url).json()
    latitude, longitude = [float(x) for x in data['loc'].split(',')]
    return (latitude, longitude)


def get_weather(latitude: float, longitude: float) -> dict:
    """
    Returns data of the weather from the given latitude and longitude
    """
    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&units=metric&exclude=hourly,minutely&appid={WEATHER_KEY}'
    return requests.get(url).json()


def get_city(city: str) -> tuple[float, float]:
    """
    Returns the current latitude and longitude of the given city
    """
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={WEATHER_KEY}'
    data = requests.get(url).json()
    pprint(data[0])
    latitude, longitude = data[0]['lat'], data[0]['lon']
    return (latitude, longitude)


def main():
    get_city(input('City: '))

if __name__ == '__main__':
    while True:
        main()