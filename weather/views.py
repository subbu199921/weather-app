from django.shortcuts import render
import requests
from .utils import fetch_weather_data, fetch_weather_forecast

# Add your OpenWeatherMap API key here
API_KEY = '8504f2c80670776b954d075dba0bc94b'

def home(request):
    """
    Homepage view with a search form.
    """
    return render(request, 'weather/home.html')

def search_location(request):
    """
    View to handle location search and display weather for the searched location.
    """
    query = request.GET.get('q')  # Get the city name from the search form
    if not query:
        return render(request, 'weather/home.html', {'error': 'Please enter a city name.'})

    # Fetch coordinates for the city using OpenWeatherMap's Geocoding API
    geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=1&appid={API_KEY}"
    response = requests.get(geocoding_url)
    if response.status_code != 200 or not response.json():
        return render(request, 'weather/home.html', {'error': 'Location not found.'})

    # Extract latitude and longitude from the Geocoding API response
    location_data = response.json()[0]
    latitude = location_data['lat']
    longitude = location_data['lon']
    location_name = location_data['name']
    country = location_data.get('country', '')

    # Fetch current weather and forecast data
    weather_data = fetch_weather_data(latitude, longitude, API_KEY)
    forecast_data = fetch_weather_forecast(latitude, longitude, API_KEY)

    # Parse the API response
    current_weather = None
    if weather_data:
        current_weather = {
            'temperature': weather_data['main']['temp'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed'],
            'wind_direction': weather_data['wind'].get('deg', 0),
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],  # Weather icon code
        }

    forecasts = []
    if forecast_data:
        for entry in forecast_data['list']:
            forecasts.append({
                'timestamp': entry['dt_txt'],
                'temperature': entry['main']['temp'],
                'humidity': entry['main']['humidity'],
                'wind_speed': entry['wind']['speed'],
                'wind_direction': entry['wind'].get('deg', 0),
                'description': entry['weather'][0]['description'],
                'icon': entry['weather'][0]['icon'],  # Weather icon code
            })

    return render(request, 'weather/location_detail.html', {
        'location': {'name': location_name, 'country': country},
        'current_weather': current_weather,
        'forecasts': forecasts,
    })