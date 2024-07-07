from turtle import color
import matplotlib.pyplot as plt
import numpy as np


# Data for plotting
x = np.arange(-0.3, 0.1, 0.1)
y = -1.980251662*x + 1.911710303


x1, y1 = (-0.301029996, 2.50458384)
x2, y2 = (-0.259637311, 2.427129413)
x3, y3 = (-0.22184875, 2.352883385)
x4, y4 = (-0.187086643, 2.283887066)
x5, y5 = (-0.15490196, 2.218853471)
x6, y6 = (-0.124938737, 2.157988562)
x7, y7 = (-0.096910013, 2.104910119)
x8, y8 = (-0.070581074, 2.049392791)
x9, y9 = (-0.045757491, 2.00253721)
x10, y10 = (-0.022276395, 1.956168467)
x11, y11 = (0, 1.911090093)


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
plt.plot(x11, y11, 'ro')


ax.set(xlabel='log $s$', ylabel='log $J$')
ax.grid()

ax = plt.gca()
# ax.set_xlim([0.5, 1.1])
# ax.set_ylim([1, 2.4])

plt.plot(x, y, "-k", label="regresijski pravac")
plt.plot(x1, y1, "ro", label="mjerenja")
plt.legend(loc="upper right")
plt.title('log $s$ - log $J$')

fig.savefig("vj6_zdk1.png")

plt.show()