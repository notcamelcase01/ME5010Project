'''
DESIGN BY CONTRACT EXPECTATION
This is done to make program faster by reducing "if checks"
because I am expecting the user to act according to the following contract
|||| SEED CANNOT BE 0 OR 1 and should be between 0 and 1 ||||
'''
import numpy as np
import time
from numba import jit

R_MAX = 4
R_MIN = 3.9
X_MIN = 0
X_MAX = 1
FORBIDDEN_NUMBER = np.array([.25,.5,.75])#WILL BRING PERIODICITY
def GetTimeSeed():
    '''
    Returns number between 0 and 1 thats basically epoch time.
    '''
    return time.time_ns()/100 % 1000 / 1000


def ScaleR(val,rmin = R_MIN,rmax = R_MAX):
    '''
    DESIGN BY CONTRACT
    Only works for value in [0,1]
    Not putting any condition or conversion cuz it will slow down the code
    '''
    return rmin + val*(rmax - rmin)

def ScaleX(val,xmin = X_MIN,xmax = X_MAX):
    '''
    DESIGN BY CONTRACT
    Only works for value in [0,1]
    Not putting any condition or conversion cuz it will slow down the code
    '''
    return xmin + val*(xmax - xmin)


def logistic(r, x):
    return r * x * (1 - x)

def normalizer(x):
    return np.arccos(1-2*x)/np.pi


@jit(nopython=True)
def run(n, initial, r):
    x = [r * initial * (1 - initial)]
    for _ in range(n+1000):
        x.append(r * x[-1] * (1 - x[-1]))
    return np.array(x[1001:])

def lprandom_real(n,seed = None):
    run(1,.2,4) #warming up njit
    if seed is None:
        seed =  ScaleX(GetTimeSeed())
    if seed in FORBIDDEN_NUMBER:
        seed = seed + 0.001
    return normalizer(run(n,seed,3.99)),seed

def lprandom_real_un(n,seed = None):
    run(1,.2,4) #warming up njit
    if seed is None:
        seed =  ScaleX(GetTimeSeed())
    if seed in FORBIDDEN_NUMBER:
        seed = seed + 0.001
    return run(n,seed,3.99),seed




