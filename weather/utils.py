import requests

def fetch_weather_data(latitude, longitude, api_key):
    """
    Fetches current weather data from OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def fetch_weather_forecast(latitude, longitude, api_key):
    """
    Fetches 5-day weather forecast from OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None