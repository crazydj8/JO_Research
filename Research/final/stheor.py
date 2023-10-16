import pandas as pd
import numpy as np

def find_stheor(df):
    l1 = []
    x = -1
    redmatele = df["reduced matrix elements"]

    for i in range(len(redmatele)):
        if pd.isna(redmatele[i]):
            x += 1
            l1.append([])
            continue
        l1[x].append(redmatele[i])
        
    l2 = []
    for i in range(len(l1)):
        l = []
        for j in l1[i]:
            j = j.strip("()")
            j = j.strip()
            jlist = list(map(float, j.split(";")))
            l.append(jlist)
        x = np.vstack(l)
        l2.append(x)

    def joparam(U):
        Utr = np.transpose(U)  # transpose of the matrix U
        UtU = Utr @ U                   # UT * U
        InvUtU = np.linalg.inv(UtU)     # inverse of the matrix
        J = InvUtU @ Utr
        return J

    newl = []
    for i in l2:
        result = np.insert(np.sum(i * joparam(i).T, axis=1).reshape(len(i), 1), 0, None)
        newl.append(result)

    df["Stheor"] = np.vstack(newl).reshape(-1, 1)
    return(df)