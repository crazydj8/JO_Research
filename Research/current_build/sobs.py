import pandas as pd
import numpy as np

def find_sobs(df):
    e = df["e(esu)"]
    center = df["center(lambda)"]
    rho = df["concentration(rho)"]
    light_speed = df["speed of light"]
    h = df["h(cgs unit)"]
    val_2jplus1 = df["2J+1"]
    mul_const = df["RI*(3/RI^2+2)^2"]

    T = ((8 * np.pi ** 3  * e ** 2 * center * rho) / (3 * light_speed * h * val_2jplus1)) * mul_const
    df["Sobs"] = ((1 / T) * df["Integrated Area"]) / (10 ** -20)
    return(df)
