import numpy as np
import time
R_MIN = 3.56999
R_MAX = 4
X_MIN = 0
X_MAX = 1

def normalizer(x):
    return np.arccos(1-2*x)/np.pi
def GetTimeSeed():
    '''
    Returns number between 0 and 1 thats basically epoch time.
    '''
    return time.time_ns()/100 % 1000 / 1000
def run(r, x, length):
    for _ in range(10):
        x = r * x * (1 - x)
    return x
def linear_scale_r(val):
    return R_MIN + (R_MAX - R_MIN) * val
def rnd(seed,num):
    num = run(seed,num*100*np.pi%1, int(100+1000 * seed % 13))
    seed = linear_scale_r(np.cos(num**2*np.pi*5)%1)
    return seed, num

def get_pnr(n):
    x = [GetTimeSeed()]
    seed = linear_scale_r(GetTimeSeed())
    for _ in range(n):
        seed,num = rnd(seed,x[-1])
        x.append(num)
    return np.array(x[1:])


