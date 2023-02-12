#Code to calculate A. Make sure to rename the created file every time.
#Also cancel all the auxiliary variables created so far but q.

import numpy as np

q = int(input('How many lower transitions?:'))
RI = float(input('What is the Refractive Index?:'))

#def A(q, RI):
O = np.array([])
print('Enter the value of JO parameters in order and press enter after each entry:')
for i in range(0, 3):
    O[0][i] = float(input())
e = np.array([])
SumAed = 0
for n in range(0, q):
    e[n][0] = float(input("J value at excited state:"))
    e[n][1] = float(input("Peak wavelength of emission:"))
    e[n][2] = float(input("Enter U2:"))
    e[n][3] = float(input("Enter U4:"))
    e[n][4] = float(input("Enter U6:"))
    Sed = e[n][2] * O[0][0] + e[n][3] * O[0][1] + e[n][4] * O[0][2]
    e[n][6] = 7.23e10 * RI * ((RI ** 2 + 2) / 3) ** 2 * Sed / ((2 * e[n][0] + 1) * (e[n][1] * 1e-9) ** 3)
    SumAed += e[n][6]

#calculation of Life time of states
LifeTime = 1 / SumAed

#calculation of Branching ratio
BrRatio = np.array([])
for i in range(0, q):   
    BrRatio[0][n] = e(n,6) / SumAed

#e(n,6) is the calculated Aed ;
#Check if a Amd occurs for the given transition.
#test