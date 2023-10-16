import pandas as pd
import numpy as np
import stheor, sobs

df = pd.read_excel("data2.xlsx")

df = stheor.find_stheor(df)
df = sobs.find_sobs(df)

print(df)

#print(rms.find_rms(df))