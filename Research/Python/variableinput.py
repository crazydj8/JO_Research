import numpy as np

def variableinput(y):
    q=4
    for n in range(0, q):
        # If empty list declared then use append
        y[n][0]=float(input('J value at ground state:'))
        y[n][1]=float(input('Integrated absorption cross section in *10^20 cm^2:'))
        y[n][2]=float(input('Average wavelentgth of absorption:'))
        y[n][3]=float(input('Refractive index at average wavelength:'))
        y[n][4]= y[n][1] * 10.41 * y[n][3] * (3 / (y[n][3] ** 2 + 2)) ** 2 * (1 + 2 * y[n][0]) / y[n][2]

# y[0][4] is the calculated          
    
    
    
    
    