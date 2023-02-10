# This program calculates the Sed value from equation 28 from B.Walsh J-O theory: principles and practices

import numpy as np
import scipy as sp


# Experimental Line strength from integrated absorption values

def linstren(q, RI):
    lst = []
    a = []
    S = np.array([])
    for i in range(0, q):
        s1 = float(input('Enter the value of 2J+1 for the ground state: '))
        s2 = float(input('Enter the value of Integrated absorption cross section in 10^-20 cm^2-nm:'))
        s3 = float(input('Enter the value of Average wavelength in nm: '))
        s4 = (9 / ((RI ** 2) + 2) ** 2)
        s5 = (10.42 * s1 * RI * s4 * s2) / s3
        s6 = (1.080e11 / (s1 * s3 * s4 * RI))
        lst.append(s5)
        a.append(s6)
    S = np.reshape(lst, (q, 1))
    A = np.array([a])
    return S, A


# Input the reduced matrix elements one by one

def redMat(q):
    lst1 = []
    U = np.array([])
    print('\n Enter the values of 3 reduced matrix at a time \n starting from the lowest                energy trnsition \n')
    for i in range(0, q):
        u1 = float(input('U2: '))
        u2 = float(input('U4: '))
        u3 = float(input('U6: '))
        lst1.append(u1)
        lst1.append(u2)
        lst1.append(u3)
        U = np.vstack([lst1])
    U = np.reshape(U, (q, 3))
    return U


# Calculation of Omega matrix by least-squared method

def joparam(U):
    Utr = np.transpose(U)  # transpose of the matrix U
    UtU = Utr @ U                   # UT * U
    InvUtU = np.linalg.inv(UtU)     # inverse of the matrix
    J = InvUtU @ Utr
    return J


# Calculate the theoretical line-strength using JO parameters and Reduced matrix elements

def stheor(J, X):
    return X @ J


# Calculation of RMS deviation in theoretical and experimental linestrenght

def relrms(q, Sexp, Sth):
    Err = (Sexp - Sth) / Sexp
    delta = np.sqrt(Err**2 / (q - 3))
    return delta


# Calculation of Error in estimation of JO parameters

def joErr(A, X):
    C = A @ X
    kai = (np.transpose(C) @ C)
    kaisq = np.sqrt(1/kai)
    return kaisq

# Calculate the transition probabilities from a higher level to all the lower lying levels

def Aexp(q, RI):
    #RI = 2.42
    #q = 3
    for i in range(1, q):
        jj = int(input('Enter "2J+1" value of the excited transition:'))
        for j in range(1, q-1):
            ml = float(
                input('\n Enter the wavelength difference of the 2 leves in nm: '))
            a = (7.19e10 * RI * ((RI ** 2) + 2) ** 2) / (9 * jj * (ml * 1e-9) ** 3)
            print('the value is:', a)
    return a


# Input the number of transitions for which the JO parameter needed to be calculated
# Since there are three unknowns the transitions should be greater than 3
print('\n As JO parameters are Three in number the transitions should be > 3 \n The more the better!! \n\n ')
q = int(input('\n Number of measured transitions =   '))
RI = float(input('\n\n Enter the value of Refractive Index:  \n '))

(o_linstrength, A) = linstren(q, RI)
reduced_mat = redMat(q)
omega = joparam(reduced_mat)
t_linstrength = stheor(omega, reduced_mat)
rms_mat = relrms(q, o_linstrength, t_linstrength)
