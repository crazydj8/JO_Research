# program to calculate the theoretical line strenth of JO calculation
# Gajanan V honnavar
import numpy as np

def Sthor(O2, O4, O6, x):
    om = np.array([O2,O4,O6]) # make a matrix of the JO parameters

    sth = np.dot(om, x.transpose())

    xr = sth.transpose()
    return xr