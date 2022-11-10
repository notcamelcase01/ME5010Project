import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')


def logistic(r, x):
    return r * x * (1 - x)




fig2, ax1 = plt.subplots(2, 2, figsize=(16, 6))


N0 = 50
t0 = np.arange(0,N0,1)


r = 4
init_pop = 1
x = init_pop*np.ones(len(t0))
for i in range(len(t0)-1):
    x[i+1] = logistic(r,x[i])
ax1[0,0].plot(t0,x,'-o',label= "x = {r}".format(r=init_pop))
init_pop = .5
x = init_pop*np.ones(len(t0))
for i in range(len(t0)-1):
    x[i+1] = logistic(r,x[i])
ax1[0,1].plot(t0,x,'-o',label= "x = {r}".format(r=init_pop))
init_pop = .75
x = init_pop*np.ones(len(t0))
for i in range(len(t0)-1):
    x[i+1] = logistic(r,x[i])
ax1[1,0].plot(t0,x,'-o',label= "x = {r}".format(r=init_pop))
init_pop = .251
x = init_pop*np.ones(len(t0))
for i in range(len(t0)-1):
    x[i+1] = logistic(r,x[i])
ax1[1,1].plot(t0,x,'-o',label= "x = {r}".format(r=init_pop))
fig2.suptitle("At r = 4 map  being non-chaotic")
ax1[0,0].legend()
ax1[1,0].legend()
ax1[0,1].legend()
ax1[1,1].legend()

plt.show()