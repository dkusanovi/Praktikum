from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# # Data for plotting
x = np.arange(0, 2, 0.01)
y = 48.39*x + 0.04248

# (d**2, T**2) mjerenja
x1, y1 = (0.04**2, 0.168)
x2, y2 = (0.06**2, 0.238)
x3, y3 = (0.08**2, 0.363)
x4, y4 = (0.1**2, 0.515)
x5, y5 = (0.12**2, 0.726)
x6, y6 = (0.14**2, 0.932)
x7, y7 = (0.16**2, 1.208)
x8, y8 = (0.18**2, 1.604)
x9, y9 = (0.2**2, 2.061)


fig, ax = plt.subplots()
ax.plot(x, y, color='red')
plt.plot(x1, y1, 'bo')
plt.plot(x2, y2, 'bo')
plt.plot(x3, y3, 'bo')
plt.plot(x4, y4, 'bo')
plt.plot(x5, y5, 'bo')
plt.plot(x6, y6, 'bo')
plt.plot(x7, y7, 'bo')
plt.plot(x8, y8, 'bo')
plt.plot(x9, y9, 'bo')


ax.set(xlabel='$d^2 [m^2]$', ylabel='$T^2 [s^2]$')
#        title='About as simple as it gets, folks')
ax.grid()

ax = plt.gca()
ax.set_xlim([0, 0.05])
ax.set_ylim([0, 3])

plt.plot(x, y, "-r", label="$T^2(d^2)$")
plt.plot(x1, y1, "-b", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj8_dinamicka.png")

plt.show()