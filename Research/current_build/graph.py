import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plotgraph(df):
    name = df["Transition:"].str.strip()  #stripping the blank spaces before the names of the transition
    stheor = df["Stheor"]
    sobs = df["Sobs"]
    
    # Split name, stheor and sobs into three lists based on blank rows
    l1 = []
    x = -1
    for i in range(len(stheor)):
        if pd.isna(stheor[i]):
            x += 1
            l1.append([])
            continue
        l1[x].append((name[i], stheor[i], sobs[i]))
    
    # Convert each list into a numpy array with 9 rows and 3 columns
    l2 = []
    for i in l1:
        l2.append(np.array(i).reshape(len(i), 3))
        
    for i in l2:
        # Select the two columns to plot
        y1 = i[:, 1].astype(float)
        y2 = i[:, 2].astype(float)
        x = i[:, 0]
        
        # Plot the data as a scatter plot
        plt.plot(x, y1, label="Stheor")
        plt.plot(x, y2, label="Sobs")
        plt.xlabel("Transition")
        plt.ylabel("LineStrength [Units]")
        plt.title("Comparison of Stheor and Sobs")
        plt.show()