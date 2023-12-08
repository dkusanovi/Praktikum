from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 90, 0.01)

# (lambda, n) mjerenja
x1, y1 = (667.24, 1.3215)
x2, y2 = (631.52, 1.3228)
x3, y3 = (553.6, 1.3252)
x4, y4 = (467.31, 1.3283)
x5, y5 = (456.13, 1.3289)
x6, y6 = (434.17, 1.3304)
x7, y7 = (414.01, 1.3313)

fig, ax = plt.subplots()
plt.plot(x1, y1, 'ro')
plt.plot(x2, y2, 'ro')
plt.plot(x3, y3, 'ro')
plt.plot(x4, y4, 'ro')
plt.plot(x5, y5, 'ro')
plt.plot(x6, y6, 'ro')
plt.plot(x7, y7, 'ro')

ax.set(xlabel='$\lambda$ [nm]', ylabel='$n$')
ax.grid()

ax = plt.gca()
ax.set_xlim([400, 700])
ax.set_ylim([1.32, 1.334])

plt.plot(x1, y1, "ro", label="mjerenja")
plt.legend(loc="upper right")

fig.savefig("vj4_vodena.png")

plt.show()