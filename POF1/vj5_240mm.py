from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 90, 0.01)

y = 2*3.14159*(0.24/(9.81*np.cos(((x/180)*math.pi))))**(1/2)

# (theta, period) mjerenja
x1, y1 = (0, 0.99)
x2, y2 = (5, 0.99)
x3, y3 = (10, 1.00)
x4, y4 = (15, 1.01)
x5, y5 = (20, 1.02)
x6, y6 = (25, 1.04)
x7, y7 = (30, 1.06)
x8, y8 = (35, 1.06)
x9, y9 = (40, 1.13)
x10, y10 = (45, 1.17)
x11, y11 = (50, 1.23)
x12, y12 = (55, 1.29)
x13, y13 = (60, 1.39)
x14, y14 = (65, 1.52)
x15, y15 = (70, 1.71)
x16, y16= (75, 1.94)
x17, y17 = (80, 2.36)
x18, y18 = (85, 3.21)


fig, ax = plt.subplots()
ax.plot(x, y, color='red')
plt.plot(x1, y1, 'bo')
plt.plot(x2, y2, 'bo')
plt.plot(x3, y3, 'bo')
plt.plot(x4, y4, 'bo')
plt.plot(x5, y5, 'bo')
plt.plot(x6, y6, 'bo')
plt.plot(x7, y7, 'bo')
plt.plot(x8, y8, 'bo')
plt.plot(x9, y9, 'bo')
plt.plot(x10, y10, 'bo')
plt.plot(x11, y11, 'bo')
plt.plot(x12, y12, 'bo')
plt.plot(x13, y13, 'bo')
plt.plot(x14, y14, 'bo')
plt.plot(x15, y15, 'bo')
plt.plot(x16, y16, 'bo')
plt.plot(x17, y17, 'bo')
plt.plot(x18, y18, 'bo')

ax.set(xlabel='Θ (°)', ylabel='T (s)')
#        title='About as simple as it gets, folks')
ax.grid()

ax = plt.gca()
ax.set_xlim([0, 90])
ax.set_ylim([0.5, 3.5])

plt.plot(x, y, "-r", label="T(Θ)")
plt.plot(x1, y1, "-b", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj5_240mm.png")

plt.show()