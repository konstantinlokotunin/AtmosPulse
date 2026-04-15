import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", context="talk")
sns.despine()
sns.set_palette("deep")

def plot_weather(df):
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(df["date_str"], df["temp_max"], label="Max Temperature °C", marker='o', linewidth=2)
    ax.plot(df["date_str"], df["temp_min"], label="Min Temperature °C", marker='o', linewidth=2)

    ax.set_title("Daily Temperature °C (Vienna)", fontsize=17, pad=12, weight="bold")
    ax.set_ylabel("°C", fontsize=12)

    y_min = int(df["temp_min"].min())
    y_max = int(df["temp_max"].max())
    ax.set_yticks(np.arange(y_min, y_max + 2, 3))

    ax.tick_params(axis='y', labelsize=10)

    ax.legend(frameon=False)
    ax.grid(True, linestyle='--', alpha=0.6)

    plt.xticks(fontsize=10, rotation=30)
    plt.tight_layout()
    plt.savefig("outputs/weather_data.png", dpi=300)
    plt.close(fig)

def plot_precipitation(df):

    fig, ax = plt.subplots(figsize=(10, 4))

    width = 0.35

    ax.bar(df["date_str"], df["precipitation"], width)

    ax.set_title("Daily Precipitation (Vienna)", fontsize=17, pad=12, weight="bold")
    ax.set_ylabel("mm", fontsize=12)

    y_max = int(df["precipitation"].max()) + 2

    ax.set_yticks(np.arange(0, y_max + 1))

    ax.tick_params(axis='y', labelsize=10)

    ax.grid(True, linestyle='--', alpha=0.6)

    plt.xticks(fontsize=10, rotation=30)
    plt.tight_layout()
    plt.savefig("outputs/precipitation.png", dpi=300)
    plt.close(fig)

def plot_temperature_with_ma(df):

    fig, ax = plt.subplots(figsize=(10, 5))

    y = np.arange(-10, 41, 5)

    ax.plot(df["date_str"], df["temp_avg"], label="Daily Average Temperature °C", linewidth=2, marker='o')
    ax.plot(df["date_str"], df["temp_ma"], label="Moving Average (2d)", linewidth=1, linestyle='--')

    anomalies = df[df["anomaly"]]

    ax.scatter(
        anomalies["date_str"],
        anomalies["temp_avg"],
        color="#7d0926",
        label="Heat peaks and cold dips",
        zorder=3
    )

    ax.set_title("Temperature °C Trends (Vienna)", fontsize=17, pad=12, weight="bold")
    ax.set_ylabel("°C", fontsize=12)

    y_min = int(df["temp_avg"].min())
    y_max = int(df["temp_avg"].max())

    ax.set_yticks(np.arange(y_min, y_max + 2))
    
    ax.tick_params(axis='y', labelsize=10)

    ax.legend(frameon=False)
    ax.grid(True, linestyle='--', alpha=0.6)

    plt.xticks(fontsize=10, rotation=30)
    plt.tight_layout()
    plt.savefig("outputs/temp_trend.png", dpi=300)
    plt.close(fig)