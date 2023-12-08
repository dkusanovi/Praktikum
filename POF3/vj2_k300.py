from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# # Data for plotting
xl = np.arange(0, 100000, 100)
yl = 305.9321*xl
y_teorija = 300*xl
# (phi, moment) mjerenja
x1, y1 = (1310, 400464)
x2, y2 = (1300, 396579)
x3, y3 = (1290, 395000)
x4, y4 = (1280, 391644)
x5, y5 = (1270, 388584)
x6, y6 = (1260, 385451)
x7, y7 = (1250, 381789)
x8, y8 = (1240, 382284)
x9, y9 = (1230, 377696)
x99, y99 = (1220, 370579)
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


axes[0].set(xlabel='$a+b$ [mm]', ylabel='$ab$ [mm$^2$]')
axes[0].grid()
axes[0].set_title('Žarišna udaljenost')

# ax = plt.gca()
axes[0].set_xlim([1200, 1340])
axes[0].set_ylim([360000, 410000])

axes[0].plot(xl, yl, "-r", label="regresijski pravac")
axes[0].plot(xl, y_teorija, "-g", label="teorijska vrijednost")
axes[0].plot(x1, y1, "bo", label="mjerenja")
axes[0].legend(loc='upper left')


# # Data for plotting
xd = np.arange(0, 100, 1)
# (phi, moment) mjerenja
x10, y10 = (486, 824)
x11, y11 = (489, 811)
x12, y12 = (500, 790)
x13, y13 = (506, 774)
x14, y14 = (514, 756)
x15, y15 = (523, 737)
x16, y16 = (531, 719)
x17, y17 = (574, 666)
x18, y18 = (592, 638)
x188, y188 = (649, 571)
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
axes[1].set_xlim([400, 700])
axes[1].set_ylim([550, 850])

axes[1].plot(x11, y11, "-b", label="mjerenja")
axes[1].legend(loc='upper right')

fig.savefig("vj2_k300.png")

plt.show()