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

    daily = data["daily"]

    df = pd.DataFrame(daily)

    return df


def parse_weather_data(df):

    df = df.rename(columns={
        "time": "date",
        "temperature_2m_max": "temp_max",
        "temperature_2m_min": "temp_min",
        "precipitation_sum": "precipitation"
    })

    df["date"] = pd.to_datetime(df["date"])

    return df[["date", "temp_max", "temp_min", "precipitation"]]