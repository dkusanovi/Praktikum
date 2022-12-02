from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# # Data for plotting
x = np.arange(0, 2, 0.01)
y = 1.88265*x - 1.25485

# (logt, logs) mjerenja
x1, y1 = (0.02189, -1.25964)
x2, y2 = (0.081587, -1.07058)
x3, y3 = (0.146128, -0.9393)
x4, y4 = (0.229597, -0.83863)
x5, y5 = (0.252853, -0.75696)
x6, y6 = (0.320838, -0.68825)
x7, y7 = (0.34308, -0.62893)
x8, y8 = (0.366734, -0.57675)
x9, y9 = (0.368597, -0.53018)
x10, y10 = (0.403692, -0.48812)


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
plt.plot(x10, y10, 'bo')


ax.set(xlabel='log $t$ [s]', ylabel='log $s$ [m]')
#        title='About as simple as it gets, folks')
ax.grid()

ax = plt.gca()
ax.set_xlim([0, 0.45])
ax.set_ylim([-1.3, -0.4])

plt.plot(x, y, "-r", label="log$s$(log$t$)")
plt.plot(x1, y1, "-b", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj3_log.png")

plt.show()