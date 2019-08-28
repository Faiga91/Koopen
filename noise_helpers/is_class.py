import numpy as np
def is_class(df):
    b1 = df["Day"]== "Monday" 
    b2 = df["hour"].between(11,16)
    b = [b1] and [b2]
    df["class1"] = np.where(b, 1, 0).reshape(-1,1)
    b1 = df["Day"]== "Tuesday" 
    b2 = df["hour"].between(12,16)
    b = [b1] and [b2]
    df["class2"] = np.where(b, 1, 0).reshape(-1,1)
    b1 = df["Day"]== "Wensday" 
    b2 = df["hour"].between(8,16)
    b = [b1] and [b2]
    df["class3"] = np.where(b, 1, 0).reshape(-1,1)
    b1 = df["Day"]== "Thursday" 
    b2 = df["hour"].between(8,12)
    b = [b1] and [b2]
    df["class4"] = np.where(b, 1, 0).reshape(-1,1)
    b1 = df["Day"]== "Friday" 
    b2 = df["hour"].between(8,14)
    b = [b1] and [b2]
    df["class5"] = np.where(b, 1, 0).reshape(-1,1)
    df["is_class"] = np.array([df["class1"]] or [df["class2"]] or [df["class3"]] or [df["class4"]] or [df["class5"]]).reshape(-1,1)
    df = df.drop(["class1", "class2", "class3" , "class4" , "class5"] , axis=1)
    return df