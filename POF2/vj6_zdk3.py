from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 90, 0.01)

y = 7*x - 0.6667

# (theta, period) mjerenja
x1, y1 = (2, 13)
x2, y2 = (3, 21)
x3, y3 = (4, 27)


fig, ax = plt.subplots()
ax.plot(x, y, color='#A52A2A')
plt.plot(x1, y1, 'ko')
plt.plot(x2, y2, 'ko')
plt.plot(x3, y3, 'ko')

ax.set(xlabel='$|-n_2/n_1|$', ylabel='$U_2$ [V]')
ax.grid()

ax = plt.gca()
ax.set_xlim([1, 5])
ax.set_ylim([0, 40])

plt.plot(x, y, "-m", label="$U_2 =U_1 |- n_2/n_1|$")
plt.plot(x1, y1, "ko", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj6_zdk3.png")

plt.show()