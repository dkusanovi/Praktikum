from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0.0000075, 0.00001, 0.000000001)
y = 1.435857689*x + 0

x1, y1 = (9.993E-06, 1.4075E-05)
x2, y2 = (9.86164E-06, 1.39729E-05)
x3, y3 = (9.60901E-06, 1.36667E-05)
x4, y4 = (9.369E-06, 1.34626E-05)
x5, y5 = (9.14068E-06, 1.31564E-05)
x6, y6 = (8.92323E-06, 1.28502E-05)
x7, y7 = (8.71589E-06, 1.25439E-05)
x8, y8 = (8.51796E-06, 1.23398E-05)
x9, y9 = (8.32882E-06, 1.21357E-05)
x10, y10 = (8.1479E-06, 1.18295E-05)
x11, y11 = (7.97467E-06, 1.16253E-05)


fig, ax = plt.subplots()
ax.plot(x, y, color='g')
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
plt.plot(x11, y11, 'bo')


ax.set(xlabel='$p^{-1}$ [Pa$^{-1}$]', ylabel='$V$ [m$^3$]')
ax.grid()

ax = plt.gca()
# ax.set_xlim([0.5, 1.1])
# ax.set_ylim([1, 2.4])

plt.plot(x, y, "-g", label="regresijski pravac")
plt.plot(x1, y1, "bo", label="mjerenja")
plt.legend(loc="upper left")
plt.title('ovisnost $V-1/p$')

fig.savefig("vj1_Vp.png")

plt.show()