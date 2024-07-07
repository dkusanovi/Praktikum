from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(300, 360, 1)
y = 4.6734E-08*x + 0

x1, y1 = (308.15, 1.43812E-05)
x2, y2 = (313.15, 1.45854E-05)
x3, y3 = (318.15, 1.47895E-05)
x4, y4 = (323.15, 1.50957E-05)
#x5, y5 = (328.15, 1.56061E-05)
x6, y6 = (333.15, 1.56061E-05)
x7, y7 = (338.15, 1.58102E-05)
x8, y8 = (343.15, 1.60143E-05)
x9, y9 = (348.15, 1.62185E-05)
x10, y10 = (353.15, 1.64226E-05)


fig, ax = plt.subplots()
ax.plot(x, y, color='k')
plt.plot(x1, y1, 'ro')
plt.plot(x2, y2, 'ro')
plt.plot(x3, y3, 'ro')
plt.plot(x4, y4, 'ro')
#plt.plot(x5, y5, 'ro')
plt.plot(x6, y6, 'ro')
plt.plot(x7, y7, 'ro')
plt.plot(x8, y8, 'ro')
plt.plot(x9, y9, 'ro')
plt.plot(x10, y10, 'ro')


ax.set(xlabel='$T$ [K]', ylabel='$V$ [m$^3$]')
ax.grid()

ax = plt.gca()
# ax.set_xlim([0.5, 1.1])
# ax.set_ylim([1, 2.4])

plt.plot(x, y, "-k", label="regresijski pravac")
plt.plot(x1, y1, "ro", label="mjerenja")
plt.legend(loc="upper left")
plt.title('ovisnost $V-T$')

fig.savefig("vj1_VT.png")

plt.show()