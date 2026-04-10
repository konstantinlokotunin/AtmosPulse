import requests
import pandas as pd

def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 48.2082,
        "longitude": 16.3738,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "Europe/Berlin"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()  # 💥 crash if API fails
    
    data = response.json()

    return data


def parse_weather_data(data):
    daily = data["daily"]

    df = pd.DataFrame({
        "date": pd.to_datetime(daily["time"]),
        "temp_max": daily["temperature_2m_max"],
        "temp_min": daily["temperature_2m_min"],
        "precipitation": daily["precipitation_sum"]
    })

    return df