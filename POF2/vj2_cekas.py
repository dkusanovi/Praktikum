from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 90, 0.01)

y = 35.94*x - 1.302

# (I, U) mjerenja
x1, y1 = (0.08, 2)
x2, y2 = (0.09, 2.1)
x3, y3 = (0.1, 2.2)
x4, y4 = (0.11, 2.5)
x5, y5 = (0.12, 2.8)
x6, y6 = (0.13, 3)
x7, y7 = (0.14, 3.3)
x8, y8 = (0.15, 4)
x9, y9 = (0.16, 4.8)
x10, y10 = (0.17, 5.2)


fig, ax = plt.subplots()
ax.plot(x, y, color='#A52A2A')
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

ax.set(xlabel='$I$ [A]', ylabel='$U$ [V]')
ax.grid()

ax = plt.gca()
ax.set_xlim([0.06, 0.2])
ax.set_ylim([1, 5.5])

plt.plot(x, y, "-k", label="regresijski pravac")
plt.plot(x1, y1, "bo", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj2_cekas.png")

plt.show()