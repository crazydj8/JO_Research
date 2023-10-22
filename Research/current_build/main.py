import pandas as pd
import stheor, sobs, rms, graph

df = pd.read_excel("data2.xlsx")

df = stheor.find_stheor(df)
df = sobs.find_sobs(df)
df = rms.find_rms(df)

print(df)
graph.plotgraph(df)