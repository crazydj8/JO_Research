# Calculation of the transponse of the reduced matrix elements
import numpy as np

# Part 1 - U^2 values input - input from low to high energy
def Redmat():
    x=np.array([]) # U(n)^2 matrix
    q = int(input('number of transitions:'))

    for a in range(0, q):
        x[a][0] = float(input("U2:"))
        x[a][1] = float(input("U4:"))
        x[a][2] = float(input("U6:"))

    # Part 2- transpose matrix x
    xt = x.transpose()

    # Part 3 - transpose * original
    p=np.dot(xt, x) #product xt * x

    # Part 4 - inverse of p
    ip = np.linalg.inv(p)

    # Part 5 - ip * xt
    f = np.dot(ip, xt)

    return x, xt, p, ip, f