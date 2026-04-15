from src.extract import fetch_weather_data, parse_weather_data
from src.transform import calculate_average_temp, find_hottest_day, find_coldest_day, add_moving_average, detect_anomalies, export_results
from src.visualization import plot_weather, plot_precipitation, plot_temperature_with_ma
import matplotlib.pyplot as plt


def main():
    df = fetch_weather_data()
    df = parse_weather_data(df)
    df = add_moving_average(df)
    df = detect_anomalies(df)

    avg_temp = round(calculate_average_temp(df), 1)

    hottest_day, hottest_temp = find_hottest_day(df)
    coldest_day, coldest_temp = find_coldest_day(df)

    print(f"Average Temperature: {avg_temp}°C")
    print(f"Hottest Temperature: {hottest_day} ({hottest_temp}°C)")
    print(f"Coldest Temperature: {coldest_day} ({coldest_temp}°C)")

    export_results(df, 'outputs/output.csv')

    plot_weather(df)
    plot_precipitation(df)
    plot_temperature_with_ma(df)

if __name__ == "__main__":
    main()
