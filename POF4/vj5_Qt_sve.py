from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 400, 1)
y = 22.45606*x + 0

x1, y1 = (0, 0)
x2, y2 = (20, 437.235)
x3, y3 = (40, 1020.215)
x4, y4 = (60, 1457.45)
x5, y5 = (80, 1894.685)
x6, y6 = (100, 2331.92)
x7, y7 = (120, 2769.155)
x8, y8 = (140, 3206.39)
x9, y9 = (160, 3643.625)
x10, y10 = (180, 4226.605)
x11, y11 = (200, 4518.095)
x12, y12 = (220, 5101.075)
x13, y13 = (240, 5392.565)
x14, y14 = (260, 5829.8)
x15, y15 = (280, 6267.035)
x16, y16 = (300, 6704.27)
x17, y17 = (320, 7141.505)
x18, y18 = (340, 7578.74)
x19, y19 = (360, 7870.23)

fig, ax = plt.subplots()
ax.plot(x, y, color='k')
plt.plot(x1, y1, 'ro')
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

ax.set(xlabel='$t$ [s]', ylabel='$Q$ [J]')
ax.grid()

ax = plt.gca()
# ax.set_xlim([0.5, 1.1])
# ax.set_ylim([1, 2.4])

plt.plot(x, y, "-k", label="regresijski pravac")
plt.plot(x1, y1, "ro", label="mjerenja")
plt.legend(loc="upper left")
plt.title('d$Q$/d$t$ ukupno')

fig.savefig("vj5_Qt_sve.png")

plt.show()