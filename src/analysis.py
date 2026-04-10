import numpy as np

def calculate_average_temp(df):
    avg_temp = (np.mean((np.array(df["temp_max"]))) + np.mean(np.array(df["temp_max"]))) / 2
    return avg_temp


def find_hottest_day(df):
    idx = np.argmax(df["temp_max"])
    return df["date"][idx], df["temp_max"][idx]


def find_coldest_day(df):
    idx = np.argmin(df["temp_min"])
    return df["date"][idx], df["temp_min"][idx]