import numpy as np
import csv

def calculate_average_temp(df):
    avg_temp = (np.mean((np.array(df["temp_max"]))) + np.mean(np.array(df["temp_max"]))) / 2
    return avg_temp

def add_moving_average(df, window=2):
    df["temp_avg"] = (df["temp_max"] + df["temp_min"]) / 2
    df["temp_ma"] = df["temp_avg"].rolling(window=window).mean()

    return df

def detect_anomalies(df, threshold=2):
    df["temp_avg"] = (df["temp_max"] + df["temp_min"]) / 2
    mean_temp = df["temp_avg"].mean()

    df["difference"] = df["temp_avg"] - mean_temp

    # Flag strong deviations
    df["anomaly"] = df["difference"].abs() > threshold

    return df

def find_hottest_day(df):
    idx = np.argmax(df["temp_max"])
    return df["date"][idx], df["temp_max"][idx]


def find_coldest_day(df):
    idx = np.argmin(df["temp_min"])
    return df["date"][idx], df["temp_min"][idx]


def export_results(df, filename):
    df.to_csv(filename, sep=";", index=False)