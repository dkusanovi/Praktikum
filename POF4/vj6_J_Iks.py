from turtle import color
import matplotlib.pyplot as plt
import numpy as np


# Data for plotting
x = np.arange(50, 330, 1)
y = 0.000239941*x + 0.011067415


x1, y1 = (321.9774472, 0.0862)
x2, y2 = (266.598388, 0.0751)
x3, y3 = (224.4019666, 0.0661)
x4, y4 = (191.5088903, 0.0585)
x5, y5 = (165.3694063, 0.052)
x6, y6 = (144.2515353, 0.0467)
x7, y7 = (126.9452683, 0.042)
x8, y8 = (112.5844973, 0.038)
x9, y9 = (100.5360111, 0.0345)
x10, y10 = (90.32816153, 0.0317)
x11, y11 = (81.60378507, 0.0291)


fig, ax = plt.subplots()
ax.plot(x, y, color='k')
plt.plot(x1, y1, 'ro')
plt.plot(x2, y2, 'ro')
plt.plot(x3, y3, 'ro')
plt.plot(x4, y4, 'ro')
plt.plot(x5, y5, 'ro')
plt.plot(x6, y6, 'ro')
plt.plot(x7, y7, 'ro')
plt.plot(x8, y8, 'ro')
plt.plot(x9, y9, 'ro')
plt.plot(x10, y10, 'ro')
plt.plot(x11, y11, 'ro')


ax.set(xlabel='$J$ [W/m$^2$]', ylabel='$I_{ks}$ [A]')
ax.grid()

ax = plt.gca()
# ax.set_xlim([0.5, 1.1])
# ax.set_ylim([1, 2.4])

plt.plot(x, y, "-m", label="regresijski pravac")
plt.plot(x1, y1, "ro", label="mjerenja")
plt.legend(loc="upper left")
plt.title('$J$ - $I_{ks}$')

fig.savefig("vj6_J_Iks.png")

plt.show()