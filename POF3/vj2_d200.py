from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# # Data for plotting
xl = np.arange(-50, 10000, 100)
yl = -192.307*xl 
y_teorija = -200*xl
# (phi, moment) mjerenja
x1, y1 = (159, -33480) 
x2, y2 = (189,-41470) 
x3, y3 = (52, -15200) 
x4, y4 = (91, -13680)
x5, y5 = (153, -21870)
x6, y6 = (94, -13920)
x7, y7 = (-14, -8600)
x8, y8 = (52, -10560)
x9, y9 = (91, -19100) 
x99, y99 = (186, -36720)
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
axes[0].set_xlim([-20, 210])
axes[0].set_ylim([-42000, -1900])

axes[0].plot(xl, yl, "-r", label="regresijski pravac")
axes[0].plot(xl, y_teorija, "-g", label="teorijska vrijednost")
axes[0].plot(x1, y1, "bo", label="mjerenja")
axes[0].legend(loc='lower left')


# # Data for plotting
xd = np.arange(0, 100, 1)
# (phi, moment) mjerenja
x10, y10 = (120, 279)
x11, y11 = (130, 319)
x12, y12 = (100, 152)
x13, y13 = (80, 171)
x14, y14 = (90, 243)
x15, y15 = (80, 174)
x16, y16 = (100, 86)
x17, y17 = (80, 132)
x18, y18 = (100, 191)
x188, y188 = (120, 306)
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


axes[1].set(xlabel='|$a$| [mm]', ylabel='$b$ [mm]')
axes[1].grid()
axes[1].set_title('Povećanje')

# ax = plt.gca()
# axes[1].set_xlim([55, 80])
# axes[1].set_ylim([100, 350])

axes[1].plot(x11, y11, "-b", label="mjerenja")
axes[1].legend(loc='upper left')

fig.savefig("vj2_d200.png")

plt.show()