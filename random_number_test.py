import random
import numpy as np
import lprandom as lprng
import matplotlib.pyplot as plt
import pseudo_random_gen as pnr

plt.style.use('dark_background')


N0 = 10000
xlpr= pnr.get_pnr(N0)
sampl = np.random.uniform(low=0., high=1, size=(N0,))
print(len(sampl))
print(len(xlpr))

fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(16, 9))
ax1.hist(xlpr,100)
ax2.hist(sampl,100)
ax1.set_title("LOGISTIC HISTOGRAM")
ax2.set_title("NUMPY HISTOGRAM")

plt.show()

'''UNCOMMENT THIS FOR SCATTER CHART FOR RANDOM NUMBERS
n0 = 1000
fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(16, 9))
x=[]
y=[]
for i in range(n0):
    x.append(random.uniform(0,1))
    y.append(random.uniform(0,1))

ax1.scatter(x,y)
x,seed = lprng.lprandom_real(2*n0)
y = x[n0:]
x = x[:n0]
ax2.scatter(x,y)

ax1.set_title("PYTHON'S RANDOM SCATTER")
ax2.set_title("LOGISTIC MAP RANDOM SCATTER FOR SEED = {seed}".format(seed = seed))
plt.show()
'''
