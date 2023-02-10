import numpy as np

def variableinput(y):
    q=4
    n=0
    for n in range(0, q):
        # If empty list declared then use append
        prompt = 'J value at ground state '
        y[n][0]=float(input(prompt))
        prompt = 'Integrated absorption cross section in *10^20 cm^2 '
        y[n][1]=float(input(prompt))
        prompt = 'Average wavelentgth of absorption '
        y[n][2]=float(input(prompt))
        prompt = 'Refractive index at average wavelength '
        y[n][3]=float(input(prompt))
        y[n][4]= y[n][1]*10.41*y[n][3]*(3/(y[n][3]**2+2))**2*(1+2*y[n][0])/y[n][2]

# y[0][4] is the calculated          
    
    
    
    
    