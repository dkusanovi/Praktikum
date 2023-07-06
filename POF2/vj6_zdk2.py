from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 90, 0.01)

y = 2.088*x - 0.2585

# (theta, period) mjerenja
x1, y1 = (2, 4)
x2, y2 = (4.1, 8)
x3, y3 = (6.2, 13)
x4, y4 = (8.9, 18)
x5, y5 = (11, 23)
x6, y6 = (13, 27)
x7, y7 = (16, 33)


fig, ax = plt.subplots()
ax.plot(x, y, color='#A52A2A')
plt.plot(x1, y1, 'bo')
plt.plot(x2, y2, 'bo')
plt.plot(x3, y3, 'bo')
plt.plot(x4, y4, 'bo')
plt.plot(x5, y5, 'bo')
plt.plot(x6, y6, 'bo')
plt.plot(x7, y7, 'bo')

ax.set(xlabel='$U_1$ [V]', ylabel='$U_2$ [V]')
ax.grid()

ax = plt.gca()
ax.set_xlim([0, 18])
ax.set_ylim([0, 40])

plt.plot(x, y, "-r", label="$U_2 = |- n_2/n_1| U_1$")
plt.plot(x1, y1, "bo", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj6_zdk2.png")

plt.show()