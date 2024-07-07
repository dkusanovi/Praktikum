from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 17, 1)
y = 2.21E-05*1000*x + 0

x1, y1 = (0, 0)
x2, y2 = (3, 0.00007*1000)
x3, y3 = (6, 0.00014*1000)
x4, y4 = (9, 0.0002*1000)
x5, y5 = (12, 0.00026*1000)
x6, y6 = (15, 0.00033*1000)



fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, color='k')
plt.plot(x1, y1, 'ro')
plt.plot(x2, y2, 'ro')
plt.plot(x3, y3, 'ro')
plt.plot(x4, y4, 'ro')
plt.plot(x5, y5, 'ro')
plt.plot(x6, y6, 'ro')


ax.set(ylabel='$\Delta l$ [mm]', xlabel='$l_0$$\Delta T$ [mK]')
ax.grid()

ax = plt.gca()
# ax.set_xlim([0.5, 1.1])
# ax.set_ylim([1, 2.4])

plt.plot(x, y, "-k", label="regresijski pravac")
plt.plot(x1, y1, "ro", label="mjerenja")
plt.legend(loc="upper left")
plt.title('aluminij')

fig.savefig("vj2_aluminij.png")

plt.show()