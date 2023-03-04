from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math


# (t, energija) mjerenja
x1, y1 = (1.05, -0.28364)
x2, y2 = (1.206667, -0.43835)
x3, y3 = (1.4, -0.59307)
x4, y4 = (1.696667, -0.74778)
x5, y5 = (1.79, -0.9025)
x6, y6 = (2.093333, -1.05721)
x7, y7 = (2.203333, -1.21192)
x8, y8 = (2.326667, -1.36664)
x9, y9 = (2.336667, -1.52135)
x10, y10 = (2.53333, -1.67606)


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


ax.set(xlabel='$t$ [s]', ylabel='$E_{pot}$ [J]')
ax.grid()

ax = plt.gca()
ax.set_xlim([1, 2.6])
ax.set_ylim([-2, 0])

# potrebne tockice umjesto crte u legendi za mjerenja
plt.plot(x1, y1, "-b", label="mjerenja")
plt.legend(loc="upper right")

fig.savefig("vj3_potencijalna.png")

plt.show()