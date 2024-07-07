from turtle import color
import matplotlib.pyplot as plt
import numpy as np


# Data for plotting
x = np.arange(50, 330, 1)
# y = 0.001196196*x + 1.665965489


x1, y1 = (321.9774472, 2.02)
x2, y2 = (266.598388, 1.98)
x3, y3 = (224.4019666, 1.95)
x4, y4 = (191.5088903, 1.92)
x5, y5 = (165.3694063, 1.88)
x6, y6 = (144.2515353, 1.86)
x7, y7 = (126.9452683, 1.83)
x8, y8 = (112.5844973, 1.81)
x9, y9 = (100.5360111, 1.79)
x10, y10 = (90.32816153, 1.75)
x11, y11 = (81.60378507, 1.72)


fig, ax = plt.subplots()
#ax.plot(x, y, color='k')
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
plt.plot(x11, y11, 'go')


ax.set(xlabel='$J$ [W/m$^2$]', ylabel='$U$ [V]')
ax.grid()

ax = plt.gca()
# ax.set_xlim([0.5, 1.1])
# ax.set_ylim([1, 2.4])

# plt.plot(x, y, "-k", label="regresijski pravac")
plt.plot(x1, y1, "go", label="mjerenja")
plt.legend(loc="upper left")
plt.title('$J$ - $U$')

fig.savefig("vj6_J_U.png")

plt.show()