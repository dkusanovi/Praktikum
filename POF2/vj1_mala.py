from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 90, 0.01)

y = 1.094*x + 1.341

# (α_r, α_e) mjerenja
x1, y1 = (27, 31)
x2, y2 = (24, 27)
x3, y3 = (20, 24)
x4, y4 = (18, 20)
x5, y5 = (15, 18)
x6, y6 = (13, 15)
x7, y7 = (10, 13)
x8, y8 = (9, 11)
x9, y9 = (28, 32)
x10, y10 = (24, 28)

fig, ax = plt.subplots()
ax.plot(x, y, color='#A52A2A')
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

ax.set(xlabel='$α_{r}$ [°]', ylabel='$α_{e}$ [°]')
ax.grid()

ax = plt.gca()
ax.set_xlim([8, 30])
ax.set_ylim([10, 34])

plt.plot(x, y, "-g", label="regresijski pravac")
plt.plot(x1, y1, "ro", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj1_mala.png")

plt.show()