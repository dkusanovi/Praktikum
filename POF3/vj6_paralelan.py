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
    y.append(abs(-(1.56**2*math.cos(theta[i])-math.sqrt(1.56**2-math.sin(theta[i])*math.sin(theta[i])))/(1.56**2*math.cos(theta[i])+math.sqrt(1.56**2-math.sin(theta[i])*math.sin(theta[i])))))

thetan, yn = [], []
for i in x:
    theta2n = (x[i]/180)*math.pi
    thetan.append(theta2)
    yn.append(abs(-(1.53986**2*math.cos(theta[i])-math.sqrt(1.53986**2-math.sin(theta[i])*math.sin(theta[i])))/(1.53986**2*math.cos(theta[i])+math.sqrt(1.53986**2-math.sin(theta[i])*math.sin(theta[i])))))

# (kut, zeta) mjerenja
x2, y2 = (85, 0.680701137)
x3, y3 = (80, 0.462238679)
x4, y4 = (75, 0.305233848)
x5, y5 = (70, 0.193046836)
x6, y6 = (65, 0.111455643)
x7, y7 = (64, 0.099688957)
x8, y8 = (63, 0.086333169)
x9, y9 = (62, 0.078811041)
x10, y10 = (61, 0.070490738)
x11, y11 = (60, 0.070490738)
x12, y12 = (59, 0.070490738)
x13, y13 = (58, 0.06104677)
x14, y14 = (57, 0.06104677)
x15, y15 = (56, 0.070490738)
x16, y16 = (55, 0.070490738)
x17, y17 = (54, 0.070490738)
x18, y18 = (53, 0.078811041)
x19, y19 = (52, 0.078811041)
x20, y20 = (51, 0.078811041)
x21, y21 = (50, 0.078811041)
x22, y22 = (45, 0.078811041)
x23, y23 = (40, 0.093250481)

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
plt.plot(x17, y17, 'ro')
plt.plot(x18, y18, 'ro')
plt.plot(x19, y19, 'ro')
plt.plot(x20, y20, 'ro')
plt.plot(x21, y21, 'ro')
plt.plot(x22, y22, 'ro')
plt.plot(x23, y23, 'ro')

ax.set(xlabel='$α$ $[°]$', ylabel='$\zeta^{\parallel}$')
ax.grid()

ax = plt.gca()
ax.set_xlim([30, 90])
ax.set_ylim([0, 0.8])


plt.plot(x2, y2, "ro", label="mjerenja")
plt.plot(x, y, label='fit funkcije $n = 1.56$')
plt.plot(x, yn, label='fit funkcije $n = 1.53986$')
plt.legend(loc="upper left")

fig.savefig("vj6_paralelan.png")

plt.show()