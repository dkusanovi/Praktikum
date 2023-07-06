from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 90, 0.01)

y = 1.383*x + 5.295

# (α_r, α_e) mjerenja
x1, y1 = (19, 28)
x2, y2 = (14, 26)
x3, y3 = (12, 23)
x4, y4 = (13, 24)
x5, y5 = (8, 12)
x6, y6 = (7, 15)
x7, y7 = (10, 21)
x8, y8 = (13, 25)
x9, y9 = (10, 19)
x10, y10 = (17, 30)

fig, ax = plt.subplots()
ax.plot(x, y, color='#A52A2A')
plt.plot(x1, y1, 'mo')
plt.plot(x2, y2, 'mo')
plt.plot(x3, y3, 'mo')
plt.plot(x4, y4, 'mo')
plt.plot(x5, y5, 'mo')
plt.plot(x6, y6, 'mo')
plt.plot(x7, y7, 'mo')
plt.plot(x8, y8, 'mo')
plt.plot(x9, y9, 'mo')
plt.plot(x10, y10, 'mo')

ax.set(xlabel='$α_{r}$ [°]', ylabel='$α_{e}$ [°]')
ax.grid()

ax = plt.gca()
ax.set_xlim([5, 20])
ax.set_ylim([10, 32])

plt.plot(x, y, "-b", label="regresijski pravac")
plt.plot(x1, y1, "mo", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj1_velika.png")

plt.show()