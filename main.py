from src.data_loader import fetch_weather_data, parse_weather_data
from src.analysis import calculate_average_temp, find_hottest_day, find_coldest_day
from src.visualization import plot_weather, plot_precipitation


def main():
    data = fetch_weather_data()
    df = parse_weather_data(data)

    avg_temp = round(calculate_average_temp(df), 1)

    hottest_day, hottest_temp = find_hottest_day(df)
    coldest_day, coldest_temp = find_coldest_day(df)

    print(f"Average temperature: {avg_temp}°C")
    print(f"Hottest Day: {hottest_day} ({hottest_temp}°C)")
    print(f"Coldest Day: {coldest_day} ({coldest_temp}°C)")

    plot_weather(df)

    plot_precipitation(df)

if __name__ == "__main__":
    main()