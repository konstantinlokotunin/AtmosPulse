import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

plt.style.use("seaborn-v0_8")

def plot_weather(df):
    _, ax = plt.subplots(figsize=(10, 5))

    x = np.arange(len(df["date"]))

    ax.set_xticks(x)
    ax.set_xticklabels(df["date"], fontsize=10, rotation=30)

    ax.plot(x, df["temp_max"], label="Max Temperature", marker='o', color="#eb2556")
    ax.plot(x, df["temp_min"], label="Min Temperature", marker='o', color="#3b82f6")

    ax.set_title("Temperature Trends (Vienna)", fontsize=16, pad=12)
    ax.set_ylabel("°C")

    ax.legend()
    ax.grid(True, color="#e1e8f4", linestyle='--', linewidth=1, alpha=0.6)

    plt.tight_layout()
    plt.savefig("outputs/weather_data.png", dpi=300)
    plt.show()

def plot_precipitation(df):

    _, ax = plt.subplots(figsize=(10, 4))

    ax.bar(df["date"], df["precipitation"], color="#60a5fa")

    ax.set_title("Daily Precipitation (Vienna)", fontsize=16, pad=12)
    ax.set_ylabel("mm")
    ax.set_xlabel("Date")

    ax.grid(axis='y', linestyle='--', linewidth=1, alpha=0.6)

    plt.xticks(fontsize=10, rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/precipitation.png", dpi=300)
    plt.show()