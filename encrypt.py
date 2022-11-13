import numpy as np

import lprandom as lp
from PIL import Image
import matplotlib.pyplot as plt
plt.style.use('dark_background')

fig, (ax1,ax2,ax3,ax4) = plt.subplots(1, 4, figsize=(16, 7))


im1 = Image.open(r"images/yae.PNG").convert('L')
(w,h) = im1.size
rng,seed = lp.lprandom_int_0_256(w*h)
rng2,seed = lp.lprandom_int_0_256(w*h,seed+.00001)

im1p = im1.load()
t = 0

ax1.imshow(im1,cmap="gray")
ax1.set_title("Original Image")

for i in range(w):
    for j in range(h):
        #im1.putpixel((i, j), im1.getpixel((i,j))^rng(t))
        im1.putpixel((i, j),int(im1.getpixel((i,j)))^int(rng[t]))
        t+=1
t = 0

ax2.imshow(im1,cmap="gray")
ax2.set_title("Encrypted Image")
##DE-ENCRYPT  WITH SAME KEY

for i in range(w):
    for j in range(h):
        #im1.putpixel((i, j), im1.getpixel((i,j))^rng(t))
        im1.putpixel((i, j),int(im1.getpixel((i,j)))^int(rng[t]))
        t+=1

ax3.imshow(im1,cmap="gray")
ax3.set_title("De-crypted Image")
t = 0

##ENCRYPT AGAIN WITH SAME KEY
for i in range(w):
    for j in range(h):
        #im1.putpixel((i, j), im1.getpixel((i,j))^rng(t))
        im1.putpixel((i, j),int(im1.getpixel((i,j)))^int(rng[t]))
        t+=1
t = 0

##DE-ENCRYPT AGAIN WITH DIFFERENT KEY

for i in range(w):
    for j in range(h):
        #im1.putpixel((i, j), im1.getpixel((i,j))^rng(t))
        im1.putpixel((i, j),int(im1.getpixel((i,j)))^int(rng2[t]))
        t+=1

ax4.imshow(im1,cmap="gray")
ax4.set_title("De-cryption Failed (Wrong key)")

plt.show()