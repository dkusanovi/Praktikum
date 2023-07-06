from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 90, 0.01)

y = 1.279*x + 0.0178

# (I, U) mjerenja
x1, y1 = (0.1, 0.15)
x2, y2 = (0.12, 0.165)
x3, y3 = (0.14, 0.198)
x4, y4 = (0.16, 0.22)
x5, y5 = (0.18, 0.25)
x6, y6 = (0.2, 0.275)
x7, y7 = (0.22, 0.3)
x8, y8 = (0.24, 0.325)
x9, y9 = (0.26, 0.35)
x10, y10 = (0.28, 0.375)


fig, ax = plt.subplots()
ax.plot(x, y, color='#A52A2A')
plt.plot(x1, y1, 'co')
plt.plot(x2, y2, 'co')
plt.plot(x3, y3, 'co')
plt.plot(x4, y4, 'co')
plt.plot(x5, y5, 'co')
plt.plot(x6, y6, 'co')
plt.plot(x7, y7, 'co')
plt.plot(x8, y8, 'co')
plt.plot(x9, y9, 'co')
plt.plot(x10, y10, 'co')

ax.set(xlabel='$I$ [A]', ylabel='$U$ [V]')
ax.grid()

ax = plt.gca()
ax.set_xlim([0.05, 0.3])
ax.set_ylim([0.1, 0.4])

plt.plot(x, y, "-y", label="regresijski pravac")
plt.plot(x1, y1, "co", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj2_bakar.png")

plt.show()