from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math


# (t, energija) mjerenja
x1, y1 = (1.05, 0.003584696)
x2, y2 = (1.206667, 0.004734222)
x3, y3 = (1.4, 0.006372793)
x4, y4 = (1.696667, 0.009359809)
x5, y5 = (1.79, 0.010417891)
x6, y6 = (2.093333, 0.014247885)
x7, y7 = (2.203333, 0.015784617)
x8, y8 = (2.326667, 0.017601198)
x9, y9 = (2.336667, 0.017752823)
x10, y10 = (2.53333, 0.020866919)


fig, ax = plt.subplots()
# ax.plot(x, y, color='red')
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


ax.set(xlabel='$t$ [s]', ylabel='$E_{kin}$ [J]')
ax.grid()

ax = plt.gca()
ax.set_xlim([1, 2.6])
ax.set_ylim([0, 0.022])


# umjesto crte u legendi bi trebala bit tocka za mjerenja

plt.plot(x1, y1, "-b", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj3_kineticka.png")

plt.show()