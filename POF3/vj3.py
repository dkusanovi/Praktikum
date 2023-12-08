from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(-1, 90, 0.01)

# y = 0.02259*x + 1.12*10**(-6)

y = 35693*x + 1.772

# (α_r, α_e) mjerenja
# x1, y1 = (4.52794*10**(-7), 6.328*10**(-7))
# x2, y2 = (9.0601*10**(-6), 1.2656*10**(-6))
# x3, y3 = (3.27184*10**(-5), 1.8984*10**(-6))
# x4, y4 = (5.19408*10**(-5), 2.5312*10**(-6))
# x5, y5 = (6.97893*10**(-5), 0.000003164)
# x6, y6 = (0.000107123, 3.7968*10**(-6))
# x7, y7 = (0.000165894, 4.4296*10**(-6))

x1, y1 = (4.52794*10**(-7), 1)
x2, y2 = (9.0601*10**(-6), 2)
x3, y3 = (3.27184*10**(-5), 3)
x4, y4 = (5.19408*10**(-5), 4)
x5, y5 = (6.97893*10**(-5), 5)
x6, y6 = (0.000107123, 6)
x7, y7 = (0.000165894, 7)

fig, ax = plt.subplots()
ax.plot(x, y, color='k')
plt.plot(x1, y1, 'ro')
plt.plot(x2, y2, 'ro')
plt.plot(x3, y3, 'ro')
plt.plot(x4, y4, 'ro')
plt.plot(x5, y5, 'ro')
plt.plot(x6, y6, 'ro')
plt.plot(x7, y7, 'ro')

ax.set(xlabel='$r_{n} (0)^2$ [m]', ylabel='$n$')
ax.grid()

ax = plt.gca()
ax.set_xlim([-0.00005, 0.0002])
# ax.set_ylim([0, 0.000005])
ax.set_ylim([0, 8])

plt.plot(x, y, "-k", label="regresijski pravac")
plt.plot(x1, y1, "ro", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj3.png")

plt.show()