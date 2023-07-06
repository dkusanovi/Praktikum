# from turtle import color
# import matplotlib.pyplot as plt
# import numpy as np
# import math

# # Data for plotting
# x = np.arange(-90, 90, 0.01)

# y = 2.066*x + 2.244

# # (logd, logU) mjerenja
# x1, y1 = (-1.397940009, -0.643974143)
# x2, y2 = (-1.494850022, -0.841637508)
# x3, y3 = (-1.602059991, -1.065501549)


# fig, ax = plt.subplots()
# ax.plot(x, y, color='#A52A2A')
# plt.plot(x1, y1, 'ro')
# plt.plot(x2, y2, 'ro')
# plt.plot(x3, y3, 'ro')


# ax.set(xlabel='log$d$', ylabel='log$U_{eff}$')
# ax.grid()

# ax = plt.gca()
# ax.set_xlim([-1.8, -1.2])
# ax.set_ylim([-1.2, -0.4])

# plt.plot(x, y, "-k", label="regresijski pravac")
# plt.plot(x2, y2, "ro", label="mjerenja")
# plt.legend(loc="upper left")

# fig.savefig("vj8_zdk4_log.png")

# plt.show()


from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(-90, 90, 0.01)

# y = 2.066*x + 2.244

# (d, U) mjerenja
x1, y1 = (25, 0.086)
x2, y2 = (32, 0.144)
x3, y3 = (40, 0.227)


fig, ax = plt.subplots()
# ax.plot(x, y, color='#A52A2A')
plt.plot(x1, y1, 'ko')
plt.plot(x2, y2, 'ko')
plt.plot(x3, y3, 'ko')


ax.set(xlabel='$d$ [mm]', ylabel='$U_{eff}$ [V]')
ax.grid()

ax = plt.gca()
ax.set_xlim([20, 45])
ax.set_ylim([0, 0.3])

# plt.plot(x, y, "-k", label="regresijski pravac")
plt.plot(x2, y2, "ko", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj8_zdk4.png")

plt.show()