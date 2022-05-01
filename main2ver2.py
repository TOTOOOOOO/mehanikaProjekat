import numpy as np
import matplotlib.pyplot as plt
import math


dt = 1e-3

ro = 1.293
pp = 0.45
cd = 1.2
m = 80
F = 400


fv = 25.8
fc = 488
tc = 0.67

T = np.arange(0,30, 1e-3)
FV = np.zeros_like(T)
FC = np.zeros_like(T)
D = np.zeros_like(T)
X = np.zeros_like(T)
A = np.zeros_like(T)
V = np.zeros_like(T)
nizSile = np.zeros_like(T)
nizSile.fill(400)

w = 0
option = input("Opcije : \n w+ : vetar -> \n w- : vetar <- \n bez vetra : nw \n")
if option == "w+":
    w = 1
elif option == "w-":
    w = -1
elif option != "nw":
    print("Lose uneta opcija")

i = 0
for tmp in T:
    nizSile[i] = 400
    i+=1
x = 0
v = 0
a = 0
i = 0
s = 1

# vreme kad je presao 100m
t100 = 0
brzina100 = 0

for t in T:
    Fv = fv*v
    Fc = fc * (math.e ** (-(t/tc) ** 2))
    trenutniPP = pp - 0.25 * pp * (math.e ** (-(t/tc) ** 2))
    d = 1/2* trenutniPP * ro * cd * (v - w)**2
    a = (F  + Fc - Fv - d)/m

    x += dt*v
    v += dt*a

    if x >= 100 and s:
        s = 0
        t100 = t
        brzina100 = v


    V[i] = v
    X[i] = x
    FV[i] = Fv
    FC[i] = Fc
    A[i] = a
    D[i] = d

    i += 1

plt.figure()
plt.title("Odnos brzine i vremena")
plt.xlabel("vreme")
plt.ylabel("brzina")
plt.plot(T, V)
plt.plot(t100,brzina100, 'ro')
plt.show()

plt.figure()
plt.title("Odnos ubrzanja i vremena")
plt.xlabel("vreme")
plt.ylabel("ubrzanje")
plt.plot(T, A)
plt.show()

plt.figure()
plt.title("Odnos putanje i vremena")
plt.xlabel("vreme")
plt.ylabel("putanja")
plt.plot(T, X)
plt.plot(t100, 100, 'ro')
plt.show()

plt.figure()
plt.title("Odnos Fv i vremena")
plt.xlabel("vreme")
plt.ylabel("Fv Fc D F")
plt.plot(T, FV, label = 'Fv', color= 'b')
plt.plot(T, D, label = 'Otpor vazduha', color = 'g')
plt.plot(T, FC, label = 'Fc', color = 'r')
plt.plot(T, nizSile, color = '#E4D00A', label = 'F')
plt.legend()
plt.grid()
plt.show()

