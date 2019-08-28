def Leq_indicator(row):
    """
    Determine the Indicator of Leq as one of five indicators
    """
    if row < 37:
        return "Excellent"
    elif row < 47:
        return "Good"
    elif row < 58:
        return "Fair"
    elif row <= 85: 
        return "Poor"
    else:
        return "Hazard"
def L10_indicator(row):
    """
    Determine the Indicator of L10 as one of five indicators
    """
    if row < 40:
        return "Excellent"
    elif row < 50:
        return "Good"
    elif row < 61:
        return "Fair"
    elif row <= 85: 
        return "Poor"
    else:
        return "Hazard"
def L50_indicator(row):
    """
    Detemine the Indicator of L50 as one of five indicators 
    """
    if row < 35:
        return "Excellent"
    elif row < 45:
        return "Good"
    elif row < 5:
        return "Fair"
    elif row <= 82: 
        return "Poor"
    else:
        return "Hazard"
def L90_indicator(row):
    """
    Determine the indicator of L90 as one of five indicators
    """
    if row < 32:
        return "Excellent"
    elif row < 42:
        return "Good"
    elif row < 53:
        return "Fair"
    elif row <= 79: 
        return "Poor"
    else:
        return "Hazard"
def NPL_indicator (row):
    """
    Determine the indicator of NPL as one of five indicators
    """
    if row < 37:
        return "Excellent"
    elif row <= 48:
        return "Good"
    elif row < 61:
        return "Fair"
    elif row < 93: 
        return "Poor"
    else:
        return "Hazard"
def CQI_indicator(Lbl):
    #lbls = [leq, l10, l90]
    CQI = []
    for L in Lbl:
        if any(x == "Hazard" for x in L):
            q = "Hazard"
        elif any(x == "Poor" for x in L):
            q = "Poor"
        elif (len([i for i in L if i == "Excellent"]) >= 2):
            q = "Excellent"
        elif (len([i for i in L if i == "Good"]) >= 2):
            q = "Good"
        elif (len([i for i in L if i == "Good"]) == 1) and (len([i for i in L if i == "Excellent"]) == 1): 
            q = "Good"
        else:
            q = "Fair"
        CQI.append(q)
    return CQI
def QQ(df):
    Q1 = df.iloc[:,0]
    Q2 = df.iloc[:,1]
    Q3 = df.iloc[:,2]

    QQ = list(zip(Q1,Q2,Q3))
    return QQ