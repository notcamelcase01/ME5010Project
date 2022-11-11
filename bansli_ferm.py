import lprandom as lprng
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')

n = 10000
fig, axx = plt.subplots(1, 1, figsize=(9, 9))
sampl, seed = lprng.lprandom_real_un(10000)

def plot(points,ax):
    """
    Plots the points using matplotlib.
    Points is a list of (x, y) pairs.
    """

    xx = [x for (x, y) in points]
    yy = [y for (x, y) in points]

    ax.plot(xx, yy, 'g.',markersize=.1)

def getnint(n,n0):
    return int(n*1000)%n0

def sierpinski(n,xar,ax):


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


