from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# (temperatura, gustoca) mjerenja
x1, y1 = (25, 0.994)
x2, y2 = (29, 0.997)
x3, y3 = (35, 1)
x4, y4 = (39, 0.994)
x5, y5 = (45, 0.99)
x6, y6 = (50, 0.985)
x7, y7 = (53, 0.986)
x8, y8 = (59, 0.983)
x9, y9 = (63, 0.98)
x10, y10 = (70, 0.977)
x11, y11 = (74, 0.974)


fig, ax = plt.subplots()
plt.plot(x1, y1, 'bo', color="#7E1E9C")
plt.plot(x2, y2, 'bo', color="#7E1E9C")
plt.plot(x3, y3, 'bo', color="#7E1E9C")
plt.plot(x4, y4, 'bo', color="#7E1E9C")
plt.plot(x5, y5, 'bo', color="#7E1E9C")
plt.plot(x6, y6, 'bo', color="#7E1E9C")
plt.plot(x7, y7, 'bo', color="#7E1E9C")
plt.plot(x8, y8, 'bo', color="#7E1E9C")
plt.plot(x9, y9, 'bo', color="#7E1E9C")
plt.plot(x10, y10, 'bo', color="#7E1E9C")
plt.plot(x11, y11, 'bo', color="#7E1E9C")

ax.set(xlabel='temperatura [$^\circ$C]', ylabel='$ρ$ [g/cm$^3$]')
#        title='About as simple as it gets, folks')
ax.grid()

ax = plt.gca()
ax.set_xlim([20, 80])
ax.set_ylim([0.97, 1.005])

plt.plot(x1, y1, "#7E1E9C", label="mjerenja")
plt.legend(loc="upper right")

fig.savefig("vj1_gustoca.png")

plt.show()