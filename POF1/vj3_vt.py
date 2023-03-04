from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# graf je previse precizan jer je koristena samo jedna vrijednost akcelereacije
# treba izvuc t iz formule

# (t, v) mjerenja
x1, y1 = (1.05, 0.116781)
x2, y2 = (1.206667, 0.134206)
x3, y3 = (1.4, 0.155708)
x4, y4 = (1.696667, 0.188703)
x5, y5 = (1.79, 0.199084)
x6, y6 = (2.093333, 0.23282)
x7, y7 = (2.203333, 0.245055)
x8, y8 = (2.326667, 0.258772)
x9, y9 = (2.336667, 0.259884)
x10, y10 = (2.533333, 0.281757)


fig, ax = plt.subplots()
# ax.plot(x, y, color='red')
plt.plot(x1, y1, 'bo', color="green")
plt.plot(x2, y2, 'bo', color="green")
plt.plot(x3, y3, 'bo', color="green")
plt.plot(x4, y4, 'bo', color="green")
plt.plot(x5, y5, 'bo', color="green")
plt.plot(x6, y6, 'bo', color="green")
plt.plot(x7, y7, 'bo', color="green")
plt.plot(x8, y8, 'bo', color="green")
plt.plot(x9, y9, 'bo', color="green")
plt.plot(x10, y10, 'bo', color="green")


ax.set(xlabel='$t$ [s]', ylabel='$v$ [m/s]')
ax.grid()

ax = plt.gca()
ax.set_xlim([1, 2.6])
ax.set_ylim([0.1, 0.3])


plt.plot(x1, y1, "-b", label="mjerenja", color="green")
plt.legend(loc="upper left")

fig.savefig("vj3_vt.png")

plt.show()