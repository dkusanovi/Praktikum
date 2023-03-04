from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# # Data for plotting
# x = np.arange(0, 2, 0.01)
# y = 1.88265*x - 1.25485

# (t, energija) mjerenja
x1, y1 = (1.05, 0.312596667)
x2, y2 = (1.206667, 0.412838904)
x3, y3 = (1.4, 0.555727408)
x4, y4 = (1.696667, 0.816204474)
x5, y5 = (1.79, 0.908472545)
x6, y6 = (2.093333, 1.242459912)
x7, y7 = (2.203333, 1.376467696)
x8, y8 = (2.326667, 1.534879216)
x9, y9 = (2.336667, 1.548101372)
x10, y10 = (2.53333, 1.819660241)


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


ax.set(xlabel='$t$ [s]', ylabel='$E_{rot}$ [J]')
#        title='About as simple as it gets, folks')
ax.grid()

ax = plt.gca()
ax.set_xlim([1, 2.6])
ax.set_ylim([0, 1.9])

# plt.plot(x, y, "-r", label="log$s$(log$t$)")
plt.plot(x1, y1, "-b", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj3_rotacijska.png")

plt.show()