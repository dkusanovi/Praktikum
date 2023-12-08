from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# # Data for plotting
xl = np.arange(0, 100000, 100)
yl = 50.62916769*xl
y_teorija = 50*xl
# (phi, moment) mjerenja
x1, y1 = (250, 12816)
x2, y2 = (270, 13869)
x3, y3 = (290, 14941)
x4, y4 = (310, 15925)
x5, y5 = (230, 11544)
x6, y6 = (210, 10541)
x7, y7 = (190, 9021)
x8, y8 = (330, 17024)
x9, y9 = (350, 17856)
x99, y99 = (370, 18096)
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
axes[0].set_xlim([150, 400])
axes[0].set_ylim([8000, 20000])

axes[0].plot(xl, yl, "-r", label="regresijski pravac")
axes[0].plot(xl, y_teorija, "-g", label="teorijska vrijednost")
axes[0].plot(x1, y1, "bo", label="mjerenja")
axes[0].legend(loc='upper left')


# # Data for plotting
xd = np.arange(0, 100, 1)
# (phi, moment) mjerenja
x10, y10 = (72, 178)
x11, y11 = (69, 201)
x12, y12 = (67, 223)
x13, y13 = (65, 245)
x14, y14 = (74, 156)
x15, y15 = (83, 127)
x16, y16 = (93, 97)
x17, y17 = (64, 266)
x18, y18 = (62, 288)
x188, y188 = (58, 312)
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
axes[1].set_xlim([55, 80])
axes[1].set_ylim([100, 350])

axes[1].plot(x11, y11, "-b", label="mjerenja")
axes[1].legend(loc='upper right')

fig.savefig("vj2_k50.png")

plt.show()