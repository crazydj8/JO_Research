import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

l1 = []

for i in df["Glass code"].unique():
    filtered_values = df[df['Glass code'] == i]['Reuced matrix elements']
    result_list = filtered_values.tolist()
    l1.append(result_list)

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
    result = np.sum(i * joparam(i).T, axis=1).reshape(len(i), 1)
    newl.append(result)
    
df["stheor"] = np.vstack(newl)
print(df)