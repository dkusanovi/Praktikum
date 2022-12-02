from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
x = np.arange(0, 10, 0.01)
y = 0.04828*x

# (t^2, s) mjerenja
x1, y1 = (1.05**2, 0.055)
x2, y2 = (1.206667**2, 0.085)
x3, y3 = (1.4**2, 0.115)
x4, y4 = (1.696667**2, 0.145)
x5, y5 = (1.79**2, 0.175)
x6, y6 = (2.093333**2, 0.205)
x7, y7 = (2.203333**2, 0.235)
x8, y8 = (2.326667**2, 0.265)
x9, y9 = (2.336667**2, 0.295)
x10, y10 = (2.53333**2, 0.325)


fig, ax = plt.subplots()
ax.plot(x, y, color='red')
plt.plot(x1, y1, 'bo', color="purple")
plt.plot(x2, y2, 'bo', color="purple")
plt.plot(x3, y3, 'bo', color="purple")
plt.plot(x4, y4, 'bo', color="purple")
plt.plot(x5, y5, 'bo', color="purple")
plt.plot(x6, y6, 'bo', color="purple")
plt.plot(x7, y7, 'bo', color="purple")
plt.plot(x8, y8, 'bo', color="purple")
plt.plot(x9, y9, 'bo', color="purple")
plt.plot(x10, y10, 'bo', color="purple")


ax.set(xlabel='$t^2$ [s$^2$]', ylabel='$s$ [m]')
#        title='About as simple as it gets, folks')
ax.grid()

ax = plt.gca()
ax.set_xlim([1, 7])
ax.set_ylim([0.05, 0.35])


plt.plot(x, y, "-r", label="$s(t^2)$")
plt.plot(x1, y1, "-b", label="mjerenja", color="purple")
plt.legend(loc="upper left")

fig.savefig("vj3_st2_regresija.png")

plt.show()