# calc of rms error
import numpy as np

<<<<<<< HEAD
def rms_error_calculation(y, q):
=======
def rms_error_calculation(y, q, tls):
    n=0
>>>>>>> fdbf47b4e2f0bebc1c73d08e296220afb353649d
    rms = 0
    tot=0
    for n in range(0, q):
        tot = tot+y[n][5]**2
<<<<<<< HEAD
        rms = rms + ((np.linalg.lstsq(1,n)-y[n][5])^2/tot)**0.5 

#still incomplete
=======
    n=0
    for n in range(0, q):
        rms = rms + ((tls[0][n]-y[n][5])^2/tot)**0.5
>>>>>>> fdbf47b4e2f0bebc1c73d08e296220afb353649d
