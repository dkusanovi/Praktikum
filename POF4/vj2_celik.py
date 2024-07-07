from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 17, 1)
y = 1.22E-05*1000*x + 0

x1, y1 = (0, 0)
x2, y2 = (3, 0.00004*1000)
x3, y3 = (6, 0.00007*1000)
x4, y4 = (9, 0.00011*1000)
x5, y5 = (12, 0.000145*1000)
x6, y6 = (15, 0.000185*1000)



fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, color='g')
plt.plot(x1, y1, 'mo')
plt.plot(x2, y2, 'mo')
plt.plot(x3, y3, 'mo')
plt.plot(x4, y4, 'mo')
plt.plot(x5, y5, 'mo')
plt.plot(x6, y6, 'mo')



ax.set(ylabel='$\Delta l$ [mm]', xlabel='$l_0$$\Delta T$ [mK]')
ax.grid()

ax = plt.gca()
# ax.set_xlim([0.5, 1.1])
# ax.set_ylim([1, 2.4])

plt.plot(x, y, "-g", label="regresijski pravac")
plt.plot(x1, y1, "mo", label="mjerenja")
plt.legend(loc="upper left")
plt.title('čelik')

fig.savefig("vj2_celik.png")

plt.show()