from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

fig, axes = plt.subplots(1, 2, figsize=(13, 4))

# Data for plotting
# x = np.arange(0, 90, 0.01)
# (U_1, U_2) mjerenja
x1, y1 = (2, 8)
x2, y2 = (4.1, 18)
x3, y3 = (6.4, 27)
x4, y4 = (8.9, 36.5)
x5, y5 = (11, 46)
x6, y6 = (13, 56)
x7, y7 = (16, 90)
axes[0].plot(x1, y1, 'go')
axes[0].plot(x2, y2, 'go')
axes[0].plot(x3, y3, 'go')
axes[0].plot(x4, y4, 'go')
axes[0].plot(x5, y5, 'go')
axes[0].plot(x6, y6, 'go')
axes[0].plot(x7, y7, 'go')


axes[0].set(xlabel='$U_1$ [V]', ylabel='$U_2$ [V]')
axes[0].grid()
axes[0].set_title('Rezultati mjerenja')

# ax = plt.gca()
axes[0].set_xlim([0, 18])
axes[0].set_ylim([0, 100])

axes[0].plot(x1, y1, "go", label="mjerenja")
axes[0].legend(loc='upper left')


# Data for plotting
x_lin = np.arange(0, 90, 0.01)
y_lin = 4.259*x_lin - 0.3071
# (U_1, U_2) mjerenja
x8, y8 = (2, 8)
x9, y9= (4.1, 18)
x10, y10 = (6.4, 27)
x11, y11 = (8.9, 36.5)
x12, y12 = (11, 46)
x13, y13 = (13, 56)
axes[1].plot(x_lin, y_lin, color='red')
axes[1].plot(x8, y8, 'bo')
axes[1].plot(x9, y9, 'bo')
axes[1].plot(x10, y10, 'bo')
axes[1].plot(x11, y11, 'bo')
axes[1].plot(x12, y12, 'bo')
axes[1].plot(x13, y13, 'bo')


axes[1].set(xlabel='$U_1$ [V]', ylabel='$U_2$ [V]')
axes[1].grid()
axes[1].set_title('Linearna regesija')

# ax = plt.gca()
axes[1].set_xlim([0, 18])
axes[1].set_ylim([0, 100])

axes[1].plot(x_lin, y_lin, "-r", label="$U_2 = |- n_2/n_1| U_1$")
axes[1].plot(x11, y11, "bo", label="mjerenja")
axes[1].legend(loc='upper left')


fig.savefig("vj6_zdk1.png")

plt.show()