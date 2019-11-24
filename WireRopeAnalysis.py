import numpy as np
import math
import matplotlib.pyplot as plt

g = 32.2
a = 4 #0.15 * g
W = 4370
l = 100
w_coef = 1.6
Su = 240000
p_Su = 4/1000
D_coef = 34
Er = 12*10**6
dw_coef = 0.067
Am_coef = 0.4
Su_nom = 106000

def getFt(d_arr, m):
    Ft = []
    for d in d_arr:
        Ft.append((W/m + w_coef * d**2 * l)*(1 + a/g))
    return Ft

def getFf(d_arr):
    Ff = []
    for d in d_arr:
        Ff.append(p_Su * Su * D_coef * d ** 2 / 2)
    return Ff

def getFb(d_arr):
    Fb = []
    for d in d_arr:
        Fb.append(Er*dw_coef*d*Am_coef*d**2/(D_coef * d))
    return Fb

def getFu(d_arr):
    Fu = []
    for d in d_arr:
        Fu.append(Su_nom * math.pi * d ** 2 / 4)
    return Fu

nd = 256
m = 1
d_arr = np.linspace(0,1.75,nd)

Ff = getFf(d_arr)
Fb = getFb(d_arr)
Fu = getFu(d_arr)


Ft = getFt(d_arr,m)
n_s = []
reached_n = False
for i in range(nd):
    n_s.append((Fu[i]-Fb[i])/Ft[i])
    if not reached_n and n_s[i] > 10:
        print(str(m) + ":" + str(d_arr[i]))
        reached_n = True
plt.plot(d_arr,n_s)
plt.plot(d_arr, 10 * np.ones(nd))
plt.text(0.15,10.9,"n = 10")
plt.title("Static Safety Factor as a Function of Rope Diameter")
plt.xlabel('Rope Diameter (in)')
plt.ylabel('Safety Factor')
plt.show()


Ft = getFt(d_arr,m)
n_s = []
n_f = []
reached_n = False
for i in range(nd):
    n_f.append((Ff[i]-Fb[i])/Ft[i])
    if not reached_n and n_f[i]>2.5:
        print("second one " + str(m) + ":" + str(d_arr[i]))
        reached_n = True
plt.plot(d_arr,n_f)
plt.plot(d_arr, 2 * np.ones(nd))
plt.text(0.4,2.1,"n = 2")
plt.title("Fatigue Safety Factor as a Function of Rope Diameter")
plt.xlabel('Rope Diameter (in)')
plt.ylabel('Safety Factor')
plt.show()