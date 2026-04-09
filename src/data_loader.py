import requests

def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 48.2082,
        "longitude": 16.3738,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "Europe/Berlin"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data
