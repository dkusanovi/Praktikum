from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 90, 0.01)

y = 2*3.14159*(0.12/(9.81*np.cos(((x/180)math.pi))))**(1/2)

# (theta, period) mjerenja
x1, y1 = (0, 0.71)
x2, y2 = (5, 0.72)
x3, y3 = (10, 0.72)
x4, y4 = (15, 0.73)
x5, y5 = (20, 0.73)
x6, y6 = (25, 0.75)
x7, y7 = (30, 0.78)
x8, y8 = (35, 0.79)
x9, y9 = (40, 0.79)
x10, y10 = (45, 0.84)
x11, y11 = (50, 0.91)
x12, y12 = (55, 0.92)
x13, y13 = (60, 1.02)
x14, y14 = (65, 1.09)
x15, y15 = (70, 1.22)
x16, y16= (75, 1.44)
x17, y17 = (80, 1.75)
x18, y18 = (85, 2.55)


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

fig.savefig("vj1_120.png")

plt.show()