from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

fig, axes = plt.subplots(1, 2, figsize=(13, 4))

# # Data for plotting
xl = np.arange(0, 2, 0.01)
yl = 0.5639*xl - 0.02993
# (phi, moment) mjerenja
x1, y1 = (0.087, 0.0196)
x2, y2 = (0.1745, 0.0634)
x3, y3 = (0.2618, 0.123)
x4, y4 = (0.3491, 0.166)
x5, y5 = (0.4363, 0.224)
x6, y6 = (0.5236, 0.258)
x7, y7 = (0.6109, 0.312)
x8, y8 = (0.6981, 0.365)
x9, y9 = (0.7854, 0.414)
axes[0].plot(xl, yl, color='red')
axes[0].plot(x1, y1, 'bo')
axes[0].plot(x2, y2, 'bo')
axes[0].plot(x3, y3, 'bo')
axes[0].plot(x4, y4, 'bo')
axes[0].plot(x5, y5, 'bo')
axes[0].plot(x6, y6, 'bo')
axes[0].plot(x7, y7, 'bo')
axes[0].plot(x8, y8, 'bo')
axes[0].plot(x9, y9, 'bo')


axes[0].set(xlabel='Ф [rad]', ylabel='M [Nm]')
axes[0].grid()
axes[0].set_title('Lijeva strana')

# ax = plt.gca()
axes[0].set_xlim([0, 0.8])
axes[0].set_ylim([0, 0.5])

axes[0].plot(xl, yl, "-r", label="M = $D_t$ Ф ")
axes[0].plot(x1, y1, "-b", label="mjerenja")
axes[0].legend(loc='upper left')


# # Data for plotting
xd = np.arange(0, 2, 0.01)
yd = 0.5508*xd  - 0.02523
# (phi, moment) mjerenja
x10, y10 = (0.087, 0.0278)
x11, y11 = (0.1745, 0.068)
x12, y12 = (0.2618, 0.115)
x13, y13 = (0.3491, 0.167)
x14, y14 = (0.4363, 0.216)
x15, y15 = (0.5236, 0.267)
x16, y16 = (0.6109, 0.306)
x17, y17 = (0.6981, 0.359)
x18, y18 = (0.7854, 0.410)
axes[1].plot(xd, yd, color='red')
axes[1].plot(x10, y10, 'bo')
axes[1].plot(x11, y11, 'bo')
axes[1].plot(x12, y12, 'bo')
axes[1].plot(x13, y13, 'bo')
axes[1].plot(x14, y14, 'bo')
axes[1].plot(x15, y15, 'bo')
axes[1].plot(x16, y16, 'bo')
axes[1].plot(x17, y17, 'bo')
axes[1].plot(x18, y18, 'bo')


axes[1].set(xlabel='Ф [rad]', ylabel='M [Nm]')
axes[1].grid()
axes[1].set_title('Desna strana')

# ax = plt.gca()
axes[1].set_xlim([0, 0.8])
axes[1].set_ylim([0, 0.5])

axes[1].plot(xd, yd, "-r", label="M = $D_t$ Ф ")
axes[1].plot(x11, y11, "-b", label="mjerenja")
axes[1].legend(loc='upper left')

fig.savefig("vj8_cu_staticka.png")

plt.show()