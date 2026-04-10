from src.data_loader import fetch_weather_data, parse_weather_data
from src.analysis import calculate_average_temp, find_hottest_day, find_coldest_day
from src.visualization import plot_weather


def main():
    data = fetch_weather_data()
    dates, temp_max, temp_min, precipitation = parse_weather_data(data)

    avg_temp = round(calculate_average_temp(temp_max, temp_min), 1)

    hottest_day, hottest_temp = find_hottest_day(dates, temp_max)
    coldest_day, coldest_temp = find_coldest_day(dates, temp_min)

    print(f"Average temperature: {avg_temp}°C")
    print(f"Hottest Day: {hottest_day} ({hottest_temp}°C)")
    print(f"Coldest Day: {coldest_day} ({coldest_temp}°C)")

    plot_weather(dates, temp_max, temp_min)


if __name__ == "__main__":
    main()