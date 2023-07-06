from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math


# Data for plotting
x = np.arange(3000, 6000, 0.01)

y = 7*(np.sqrt(((204)**2+(x-1/(x*5*10**(-8)))**2)/((x-1/(x*5*10**(-8)))**2+(100+204)**2)))


# (omega, U_TO) mjerenja
x3, y3 = (3769.911184, 6.85)
x4, y4 = (4084.07045, 6.69)
x5, y5 = (4398.229715, 5.5)
x6, y6 = (4461.061568, 4.91)
x7, y7 = (4467.344753, 4.85)
x8, y8 = (4473.627939, 4.79)
x9, y9 = (4479.911124, 4.75)
x10, y10 = (4486.194309, 4.71)
x11, y11 = (4492.477495, 4.71)
x12, y12 = (4498.76068, 4.69)
x13, y13 = (4505.043865, 4.67)
x14, y14 = (4511.327051, 4.69)
x15, y15 = (4517.610236, 4.71)
x16, y16 = (4523.893421, 4.71)
x17, y17 = (4712.38898, 6.19)
x18, y18 = (5026.548246, 6.73)


fig, ax = plt.subplots()
ax.plot(x, y, color='#A52A2A')
plt.plot(x3, y3, 'bo')
plt.plot(x4, y4, 'bo')
plt.plot(x5, y5, 'bo')
plt.plot(x6, y6, 'bo')
plt.plot(x7, y7, 'bo')
plt.plot(x8, y8, 'bo')
plt.plot(x9, y9, 'bo')
plt.plot(x10, y10, 'bo')
plt.plot(x11, y11, 'bo')
plt.plot(x12, y12, 'bo')
plt.plot(x13, y13, 'bo')
plt.plot(x14, y14, 'bo')
plt.plot(x15, y15, 'bo')
plt.plot(x16, y16, 'bo')
plt.plot(x17, y17, 'bo')
plt.plot(x18, y18, 'bo')

ax.set(xlabel='$\omega$ [s$^{-1}$]', ylabel='$U_{QO}$ [V]')
ax.grid()

ax = plt.gca()
ax.set_xlim([3500, 5500])
ax.set_ylim([4.5, 7])

plt.plot(x, y, "-k", label="teorijska krivulja, jednadžba (14)")
plt.plot(x11, y11, "bo", label="mjerenja")
plt.legend(loc="lower left")

fig.savefig("vj5_drugi.png")

plt.show()