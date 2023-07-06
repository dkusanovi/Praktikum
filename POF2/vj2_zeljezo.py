from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 90, 0.01)

y = 3.602*x + 0.0512

# (I, U) mjerenja
x1, y1 = (0.1, 0.4)
x2, y2 = (0.11, 0.45)
x3, y3 = (0.14, 0.55)
x4, y4 = (0.16, 0.65)
x5, y5 = (0.18, 0.7)
x6, y6 = (0.2, 0.77)
x7, y7 = (0.22, 0.85)
x8, y8 = (0.24, 0.9)
x9, y9 = (0.26, 0.99)
x10, y10 = (0.28, 1.06)


fig, ax = plt.subplots()
ax.plot(x, y, color='#A52A2A')
plt.plot(x1, y1, 'mo')
plt.plot(x2, y2, 'mo')
plt.plot(x3, y3, 'mo')
plt.plot(x4, y4, 'mo')
plt.plot(x5, y5, 'mo')
plt.plot(x6, y6, 'mo')
plt.plot(x7, y7, 'mo')
plt.plot(x8, y8, 'mo')
plt.plot(x9, y9, 'mo')
plt.plot(x10, y10, 'mo')

ax.set(xlabel='$I$ [A]', ylabel='$U$ [V]')
ax.grid()

ax = plt.gca()
ax.set_xlim([0.05, 0.3])
ax.set_ylim([0.2, 1.20])

plt.plot(x, y, "-g", label="regresijski pravac")
plt.plot(x1, y1, "mo", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj2_zeljezo.png")

plt.show()