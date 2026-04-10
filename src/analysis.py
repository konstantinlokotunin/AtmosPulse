import numpy as np

def calculate_average_temp(temp_max, temp_min):
    arr = np.array(temp_max) + np.array(temp_min)
    return (np.mean(arr))


def find_hottest_day(dates, temp_max):
    idx = np.argmax(temp_max)
    return dates[idx], temp_max[idx]


def find_coldest_day(dates, temp_min):
    idx = np.argmin(temp_min)
    return dates[idx], temp_min[idx]