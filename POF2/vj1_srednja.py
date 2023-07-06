from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 90, 0.01)

y = 1.292*x + 4.2

# (α_r, α_e) mjerenja
x1, y1 = (11, 20)
x2, y2 = (6, 11)
x3, y3 = (20, 28)
x4, y4 = (15, 25)
x5, y5 = (9, 15)
x6, y6 = (12, 17)
x7, y7 = (14, 22)
x8, y8 = (10, 19)
x9, y9 = (7, 13)
x10, y10 = (16, 27)

fig, ax = plt.subplots()
ax.plot(x, y, color='#A52A2A')
plt.plot(x1, y1, 'ko')
plt.plot(x2, y2, 'ko')
plt.plot(x3, y3, 'ko')
plt.plot(x4, y4, 'ko')
plt.plot(x5, y5, 'ko')
plt.plot(x6, y6, 'ko')
plt.plot(x7, y7, 'ko')
plt.plot(x8, y8, 'ko')
plt.plot(x9, y9, 'ko')
plt.plot(x10, y10, 'ko')

ax.set(xlabel='$α_{r}$ [°]', ylabel='$α_{e}$ [°]')
ax.grid()

ax = plt.gca()
ax.set_xlim([5, 21])
ax.set_ylim([10, 30])

plt.plot(x, y, "-r", label="regresijski pravac")
plt.plot(x1, y1, "ko", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj1_srednja.png")

plt.show()