import numpy as np

def calculate_average_temp(temp_max, temp_min):
    avg_temp = (np.mean((np.array(temp_max))) + np.mean(np.array(temp_min))) / 2
    return avg_temp


def find_hottest_day(dates, temp_max):
    idx = np.argmax(temp_max)
    return dates[idx], temp_max[idx]


def find_coldest_day(dates, temp_min):
    idx = np.argmin(temp_min)
    return dates[idx], temp_min[idx]