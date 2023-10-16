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
    
    # Calculate the RMS
    rms = []
    for i in l2:
        
        
    return rms
