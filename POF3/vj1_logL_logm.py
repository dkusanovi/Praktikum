from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(-1, 5, 0.1)
y = 2.144353717*x + 1.20015444
y_teorija = 2*x + 1.255229462

x1, y1 = (0, 1.204119983)
x2, y2 = (0.176091259, 1.568201724)
x3, y3 = (0.301029996, 1.851258349)


fig, ax = plt.subplots()
ax.plot(x, y, color='k')
plt.plot(x1, y1, 'ro')
plt.plot(x2, y2, 'ro')
plt.plot(x3, y3, 'ro')

ax.set(xlabel='log$L$ [m]', ylabel='log$m$ [g]')
ax.grid()

ax = plt.gca()
ax.set_xlim([-0.2, 0.5])
ax.set_ylim([1, 2])

plt.plot(x, y, "-k", label="regresijski pravac")
plt.plot(x, y_teorija, "-g", label="teorijska vrijednost")
plt.plot(x1, y1, "ro", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj1_logL_logm.png")

plt.show()