import random
import lprandom as lprng
import matplotlib.pyplot as plt

plt.style.use('dark_background')

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

