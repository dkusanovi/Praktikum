# from turtle import color
# import matplotlib.pyplot as plt
# import numpy as np
# import math

# # Data for plotting
# x = np.arange(-90, 90, 0.01)

# y = 0.8036*x -4.389

# # (log\omega, logU) mjerenja
# x1, y1 = (3.800346, -1.37675071)
# x2, y2 = (4.09921, -1.086186148)
# x3, y3 = (4.275301123, -0.924453039)
# x4, y4 = (4.400022658, -0.821023053)
# x5, y5 = (4.49697612, -0.749579998)
# x6, y6 = (4.576548212, -0.701146924)
# x7, y7 = (4.643339946, -0.661543506)
# x8, y8 = (4.701161268, -0.628932138)
# x9, y9 = (4.752567119, -0.603800653)
# x10, y10 = (4.79904759, -0.54515514)


# fig, ax = plt.subplots()
# ax.plot(x, y, color='#A52A2A')
# plt.plot(x1, y1, 'bo')
# plt.plot(x2, y2, 'bo')
# plt.plot(x3, y3, 'bo')
# plt.plot(x4, y4, 'bo')
# plt.plot(x5, y5, 'bo')
# plt.plot(x6, y6, 'bo')
# plt.plot(x7, y7, 'bo')
# plt.plot(x8, y8, 'bo')
# plt.plot(x9, y9, 'bo')
# plt.plot(x10, y10, 'bo')

# ax.set(xlabel='log$\omega$', ylabel='log$U_{eff}$')
# ax.grid()

# ax = plt.gca()
# ax.set_xlim([3.6, 5])
# ax.set_ylim([-1.4, -0.5])

# plt.plot(x, y, "-r", label="regresijski pravac")
# plt.plot(x1, y1, "bo", label="mjerenja")
# plt.legend(loc="upper left")

# fig.savefig("vj8_zdk2_log.png")

# plt.show()

from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(-90, 90, 0.01)

# y = 0.8036*x -4.389

# (omega, U) mjerenja
x1, y1 = (6314.601, 0.042)
x2, y2 = (12566.37061, 0.082)
x3, y3 = (18849.55592, 0.119)
x4, y4 = (25120.17486, 0.151)
x5, y5 = (31403.36017, 0.178)
x6, y6 = (37717.9614, 0.199)
x7, y7 = (43988.58034, 0.218)
x8, y8 = (50252.91609, 0.235)
x9, y9 = (56567.51732, 0.249)
x10, y10 = (62957.51678, 0.285)


fig, ax = plt.subplots()
# ax.plot(x, y, color='#A52A2A')
plt.plot(x1, y1, 'bo')
plt.plot(x2, y2, 'bo')
plt.plot(x3, y3, 'bo')
plt.plot(x4, y4, 'bo')
plt.plot(x5, y5, 'bo')
plt.plot(x6, y6, 'bo')
plt.plot(x7, y7, 'bo')
plt.plot(x8, y8, 'bo')
plt.plot(x9, y9, 'bo')
plt.plot(x10, y10, 'bo')

ax.set(xlabel='$\omega$ [rad/s]', ylabel='$U_{eff}$ [V]')
ax.grid()

ax = plt.gca()
ax.set_xlim([5000, 65000])
ax.set_ylim([0, 0.3])

# plt.plot(x, y, "-r", label="regresijski pravac")
plt.plot(x1, y1, "bo", label="mjerenja")
plt.legend(loc="upper left")

fig.savefig("vj8_zdk2.png")

plt.show()