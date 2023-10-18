import pandas as pd
import numpy as np

def find_rms(df):
    stheor = df["Stheor"]
    sobs = df["Sobs"]

import numpy as np

def find_rms(df):
    stheor = df["Stheor"]
    sobs = df["Sobs"]
    
    # Split stheor and sobs into three lists based on blank rows
    l1 = []
    x = -1
    for i in range(len(stheor)):
        if pd.isna(stheor[i]):
            x += 1
            l1.append([])
            continue
        l1[x].append((stheor[i], sobs[i]))
    
    # Convert each list into a numpy array with 9 rows and 2 columns
    l2 = []
    for i in l1:
        l2.append(np.array(i).reshape(len(i), 2))
    
    # Calculate the RMS = root((1 / n - p )((obs - theor)/obs)^2) where p is number of fit parameters
    rms = []
    p = 4
    for i in l2:
        rms.append(np.sqrt((1 / (len(i) - p)) * np.sum(((i[:, 1] - i[:, 0]) / i[:, 1]) ** 2)))
    
    newl = []
    for i in range(len(rms)):
        newl.append(np.insert(np.repeat(rms[i], len(l2[i])), 0, None))
    df["rms"] = np.vstack(newl).reshape(-1, 1)
    return(df)