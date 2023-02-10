# Calculation of the transponse of the reduced matrix elements
import numpy as np

# Part 1 - U^2 values input - input from low to high energy
def Redmat():
    x=np.array([]) # U(n)^2 matrix
    xa = [] # Elements in row 'a'
    q=0 # number of transitions
    prompt = 'number of transitions '
    q = int(input(prompt))

    for a in range(0, q):
        prompt = 'U2 '
        xa.append(float(input(prompt)))
        prompt = 'U4 '
        xa.append(float(input(prompt)))
        prompt = 'U6 '
        xa.append(float(input(prompt)))
        x=np.vstack([xa])
    x = np.reshape(x, (q, 3))

    # Part 2- transpose matrix x
    xt=x.transpose()

    # Part 3 - transpose * original
    p=np.dot(xt, x) #product xt * x

    # Part 4 - inverse of p
    ip=np.linalg.inv(p)

    # Part 5 - ip * xt
    f = np.dot(ip, xt)

    return x, xt, p, ip, f