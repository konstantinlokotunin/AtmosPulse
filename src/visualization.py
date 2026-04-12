import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

plt.style.use("seaborn-v0_8")

def plot_weather(df):
    _, ax = plt.subplots(figsize=(10, 5))

    x = np.arange(len(df["date"]))

    ax.set_xticks(x)
    ax.set_xticklabels(df["date"], fontsize=11, rotation=30)

    ax.plot(x, df["temp_max"], label="Max Temperature °C", marker='o', linewidth=2, color="#eb2556")
    ax.plot(x, df["temp_min"], label="Min Temperature °C", marker='o', linewidth=2, color="#3b82f6")

    ax.set_title("Daily Temperature °C (Vienna)", fontsize=17, pad=12)
    ax.set_ylabel("°C")

    y_min = int(df["temp_min"].min())
    y_max = int(df["temp_max"].max())
    ax.set_yticks(np.arange(y_min, y_max + 1, 3))

    ax.tick_params(axis='y', labelsize=11)

    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.savefig("outputs/weather_data.png", dpi=300)

def plot_precipitation(df):

    _, ax = plt.subplots(figsize=(10, 4))

    width = 0.35

    ax.bar(df["date"], df["precipitation"], width, color="#60a5fa")

    ax.set_title("Daily Precipitation (Vienna)", fontsize=17, pad=12)
    ax.set_ylabel("mm")

    y_max = int(df["precipitation"].max()) + 2

    ax.set_yticks(np.arange(0, y_max + 1))

    ax.tick_params(axis='y', labelsize=11)

    ax.grid(True, linestyle='--', alpha=0.6)

    plt.xticks(fontsize=11, rotation=30)
    plt.tight_layout()
    plt.savefig("outputs/precipitation.png", dpi=300)

def plot_temperature_with_ma(df):

    _, ax = plt.subplots(figsize=(10, 5))

    y = np.arange(-10, 41, 5)

    ax.plot(df["date"], df["temp_avg"], label="Daily Average Temperature °C", linewidth=2, marker='o')
    ax.plot(df["date"], df["temp_ma"], label="Moving Average (2d)", linewidth=1, linestyle='--')

    anomalies = df[df["anomaly"]]

    ax.scatter(
        anomalies["date"],
        anomalies["temp_avg"],
        color="#7d0926",
        label="Anomalies",
        zorder=3
    )

    ax.set_title("Temperature °C Trends (Vienna)", fontsize=17, pad=12)
    ax.set_ylabel("°C")

    y_min = int(df["temp_avg"].min())
    y_max = int(df["temp_avg"].max())

    ax.set_yticks(np.arange(y_min, y_max + 1))
    
    ax.tick_params(axis='y', labelsize=11)

    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)

    plt.xticks(fontsize=11, rotation=30)
    plt.tight_layout()
    plt.savefig("outputs/temp_trend.png", dpi=300)