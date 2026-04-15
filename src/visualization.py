import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="white", context="talk")
COLORS = {
    "primary": "#DB5461",    
    "secondary": "#2274A5",  
    "tertiary": "#379392",    
    "quaternary": "#003249",
    "accent": "#DB5461", 
    "fifth": "#DF928E"
}

def style_ax(ax):
    # Background
    ax.set_facecolor("#F2F6F8")  # platinum

    # Grid (subtle, vertical only)
    ax.grid(True, axis="x", color="#9ca3af", linestyle="--", alpha=0.5)

    # Customize spines
    sns.despine(ax=ax, left=False, bottom=False)

    for spine in ["left", "bottom", "right", "top"]:
        ax.spines[spine].set_linewidth(1.25)
        ax.spines[spine].set_color("#9ca3af")

    # Tick styling
    ax.tick_params(axis='x', labelsize=10, rotation=30)
    ax.tick_params(axis='y', labelsize=10)

    # Labels
    ax.yaxis.label.set_color("#242424")
    ax.xaxis.label.set_color("#242424")

    # Title
    ax.title.set_color("#242424")

def plot_weather(df):
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(df["date_str"], df["temp_max"], label="Max Temperature °C", color=COLORS["primary"], marker='o', linewidth=2)
    ax.plot(df["date_str"], df["temp_min"], label="Min Temperature °C", color=COLORS["secondary"], marker='o', linewidth=2)

    ax.set_title("Daily Temperature °C (Vienna)", fontsize=17, pad=12, weight="bold")
    ax.set_ylabel("°C", fontsize=12)

    y_min = int(df["temp_min"].min())
    y_max = int(df["temp_max"].max())

    ax.set_yticks(np.arange(y_min, y_max + 2, 2))

    ax.legend(frameon=False)

    style_ax(ax)

    plt.tight_layout()
    plt.savefig("outputs/weather_data.png", dpi=300)
    plt.close(fig)

def plot_precipitation(df):

    fig, ax = plt.subplots(figsize=(10, 4))

    width = 0.35

    ax.bar(df["date_str"], df["precipitation"], width, color=COLORS["secondary"])

    ax.set_title("Daily Precipitation (Vienna)", fontsize=17, pad=12, weight="bold")
    ax.set_ylabel("mm", fontsize=12)

    y_max = int(df["precipitation"].max()) + 2

    ax.set_yticks(np.arange(0, y_max + 1))

    style_ax(ax)

    plt.tight_layout()
    plt.savefig("outputs/precipitation.png", dpi=300)
    plt.close(fig)

def plot_temperature_with_ma(df):

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(df["date_str"], df["temp_avg"], label="Daily Average Temperature °C", color=COLORS["quaternary"], linewidth=2.5, marker='o')
    ax.plot(df["date_str"], df["temp_ma"], label="Moving Average (2d)", color=COLORS["tertiary"], linewidth=1.5, linestyle='--')

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

    ax.legend(frameon=False)
    
    style_ax(ax)

    plt.tight_layout()
    plt.savefig("outputs/temp_trend.png", dpi=300)
    plt.close(fig)