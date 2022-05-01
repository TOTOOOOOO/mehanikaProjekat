import numpy as np
import matplotlib.pyplot as plt
import math


dt = 1e-3


# posmatramo vremenski period od 25s
T = np.arange(0, 25, 1e-3)
V = np.zeros_like(T)
X = np.zeros_like(T)

ro = 1.293
A = 0.45
cd = 1.2
m = 80
F = 400

x = 0
v = 0

i = 0
# t100 sluzi da obelezimo za koje vreme je presao 100m
t100 = 0
brzina = 0
s = 1

for t in T:
    a = (F - 1/2*ro*cd*A*v*v)/m
    x += v*dt
    v += a*dt

    #pamtimo vreme kada je trkac presao 100m
    if x >= 100 and s:
        t100 = t
        brzina = v
        s = 0

    X[i] = x
    V[i] = v
    i += 1

plt.figure()
plt.xlabel('vreme')
plt.ylabel('brzina')
plt.plot(T, V)
plt.plot(t100, brzina, 'ro')
plt.show()

plt.figure()
plt.xlabel('vreme')
plt.ylabel('putanja')
plt.plot(T, X)
plt.plot(t100, 100, 'ro')
plt.show()

print("Dostigne 100m za ")
print(t100)
print(" brzinom od: ")
print(brzina)
print("m/s")


print("provera za maksimalnu brzinu")
print(math.sqrt(2*400 / (1.293 * 1.2 * 0.45)))

