# from turtle import color
# import matplotlib.pyplot as plt
# import numpy as np
# import math

# # Data for plotting
# x = np.arange(-90, 90, 0.01)

# y = 0.8755*x + 0.3884

# # (logI, logU) mjerenja
# x1, y1 = (-1.9914, -1.34679)
# x2, y2 = (-1.70333, -1.11351)
# x3, y3 = (-1.53313, -0.96658)
# x4, y4 = (-1.39903, -0.84164)
# x5, y5 = (-1.35853, -0.8041)
# x6, y6 = (-1.33442, -0.78252)
# x7, y7 = (-1.30016, -0.74958)
# x8, y8 = (-1.2652, -0.7167)
# x9, y9 = (-1.233589, -0.68613)
# x10, y10 = (-2.3279, -1.638272)


# fig, ax = plt.subplots()
# ax.plot(x, y, color='#A52A2A')
# plt.plot(x1, y1, 'go')
# plt.plot(x2, y2, 'go')
# plt.plot(x3, y3, 'go')
# plt.plot(x4, y4, 'go')
# plt.plot(x5, y5, 'go')
# plt.plot(x6, y6, 'go')
# plt.plot(x7, y7, 'go')
# plt.plot(x8, y8, 'go')
# plt.plot(x9, y9, 'go')
# plt.plot(x10, y10, 'go')

# ax.set(xlabel='log$I_{eff}$', ylabel='log$U_{eff}$')
# ax.grid()

# ax = plt.gca()
# ax.set_xlim([-2.4, -1])
# ax.set_ylim([-1.78, -0.4])

# plt.plot(x, y, "-r", label="regresijski pravac")
# plt.plot(x1, y1, "go", label="mjerenja")
# plt.legend(loc="upper left")

# fig.savefig("vj8_zdk1_log.png")

# plt.show()


from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(-90, 90, 0.01)

# y = 0.8755*x + 0.3884

# (I, U) mjerenja
x1, y1 = (10.2/1000, 0.045)
x2, y2 = (19.8/1000, 0.077)
x3, y3 = (29.3/1000, 0.108)
x4, y4 = (39.9/1000, 0.144)
x5, y5 = (43.8/1000, 0.157)
x6, y6 = (46.3/1000, 0.165)
x7, y7 = (50.1/1000, 0.178)
x8, y8 = (54.3/1000, 0.192)
x9, y9 = (58.4/1000, 0.206)
x10, y10 = (5.2/1000, 0.023)


fig, ax = plt.subplots()
# ax.plot(x, y, color='#A52A2A')
plt.plot(x1, y1, 'go')
plt.plot(x2, y2, 'go')
plt.plot(x3, y3, 'go')
plt.plot(x4, y4, 'go')
plt.plot(x5, y5, 'go')
plt.plot(x6, y6, 'go')
plt.plot(x7, y7, 'go')
plt.plot(x8, y8, 'go')
plt.plot(x9, y9, 'go')
plt.plot(x10, y10, 'go')

ax.set(xlabel='$I_{eff}$ [A]', ylabel='$U_{eff}$ [V]')
ax.grid()

ax = plt.gca()
ax.set_xlim([0, 70/1000])
ax.set_ylim([0, 0.25])

# plt.plot(x, y, "-r", label="regresijski pravac")
plt.plot(x1, y1, "go", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj8_zdk1.png")

plt.show()