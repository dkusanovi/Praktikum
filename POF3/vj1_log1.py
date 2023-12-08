from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 5, 0.1)
y = -2.337133738*x + 3.28316355

x1, y1 = (0.954242509, 1)
x2, y2 = (0.903089987, 1.204119983)
x3, y3 = (0.84509804, 1.322219295)
x4, y4 = (0.77815125, 1.477121255)
x5, y5 = (0.698970004, 1.653212514)
x6, y6 = (0.602059991, 1.892094603)
x7, y7 = (0.477121255, 2.1430148)


fig, ax = plt.subplots()
ax.plot(x, y, color='k')
plt.plot(x1, y1, 'ro')
plt.plot(x2, y2, 'ro')
plt.plot(x3, y3, 'ro')
plt.plot(x4, y4, 'ro')
plt.plot(x5, y5, 'ro')
plt.plot(x6, y6, 'ro')
plt.plot(x7, y7, 'ro')

ax.set(xlabel='log$n$', ylabel='log$m$ [g]')
ax.grid()

ax = plt.gca()
ax.set_xlim([0.4, 1])
ax.set_ylim([0.5, 2.5])

plt.plot(x, y, "-k", label="regresijski pravac")
plt.plot(x1, y1, "ro", label="mjerenja")
plt.legend(loc="upper right")
plt.title('$L$ = 1 m')

fig.savefig("vj1_log1.png")

plt.show()