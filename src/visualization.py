import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

plt.style.use("seaborn-v0_8")

def plot_weather(dates, temp_max, temp_min):
    _, ax = plt.subplots(figsize=(10, 5))

    ax.plot(dates, temp_max, label="Max Temperature", marker='o', color=ListedColormap("#eb2556"))
    ax.plot(dates, temp_min, label="Min Temperature", marker='o', color=ListedColormap( "#3b82f6"))

    ax.set_title("Temperature Trends (Vienna)", fontsize=16, pad=12)
    ax.set_ylabel("°C")
    ax.set_xticklabels(dates, fontsize=10, rotation=30)

    ax.legend()
    ax.grid(True, color="#e1e8f4", linestyle='--', linewidth=0.5, alpha=0.6)

    plt.tight_layout()
    plt.show()