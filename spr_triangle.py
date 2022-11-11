import lprandom as lprng
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')

n = 10000
fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(16, 9))
xrng, seed = lprng.lprandom_real(n)
sampl = np.random.uniform(low=0., high=1, size=(n,))
def plot(points,ax):
    """
    Plots the points using matplotlib.
    Points is a list of (x, y) pairs.
    """

    xx = [x for (x, y) in points]
    yy = [y for (x, y) in points]

    ax.plot(xx, yy, 'w.')



def get123(n):
    return int(n*1000)%3

def sierpinski(n,xar,ax):
    """
    Generates positions for the Chaos Game Sierpinski
    triangle with 'n' iterations in a square of size 1x1.
    """

    vertices = [(0.0, 0.0), (0.5, 1.0), (1.0, 0.0)]
    points = []

    # initial vertex
    x, y = vertices[2]

    for i in range(n):

        # select new vertex
        vx, vy = vertices[get123(xar[i])]


        # get middle point
        x = (vx + x) / 2.0
        y = (vy + y) / 2.0


        points.append((x, y))


    plot(points,ax)


sierpinski(n,xrng,ax1)
sierpinski(n,sampl,ax2)
ax1.set_title("LOGISTIC")
ax2.set_title("NUMPY RAND")
ax1.set_aspect('equal', adjustable='box')
ax2.set_aspect('equal', adjustable='box')

plt.show()