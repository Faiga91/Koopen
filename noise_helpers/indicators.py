import numpy as np
import math
def calcLeq(li):
    """
    Calculate Leq function takes in number of samples and calcualte Leq for a 15 mintues interval
    """
    if len(li) ==0:
        return 0
    else:
        v = li.apply(lambda x: 10**(x / 10))
        res = sum(v) / len(li)
        return 10*(math.log10(res)) 
def L10(li):
    if len(li) ==0:
        return 0
    else:
        return np.percentile(li, 90)
def L90(li):
    if len(li) ==0:
        return 0
    else:
        return np.percentile(li, 10)
def L50(li):
    if len(li) ==0:
        return 0
    else:
        return np.percentile(li, 50)
def metric (df, indicator):
    return df.resample('15T').apply(indicator)
def npl(row):
    n50 = row["L50"]
    n10 = row["L10"]
    n90 = row["L90"]
    nl = (n10 - n90) ** 2 
    nl = nl / 60
    return n50 + n10 - n90 + nl 