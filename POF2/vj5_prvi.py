from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math


# Data for plotting
x = np.arange(3000, 6000, 0.01)

y = (50*5.82)/(np.sqrt((x-(1/(x*5*10**(-8))))**2+(50+204)**2))


# (omega, U_TO) mjerenja
x1, y1 = (3141.592654, 0.1384)
x2, y2 = (3455.751919, 0.1832)
x3, y3 = (3769.911184, 0.2426)
x4, y4 = (4084.07045, 0.401)
x5, y5 = (4398.229715, 0.9454)
x6, y6 = (4461.061568, 1.1)
x7, y7 = (4467.344753, 1.11)
x8, y8 = (4473.627939, 1.11)
x9, y9 = (4479.911124, 1.13)
x10, y10 = (4486.194309, 1.13)
x11, y11 = (4492.477495, 1.13)
x12, y12 = (4498.76068, 1.13)
x13, y13 = (4505.043865, 1.14)
x14, y14 = (4511.327051, 1.13)
x15, y15 = (4517.610236, 1.13)
x16, y16 = (4523.893421, 1.12)
x17, y17 = (4712.38898, 0.688)
x18, y18 = (5026.548246, 0.3663)
x19, y19 = (5340.707511, 0.2475)
x20, y20 = (5654.866776, 0.1931)


fig, ax = plt.subplots()
ax.plot(x, y, color='#A52A2A')
plt.plot(x1, y1, 'co')
plt.plot(x2, y2, 'co')
plt.plot(x3, y3, 'co')
plt.plot(x4, y4, 'co')
plt.plot(x5, y5, 'co')
plt.plot(x6, y6, 'co')
plt.plot(x7, y7, 'co')
plt.plot(x8, y8, 'co')
plt.plot(x9, y9, 'co')
plt.plot(x10, y10, 'co')
plt.plot(x11, y11, 'co')
plt.plot(x12, y12, 'co')
plt.plot(x13, y13, 'co')
plt.plot(x14, y14, 'co')
plt.plot(x15, y15, 'co')
plt.plot(x16, y16, 'co')
plt.plot(x17, y17, 'co')
plt.plot(x18, y18, 'co')
plt.plot(x19, y19, 'co')
plt.plot(x20, y20, 'co')

ax.set(xlabel='$\omega$ [s$^{-1}$]', ylabel='$U_{TO}$ [V]')
ax.grid()

ax = plt.gca()
ax.set_xlim([3000, 6000])
ax.set_ylim([0, 1.2])

plt.plot(x, y, "-y", label="$U_{TO} = (R_RU_0)/\sqrt{(\omega L - 1/(\omega C))^2+(R_R+R_L)^2} $")
plt.plot(x1, y1, "co", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj5_prvi.png")

plt.show()