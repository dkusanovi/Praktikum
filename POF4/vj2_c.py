from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 26, 1)
# y = 1.22E-05*x + 0

x1, y1 = (0, 0)
x2, y2 = (5, 0.00004*1000)
x3, y3 = (10, 0.00007*1000)
x4, y4 = (15, 0.00011*1000)
x5, y5 = (20, 0.000145*1000)
x6, y6 = (25, 0.000185*1000)



fig, ax = plt.subplots(figsize=(8, 5))
# ax.plot(x, y, color='g')
plt.plot(x1, y1, 'mo')
plt.plot(x2, y2, 'mo')
plt.plot(x3, y3, 'mo')
plt.plot(x4, y4, 'mo')
plt.plot(x5, y5, 'mo')
plt.plot(x6, y6, 'mo')



ax.set(ylabel='$\Delta l$ [mm]', xlabel='$\Delta T$ [K]')
ax.grid()

ax = plt.gca()
# ax.set_xlim([0.5, 1.1])
# ax.set_ylim([1, 2.4])

# plt.plot(x, y, "-g", label="regresijski pravac")
plt.plot(x1, y1, "mo", label="mjerenja")
plt.legend(loc="upper left")
plt.title('čelik')

fig.savefig("vj2_celik2.png")

plt.show()