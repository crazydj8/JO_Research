import pandas as pd

df = pd.read_csv("data.csv")

""" 
((8 * pi^3 * e^2 * lambda(bar) * rho) / (3 * c * h * (2 * J + 1))) * (1 / n) * ((n^2 + 2)^2 / 9) * S 
"""

rho = df["RI"] * (3 / ((df["RI"] ** 2) + 2)) ** 2
numerator1 = 8 * (df["p"] ** 3) * (df["e  (esu)"] ** 2) * df["par.c.l(nm)"] * rho
denominator1 = 3 * df["c  (cm/s)"] * df["h  (cm2g/s)"] * df["2J+1"]
numerator2 = ((df["RI"] ** 2) + 2) ** 2

T = ((numerator1 / denominator1) * (1 / df["RI"]) * (numerator2 / 9))
sobs = (1 / T) * df["Integrated Area"]
print(sobs)
# print(df)