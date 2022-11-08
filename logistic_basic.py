import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')


def logistic(r, x):
    return r * x * (1 - x)





fig, ax2 = plt.subplots(1, 1, figsize=(7, 6))

xn = np.linspace(0,1,100)
xn4 = logistic(4,xn)

xn1 = logistic(1,xn)
xn_5 = logistic(.5,xn)

ax2.plot(xn,xn4,label="r = 4")
ax2.plot(xn,xn1,label="r = 1")
ax2.plot(xn,xn_5,label="r = .5")

ax2.set_title(r'$x_{n+1}$ vs $x_n$')
ax2.set_ylim(0, 1)
ax2.set_xlabel(r'$x_n$')
ax2.set_ylabel(r'$x_{n+1}$')

plt.legend()
plt.show()