import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,TextBox
from numba import jit

plt.style.use('dark_background')


def logistic(r, x):
    return r * x * (1 - x)

@jit(nopython=True)
def getf(N0,x0,r0):
    for i in range(N0-1):
        x0[i+1] = r0*x0[i]*(1-x0[i])
    return x0


n = 10000
r = np.linspace(2.5, 4.0, n)
iterations = 1000
last = 100
x = .9 * np.ones(n)
fig, (ax2,ax1) = plt.subplots(1, 2, figsize=(13, 6))

for i in range(iterations):
    x = logistic(r, x)
    if i >= (iterations - last):
        ax1.plot(r, x, ',w',alpha = .25)
ax1.set_xlim(2.5, 4)
ax1.set_title("Bifurcation diagram")
ax1.set_xlabel('r')
ax1.set_ylabel('Equilibrium x')
ax2.set_title(r'$x_n$ at Equilibrium')
ax2.set_ylim(0,1)
ax2.set_xlabel('n')
ax2.set_ylabel("$x_n$")
r0 = 3.0002
N0 = 50
t0 = np.arange(0,N0,1)
init_pop = 0.25


line, = ax2.plot(t0, getf(N0,init_pop*np.ones(N0),r0),'-o')
fig.subplots_adjust(left=0.2,bottom=0.2)
axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
axini = fig.add_axes([0.05, 0.25, 0.0225, 0.63])
graphBox = fig.add_axes([0.1, 0.05, 0.8, 0.075])

amp_slider = Slider(
    ax=axamp,
    label="r",
    valmin=0,
    valmax=4,
    valinit=r0,
    orientation="vertical"
)

ini_slider = Slider(
    ax=axini,
    label="init_pop",
    valmin=0,
    valmax=.99999,
    valinit=init_pop,
    orientation="vertical"
)

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def visslider(k):
    k = str(k)
    if isfloat(k):
        k = float(k)
        if k < 0 or k > 3.999:
            return
        amp_slider.set_val(float(k))


txtBox = TextBox(graphBox,'R',color="black", hovercolor='black')
txtBox.on_submit(visslider)


def update(val):
    line.set_ydata(getf(N0,ini_slider.val*np.ones(N0),amp_slider.val))
    fig.canvas.draw_idle()
amp_slider.on_changed(update)
ini_slider.on_changed(update)
plt.show()