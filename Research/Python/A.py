# Code to calculate A. Make sure to rename the created file every time.
# Also cancel all the auxiliary variables created so far but q.

import numpy as np

def A(x):
    e=[[0, 0, 0, 0, 0, 0, 0]] # Changes needed later
    for n in range(0, 1):
        etemp = []
        # If e is just empty list use append
        prompt = 'J value at excited state '
        e[n][0]=float(input(prompt))
        prompt = 'Peak wavelength of emission '
        e[n][1]=float(input(prompt))
        e[n][2]=x[n][0]
        e[n][3]=x[n][1]
        e[n][4]=x[n][2]
        e[n][5]=x[n][3] # Or y[n][3] - confusion
        e[n][6]= 7.23*(10**10)*e[n][5]*((e[n][5]**2+2)/3)**2*np.linalg.lstsq(1,n)/((2*e[n][0]+1)*(e[n][1]*1*10-7)**3) # np.linalg.lststq error
    return e
# e[n][6] is the calculated Aed
# Check if a Amd occurs for the given transition.

# x=[[1,2,3,4]]
# print(A(x))

# INCOMPLETE