from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(300, 360, 1)
y = 333.5719708*10**(-2)*x + 0

x1, y1 = (308.15, 103802.4*10**(-2))
x2, y2 = (313.15, 104069*10**(-2))
x3, y3 = (318.15, 105801.9*10**(-2))
x4, y4 = (323.15, 107668.1*10**(-2))
x5, y5 = (328.15, 109401*10**(-2))
x6, y6 = (333.15, 110867.3*10**(-2))
x7, y7 = (338.15, 112067*10**(-2))
x8, y8 = (343.15, 114066.5*10**(-2))
x9, y9 = (348.15, 116465.9*10**(-2))
x10, y10 = (353.15, 118732*10**(-2))


fig, ax = plt.subplots()
ax.plot(x, y, color='m')
plt.plot(x1, y1, 'ko')
plt.plot(x2, y2, 'ko')
plt.plot(x3, y3, 'ko')
plt.plot(x4, y4, 'ko')
plt.plot(x5, y5, 'ko')
plt.plot(x6, y6, 'ko')
plt.plot(x7, y7, 'ko')
plt.plot(x8, y8, 'ko')
plt.plot(x9, y9, 'ko')
plt.plot(x10, y10, 'ko')


ax.set(xlabel='$T$ [K]', ylabel='$p$ [hPa]')
ax.grid()

ax = plt.gca()
# ax.set_xlim([0.5, 1.1])
# ax.set_ylim([1, 2.4])

plt.plot(x, y, "-m", label="regresijski pravac")
plt.plot(x1, y1, "ko", label="mjerenja")
plt.legend(loc="upper left")
plt.title('ovisnost $p-T$')

fig.savefig("vj1_pT.png")

plt.show()