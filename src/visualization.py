import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="white", context="talk")
COLORS = {
    "primary": "#2563eb",    # blue
    "secondary": "#f59e0b",  # amber/orange
    "accent": "#dc2626",     # red
    "neutral": "#6b7280",    # gray
    "water": "#0ea5e9"       # cyan (for precipitation only)
}

def plot_weather(df):
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(df["date_str"], df["temp_max"], label="Max Temperature °C", color=COLORS["primary"], marker='o', linewidth=2)
    ax.plot(df["date_str"], df["temp_min"], label="Min Temperature °C", color=COLORS["neutral"], marker='o', linewidth=2)

    ax.set_title("Daily Temperature °C (Vienna)", fontsize=17, pad=12, weight="bold")
    ax.set_ylabel("°C", fontsize=12)

    y_min = int(df["temp_min"].min())
    y_max = int(df["temp_max"].max())
    ax.set_yticks(np.arange(y_min, y_max + 2, 3))

    ax.tick_params(axis='x', labelsize=10, rotation=30)
    ax.tick_params(axis='y', labelsize=10)

    ax.legend(frameon=False)

    sns.despine(ax=ax, left=False, bottom=False)

    ax.grid(True, axis="x", color="#9ca3af", linestyle="--", alpha=0.7)
    
    for spine in ["left", "bottom", "right", "top"]:
        ax.spines[spine].set_linewidth(1.5)
        ax.spines[spine].set_color("#9ca3af")

    plt.tight_layout()
    plt.savefig("outputs/weather_data.png", dpi=300)
    plt.close(fig)

def plot_precipitation(df):

    fig, ax = plt.subplots(figsize=(10, 4))

    width = 0.35

    ax.bar(df["date_str"], df["precipitation"], width, color=COLORS["water"])

    ax.set_title("Daily Precipitation (Vienna)", fontsize=17, pad=12, weight="bold")
    ax.set_ylabel("mm", fontsize=12)

    y_max = int(df["precipitation"].max()) + 2

    ax.set_yticks(np.arange(0, y_max + 1))

    ax.tick_params(axis='x', labelsize=10, rotation=30)
    ax.tick_params(axis='y', labelsize=10)

    sns.despine(ax=ax, left=False, bottom=False)

    ax.grid(True, axis="x", color="#9ca3af", linestyle="--", alpha=0.7)
    
    for spine in ["left", "bottom", "right", "top"]:
        ax.spines[spine].set_linewidth(1.5)
        ax.spines[spine].set_color("#9ca3af")

    plt.tight_layout()
    plt.savefig("outputs/precipitation.png", dpi=300)
    plt.close(fig)

def plot_temperature_with_ma(df):

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(df["date_str"], df["temp_avg"], label="Daily Average Temperature °C", color=COLORS["primary"], linewidth=2, marker='o')
    ax.plot(df["date_str"], df["temp_ma"], label="Moving Average (2d)", color=COLORS["secondary"], linewidth=1, linestyle='--')

    anomalies = df[df["anomaly"]]

    ax.scatter(
        anomalies["date_str"],
        anomalies["temp_avg"],
        color=COLORS["accent"],
        label="Heat peaks and cold dips",
        zorder=3
    )

    ax.set_title("Temperature °C Trends (Vienna)", fontsize=17, pad=12, weight="bold")
    ax.set_ylabel("°C", fontsize=12)

    y_min = int(df["temp_avg"].min())
    y_max = int(df["temp_avg"].max())

    ax.set_yticks(np.arange(y_min, y_max + 2))
    
    ax.tick_params(axis='x', labelsize=10, rotation=30)
    ax.tick_params(axis='y', labelsize=10)

    ax.legend(frameon=False)
    
    sns.despine(ax=ax, left=False, bottom=False)

    ax.grid(True, axis="x", color="#9ca3af", linestyle="--", alpha=0.7)
    
    for spine in ["left", "bottom", "right", "top"]:
        ax.spines[spine].set_linewidth(1.5)
        ax.spines[spine].set_color("#9ca3af")

    plt.tight_layout()
    plt.savefig("outputs/temp_trend.png", dpi=300)
    plt.close(fig)