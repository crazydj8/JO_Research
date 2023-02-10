# program to calculate the theoretical line strenth of JO calculation
# Gajanan V honnavar
import numpy as np

def Sthor(O2, O4, O6, x):
    Om = [O2,O4,O6] # make a matrix of the JO parameters

    Sth = np.dot(Om, x.transpose())

    Xr = Sth.transpose()
    return Xr