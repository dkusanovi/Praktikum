# from turtle import color
# import matplotlib.pyplot as plt
# import numpy as np
# import math  

# # Data for plotting
# x = np.arange(-90, 90, 0.01)

# y = 1.058*x -3.265

# # (logN, logU) mjerenja
# x1, y1 = (2.477121255, -0.643974143)
# x2, y2 = (2.301029996, -0.829738285)
# x3, y3 = (2, -1.148741651)


# fig, ax = plt.subplots()
# ax.plot(x, y, color='#A52A2A')
# plt.plot(x1, y1, 'ro')
# plt.plot(x2, y2, 'ro')
# plt.plot(x3, y3, 'ro')


# ax.set(xlabel='log$N$', ylabel='log$U_{eff}$')
# ax.grid()

# ax = plt.gca()
# ax.set_xlim([1.8, 2.7])
# ax.set_ylim([-1.2, -0.6])

# plt.plot(x, y, "-b", label="regresijski pravac")
# plt.plot(x2, y2, "ro", label="mjerenja")
# plt.legend(loc="upper left")

# fig.savefig("vj8_zdk3_log.png")

# plt.show()


from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(-90, 90, 0.01)

# y = 1.058*x -3.265

# (N, U) mjerenja
x1, y1 = (100, 0.071)
x2, y2 = (200, 0.148)
x3, y3 = (300, 0.227)


fig, ax = plt.subplots()
# ax.plot(x, y, color='#A52A2A')
plt.plot(x1, y1, 'ro')
plt.plot(x2, y2, 'ro')
plt.plot(x3, y3, 'ro')


ax.set(xlabel='$N$', ylabel='$U_{eff}$ [V]')
ax.grid()

ax = plt.gca()
ax.set_xlim([50, 350])
ax.set_ylim([0, 0.3])

# plt.plot(x, y, "-b", label="regresijski pravac")
plt.plot(x2, y2, "ro", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj8_zdk3.png")

plt.show()