from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 91, 1)
theta, y = [], []
for i in x:
    theta2 = (x[i]/180)*math.pi
    theta.append(theta2)
    y.append(abs((math.sqrt(1.56**2-math.sin(theta[i])*math.sin(theta[i]))-math.cos(theta[i]))**2/(1.56**2-1))-0.03)

thetan, yn = [], []
for i in x:
    theta2n = (x[i]/180)*math.pi
    thetan.append(theta2n)
    yn.append(abs((math.sqrt(1.53986**2-math.sin(thetan[i])*math.sin(thetan[i]))-math.cos(thetan[i]))**2/(1.53986**2-1))-0.03)

# (kut, zeta) mjerenja
x2, y2 = (85, 0.811421698)
x3, y3 = (80, 0.712420594)
x4, y4 = (75, 0.621108575)
x5, y5 = (70, 0.533369252)
x6, y6 = (65, 0.459572515)
x7, y7 = (60, 0.402042201)
x8, y8 = (55, 0.356588239)
x9, y9 = (50, 0.318265775)
x10, y10 = (45, 0.286175736)
x11, y11 = (40, 0.182770819)
x12, y12 = (35, 0.08040844)
x13, y13 = (30, 0.073402527)
x14, y14 = (25, 0.056857353)
x15, y15 = (20, 0.056857353)
x16, y16 = (15, 0.046423835)

fig, ax = plt.subplots()
plt.plot(x2, y2, 'ro')
plt.plot(x3, y3, 'ro')
plt.plot(x4, y4, 'ro')
plt.plot(x5, y5, 'ro')
plt.plot(x6, y6, 'ro')
plt.plot(x7, y7, 'ro')
plt.plot(x8, y8, 'ro')
plt.plot(x9, y9, 'ro')
plt.plot(x10, y10, 'ro')
plt.plot(x11, y11, 'ro')
plt.plot(x12, y12, 'ro')
plt.plot(x13, y13, 'ro')
plt.plot(x14, y14, 'ro')
plt.plot(x15, y15, 'ro')
plt.plot(x16, y16, 'ro')

ax.set(xlabel='$α$ $[°]$', ylabel='$\zeta^{\perp}$')
ax.grid()

ax = plt.gca()
ax.set_xlim([0, 90])
ax.set_ylim([0, 1])
# ax.set_xlim([-100, 100])
# ax.set_ylim([-5, 5])

plt.plot(x2, y2, "ro", label="mjerenja")
plt.plot(x, y, label='fit funkcije $n = 1.56$')
plt.plot(x, yn, label='fit funkcije $n = 1.53986$')
plt.legend(loc="upper left")

fig.savefig("vj6_okomit.png")

plt.show()