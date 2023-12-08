from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# # Data for plotting
xl = np.arange(0, 70000, 10)
yl = 103.7837377*xl
y_teorija = 100*xl
# (phi, moment) mjerenja
x1, y1 = (430, 44625)
x2, y2 = (450, 46656)
x3, y3 = (470, 48984)
x4, y4 = (490, 50421)
x5, y5 = (510, 52925)
x6, y6 = (530, 54600)
x7, y7 = (550, 57129)
x8, y8 = (570, 59024)
x9, y9 = (590, 61425)
x99, y99 = (610, 63784)
axes[0].plot(xl, yl, color='red')
axes[0].plot(x1, y1, 'bo')
axes[0].plot(x2, y2, 'bo')
axes[0].plot(x3, y3, 'bo')
axes[0].plot(x4, y4, 'bo')
axes[0].plot(x5, y5, 'bo')
axes[0].plot(x6, y6, 'bo')
axes[0].plot(x7, y7, 'bo')
axes[0].plot(x8, y8, 'bo')
axes[0].plot(x9, y9, 'bo')
axes[0].plot(x99, y99, 'bo')


axes[0].set(xlabel='$a+b$ [mm]', ylabel='$ab$ [mm$^2$]')
axes[0].grid()
axes[0].set_title('Žarišna udaljenost')

# ax = plt.gca()
axes[0].set_xlim([400, 650])
axes[0].set_ylim([40000, 70000])

axes[0].plot(xl, yl, "-r", label="regresijski pravac")
axes[0].plot(xl, y_teorija, "-g", label="teorijska vrijednost")
axes[0].plot(x1, y1, "bo", label="mjerenja")
axes[0].legend(loc='upper left')


# # Data for plotting
xd = np.arange(0, 500, 2)
# (phi, moment) mjerenja
x10, y10 = (175, 255)
x11, y11 = (162, 288)
x12, y12 = (156, 314)
x13, y13 = (147, 343)
x14, y14 = (145, 365)
x15, y15 = (140, 390)
x16, y16 = (139, 411)
x17, y17 = (136, 434)
x18, y18 = (135, 455)
x188, y188 = (134, 476)
axes[1].plot(x10, y10, 'bo')
axes[1].plot(x11, y11, 'bo')
axes[1].plot(x12, y12, 'bo')
axes[1].plot(x13, y13, 'bo')
axes[1].plot(x14, y14, 'bo')
axes[1].plot(x15, y15, 'bo')
axes[1].plot(x16, y16, 'bo')
axes[1].plot(x17, y17, 'bo')
axes[1].plot(x18, y18, 'bo')
axes[1].plot(x188, y188, 'bo')


axes[1].set(xlabel='$a$ [mm]', ylabel='$b$ [mm]')
axes[1].grid()
axes[1].set_title('Povećanje')

# ax = plt.gca()
axes[1].set_xlim([100, 200])
axes[1].set_ylim([200, 500])

axes[1].plot(x11, y11, "-b", label="mjerenja")
axes[1].legend(loc='upper left')

fig.savefig("vj2_k100.png")

plt.show()