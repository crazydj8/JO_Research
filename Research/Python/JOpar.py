# Calculation of O2, O4, O6

def Matrix_Calculation(q, f, y): #q is the number of lower transitions
    O2 = 0; O4 = 0; O6 = 0;
    for i in range(0, q):
        O2 = O2 + f[1][i] * y[i][5]
        O4 = O4 + f[2][i] * y[i][5]
        O6 = O6 + f[3][i] * y[i][5]
    
    return O2, O4, O6