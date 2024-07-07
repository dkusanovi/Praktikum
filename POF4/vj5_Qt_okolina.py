from turtle import color
import matplotlib.pyplot as plt
import numpy as np


# Data for plotting
x = np.arange(60, 600, 1)
y = 3.113643182*x -205.3679545
# y = 2.624671861*x + 0

x1, y1 = (60, 0)
x2, y2 = (120, 145.745)
x3, y3 = (180, 291.49)
x4, y4 = (240, 437.235)
x5, y5 = (300, 582.98)
x6, y6 = (360, 874.47)
x7, y7 = (420, 1020.215)
x8, y8 = (480, 1311.705)
x9, y9 = (540, 1603.195)
x10, y10 = (600, 1748.94)


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


ax.set(xlabel='$t$ [s]', ylabel='$Q$ [J]')
ax.grid()

ax = plt.gca()
# ax.set_xlim([0.5, 1.1])
# ax.set_ylim([1, 2.4])

plt.plot(x, y, "-k", label="regresijski pravac")
plt.plot(x1, y1, "ro", label="mjerenja")
plt.legend(loc="upper left")
plt.title('d$Q$/d$t$ okolina')

fig.savefig("vj5_Qt_okolina.png")

plt.show()