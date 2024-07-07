from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 400, 1)
# y = 22.45606*x + 0

x1, y1 = (0, 34)
x2, y2 = (20, 34.1)
x3, y3 = (40, 34)
x4, y4 = (60, 34.1)
x5, y5 = (80, 34.2)
x6, y6 = (100, 34.2)
x7, y7 = (120, 34.2)
x8, y8 = (140, 34)
x9, y9 = (160, 34.2)
x10, y10 = (180, 34.1)
x11, y11 = (200, 33.9)
x12, y12 = (220, 34)
x13, y13 = (240, 33.9)
x14, y14 = (260, 33.7)
x15, y15 = (280, 33.8)
x16, y16 = (300, 33.9)
x17, y17 = (320, 33.6)
x18, y18 = (340, 33.4)
x19, y19 = (360, 33.5)

fig, ax = plt.subplots()
# ax.plot(x, y, color='c')
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

ax.set(xlabel='$t$ [s]', ylabel='$|T_2-T_1|$ [°C]')
ax.grid()

ax = plt.gca()
# ax.set_xlim([0.5, 1.1])
ax.set_ylim([20, 40])

# plt.plot(x, y, "-k", label="regresijski pravac")
plt.plot(x1, y1, "ro", label="mjerenja")
plt.legend(loc="upper left")
plt.title('')

fig.savefig("vj5_T_t.png")

plt.show()