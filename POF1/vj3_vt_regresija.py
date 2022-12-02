from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 10, 0.01)
y = 0.09656*x

# (t, v) mjerenja
x1, y1 = (1.05, 0.101388)
x2, y2 = (1.206667, 0.116516)
x3, y3 = (1.4, 0.135184)
x4, y4 = (1.696667, 0.16383)
x5, y5 = (1.79, 0.172842)
x6, y6 = (2.093333, 0.202132)
x7, y7 = (2.203333, 0.212754)
x8, y8 = (2.326667, 0.224663)
x9, y9 = (2.336667, 0.225629)
x10, y10 = (2.533333, 0.244619)


fig, ax = plt.subplots()
ax.plot(x, y, color='red')
plt.plot(x1, y1, 'bo', color="green")
plt.plot(x2, y2, 'bo', color="green")
plt.plot(x3, y3, 'bo', color="green")
plt.plot(x4, y4, 'bo', color="green")
plt.plot(x5, y5, 'bo', color="green")
plt.plot(x6, y6, 'bo', color="green")
plt.plot(x7, y7, 'bo', color="green")
plt.plot(x8, y8, 'bo', color="green")
plt.plot(x9, y9, 'bo', color="green")
plt.plot(x10, y10, 'bo', color="green")


ax.set(xlabel='$t$ [s]', ylabel='$v$ [m/s]')
ax.grid()

ax = plt.gca()
ax.set_xlim([1, 2.6])
ax.set_ylim([0.1, 0.25])


plt.plot(x, y, "-r", label="$s(v)$")
plt.plot(x1, y1, "-b", label="mjerenja", color="green")
plt.legend(loc="upper left")

fig.savefig("vj3_vt_regresija.png")

plt.show()