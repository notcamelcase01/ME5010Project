import lprandom as lprng
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')

n = 100000
n2 = 10000
n3 = 1000
n4 = 100
fig, axx = plt.subplots(2, 2, figsize=(9, 9))
sampl = np.random.uniform(low=0., high=1, size=(n,))
xrng, seed = lprng.lprandom_real_un(n)
def plot(points,ax):


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


sierpinski(n,xrng,axx[1,1])
sierpinski(n2,xrng,axx[1,0])
sierpinski(n3,xrng,axx[0,1])
sierpinski(n4,xrng,axx[0,0])

axx[1,1].set_title("100000 points")
axx[1,0].set_title("10000 points")
axx[0,1].set_title("1000 points")
axx[0,0].set_title("100 points")

axx[0,0].set_aspect('equal', adjustable='box')
axx[0,1].set_aspect('equal', adjustable='box')
axx[1,0].set_aspect('equal', adjustable='box')
axx[1,1].set_aspect('equal', adjustable='box')

plt.show()