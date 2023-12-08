from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 5, 0.1)
y = -2.324967388*x + 3.660729916

x1, y1 = (1.041392685, 1.230448921)
x2, y2 = (1, 1.342422681)
x3, y3 = (0.954242509, 1.431363764)
x4, y4 = (0.903089987, 1.568201724)
x5, y5 = (0.84509804, 1.698970004)
x6, y6 = (0.77815125, 1.86332286)
x7, y7 = (0.698970004, 2.037426498)
x8, y8 = (0.602059991, 2.250420002)


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

ax.set(xlabel='log$n$', ylabel='log$m$ [g]')
ax.grid()

ax = plt.gca()
ax.set_xlim([0.5, 1.1])
ax.set_ylim([1, 2.4])

plt.plot(x, y, "-k", label="regresijski pravac")
plt.plot(x1, y1, "ro", label="mjerenja")
plt.legend(loc="upper right")
plt.title('$L$ = 1.5 m')

fig.savefig("vj1_log1.5.png")

plt.show()