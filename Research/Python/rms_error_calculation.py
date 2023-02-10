# calc of rms error
import numpy as np

def rms_error_calculation(y, q):
    n=0
    rms = 0
    tot=0
    for n in range(0, q):
        tot = tot+y[n][5]**2
    n=0
    for n in range(0, q):
        rms = rms + ((np.linalg.lstsq(1,n)-y[n][5])^2/tot)**0.5 

# INCOMPLETE