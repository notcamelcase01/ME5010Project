import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')


def logistic(r, x):
    return r * x * (1 - x)




fig2, ax1 = plt.subplots(2, 2, figsize=(16, 6))


N0 = 50
t0 = np.arange(0,N0,1)
init_pop = 0.01

x = init_pop*np.ones(len(t0))
r = 2
for i in range(len(t0)-1):
    x[i+1] = logistic(r,x[i])
ax1[0,0].plot(t0,x,'-o',label= "Period 1 at r = {r} < 3".format(r=r))
r = 3.1
for i in range(len(t0)-1):
    x[i+1] = logistic(r,x[i])
ax1[0,1].plot(t0,x,'-o',label= "Period 2 at $r_1$ = {r}".format(r=r))
r = 3.49
for i in range(len(t0)-1):
    x[i+1] = logistic(r,x[i])
ax1[1,0].plot(t0,x,'-o',label= "Period 4 at $r_2$ = {r}".format(r=r))
r = 3.560
for i in range(len(t0)-1):
    x[i+1] = logistic(r,x[i])
ax1[1,1].plot(t0,x,'-o',label= "Period 8 at $r_3$ = {r}".format(r=r))
fig2.suptitle("Demonstration of period doubling, Showing $r_0$ , $r_1$ , $r_2$ , $r_3$")
ax1[0,0].legend()
ax1[1,0].legend()
ax1[0,1].legend()
ax1[1,1].legend()

plt.show()