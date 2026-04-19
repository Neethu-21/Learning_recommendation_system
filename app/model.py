import numpy as np

def predict_next_score(scores):
    x = np.array([1,2,3])
    y = np.array(scores)

    coef = np.polyfit(x,y,1)
    return round(coef[0]*4 + coef[1],2)

def risk_level(avg):
    if avg < 50:
        return "High Risk 🔴"
    elif avg < 65:
        return "Medium Risk 🟠"
    else:
        return "Low Risk 🟢"