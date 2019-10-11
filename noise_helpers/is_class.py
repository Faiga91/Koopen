import numpy as np
def is_class(df):
    if (df["weekday"] == 0) & (11 <= df["hour"] < 16 ):
        return 1
    if (df["weekday"] == 1) &  (12 <= df["hour"] < 16):
        return 1
    if (df["weekday"] == 2) & (8 <= df["hour"] < 16):
        return 1
    if (df["weekday"] == 3) & (8 <= df["hour"] < 12):
        return 1
    if (df["weekday"] == 4) & (8 <= df["hour"] < 14):
        return 1
    return 0       