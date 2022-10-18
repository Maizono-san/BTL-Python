from requests import get


WEATHER_KEY = '922fa7db5e80194935a053d2bbab7354'
IP_KEY = '854633293d1654'

weather_data = {}

def get_current_ip() -> str:
    """
    Returns the current IP
    """
    url = 'https://api.ipify.org'
    return get(url).content.decode('utf-8')


def get_current_location() -> tuple[float, float]:
    """ 
    Returns the current location in latitude and longitude
    """
    url = f'https://ipinfo.io/{get_current_ip()}?token={IP_KEY}'
    data = get(url).json()
    latitude, longitude = [float(x) for x in data['loc'].split(',')]
    return (latitude, longitude)


def get_weather(latitude: float, longitude: float) -> dict:
    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&units=metric&exclude=hourly,minutely&appid={WEATHER_KEY}'
    
    

def main():
    print(get_current_location())


if __name__ == '__main__':
    main()