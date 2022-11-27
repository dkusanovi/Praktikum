from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

fig, axes = plt.subplots(1, 2, figsize=(13, 4))

# # Data for plotting
xl = np.arange(0, 2, 0.01)
yl = 0.3222*xl + 0.003204
# (phi, moment) mjerenja
x1, y1 = (0.1745, 0.052)
x2, y2 = (0.3491, 0.124)
x3, y3 = (0.5236, 0.168)
x4, y4 = (0.6981, 0.236)
x5, y5 = (0.8727, 0.284)
x6, y6 = (1.0472, 0.336)
axes[0].plot(xl, yl, color='red')
axes[0].plot(x1, y1, 'bo')
axes[0].plot(x2, y2, 'bo')
axes[0].plot(x3, y3, 'bo')
axes[0].plot(x4, y4, 'bo')
axes[0].plot(x5, y5, 'bo')
axes[0].plot(x6, y6, 'bo')


axes[0].set(xlabel='Ф [rad]', ylabel='M [Nm]')
axes[0].set_title('Lijeva strana')
axes[0].grid()

# axes[0] = plt.gca()
axes[0].set_xlim([0, 1.1])
axes[0].set_ylim([0, 0.4])

axes[0].plot(xl, yl, "-r", label="M = $D_t$ Ф ")
axes[0].plot(x1, y1, "-b", label="mjerenja")
axes[0].legend(loc='upper left')




# # Data for plotting
xd = np.arange(0, 2, 0.01)
yd = 0.3261*xd + 0.006137
# (phi, moment) mjerenja
x7, y7 = (0.1745, 0.056)
x8, y8 = (0.3491, 0.124)
x9, y9 = (0.5236, 0.176)
x10, y10 = (0.6981, 0.24)
x11, y11 = (0.8727, 0.3)
x12, y12 = (1.0472, 0.336)
axes[1].plot(xd, yd, color='red')
axes[1].plot(x7, y7, 'bo')
axes[1].plot(x8, y8, 'bo')
axes[1].plot(x9, y9, 'bo')
axes[1].plot(x10, y10, 'bo')
axes[1].plot(x11, y11, 'bo')
axes[1].plot(x12, y12, 'bo')


axes[1].set(xlabel='Ф [rad]', ylabel='M [Nm]')
axes[1].grid()
axes[1].set_title('Desna strana')

# axes[1] = plt.gca()
axes[1].set_xlim([0, 1.1])
axes[1].set_ylim([0, 0.4])

axes[1].plot(xd, yd, "-r", label="M = $D_t$ Ф ")
axes[1].plot(x8, y8, "-b", label="mjerenja")
axes[1].legend(loc='upper left')

fig.savefig("vj8_al_staticka.png")

plt.show()