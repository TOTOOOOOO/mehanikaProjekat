import numpy as np
import matplotlib.pyplot as plt

dt = 1e-3

DT = np.arange(0,10,0.1)
print((DT))

V = np.zeros_like(DT)
S = np.zeros_like(DT)

s = 0
ro = 1.293
A = 0.45
cd = 1.2
m = 80
F = 400
v = 0
x = 0


i = 0

for dt in DT:

    a = (F - 1/2*ro*cd*A*v*v)/m
    x += v * dt
    v += a * dt

    V[i] = v
    S[i] = x

plt.figure()
plt.plot(DT,V)
plt.xlabel("vreme")
plt.ylabel("brzina")
plt.show()