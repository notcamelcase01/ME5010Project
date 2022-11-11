import lprandom as lprng
import matplotlib.pyplot as plt
import numpy as np
import pseudo_random_gen as pnr
plt.style.use('dark_background')

n = 100000
fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(16, 9))
#sampl, seed = lprng.lprandom_real(n)
sampl = pnr.get_pnr(n)
xrng = np.random.uniform(low=0., high=1, size=(n,))



def plot(points,ax):
    """
    Plots the points using matplotlib.
    Points is a list of (x, y) pairs.
    """

    xx = [x for (x, y) in points]
    yy = [y for (x, y) in points]

    ax.plot(xx, yy, 'g.',markersize=1)




def sierpinski(n,xar,ax):

    points = []

    # initial vertex
    x,y = 0,0

    for i in range(n):

        r = xar[i]
        if r < 0.01:
            x, y = 0.00 * x + 0.00 * y, 0.00 * x + 0.16 * y + 0.00
        elif r < 0.86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.60
        elif r < 0.93:
            x, y = 0.20 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.60
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44


        points.append((x,y))


    plot(points,ax)


sierpinski(n,sampl,ax2)
sierpinski(n,xrng,ax1)

ax1.set_title("NumpyRand")
ax2.set_title("Logistic")



plt.show()