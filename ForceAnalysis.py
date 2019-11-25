import numpy as np
import math
import matplotlib.pyplot as plt

g = 32.2
a = 0.15 * g
W_cw = 3800
W_e = 5000
l = 100
w_coef = 1.6
Su = 240000
p_Su = 3.8/1000

def calcFtTop(W, d):
    return (W + w_coef * d**2 * l)*(1 + a/g)

def calcFtBottom(W):
    return (W)*(1 + a/g)

def getLowerCwRadialForce():
    return calcFtBottom(W_cw)

def getLowerElevatorRadialForce():
    return calcFtBottom(W_e)

def getUpperCwRadialForce(d):
    return 2**0.5*calcFtTop(W_cw/2, d)

def getUpperElevatorRadialForce(d):
    return 2**0.5*calcFtTop(W_e/2, d)