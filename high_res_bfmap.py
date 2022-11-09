import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

def logistic(r, x):
    return r * x * (1 - x)

n = 1000000
r = np.linspace(2.5, 4.0, n)

iterations = 1000
last = 100

x = .1 * np.ones(n)
fig, ax1 = plt.subplots(1, 1, figsize=(16,9))
for i in range(iterations):
    x = logistic(r, x)
    if i >= (iterations - last):
        ax1.plot(r, x, ',w', alpha=.25)
ax1.set_xlim(2.5, 4)
ax1.set_title("Bifurcation diagram")
ax1.set_xlabel("r")
ax1.set_ylabel("x")
plt.show()