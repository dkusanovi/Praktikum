from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 5, 0.1)
y = -2.264251275*x + 3.882823216

x1, y1 = (1.113943352, 1.322219295)
x2, y2 = (1.079181246, 1.431363764)
x3, y3 = (1.041392685, 1.531478917)
x4, y4 = (1, 1.633468456)
x5, y5 = (0.954242509, 1.740362689)
x6, y6 = (0.903089987, 1.851258349)
x7, y7 = (0.84509804, 1.982271233)
x8, y8 = (0.77815125, 2.133538908)
x9, y9 = (0.698970004, 2.28780173)
x10, y10 = (0.602059991, 2.499687083)


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

ax.set(xlabel='log$n$', ylabel='log$m$ [g]')
ax.grid()

ax = plt.gca()
ax.set_xlim([0.5, 1.2])
ax.set_ylim([1.2, 2.6])

plt.plot(x, y, "-k", label="regresijski pravac")
plt.plot(x1, y1, "ro", label="mjerenja")
plt.legend(loc="upper right")
plt.title('$L$ = 2 m')

fig.savefig("vj1_log2.png")

plt.show()