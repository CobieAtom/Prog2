"""
Solutions to module 4
Review date:
"""

student = "Rozalin Ghanim"
reviewer = ""

import math as m
import random as r
import numpy as np
#import functools 
from time import perf_counter as pc


def sphere_volume(n, d):
    indots = 0
    r = 1
    dots = [[np.random.uniform(-r,r) for _ in range(d)] for _ in range(n)]
    #Dot inside the hypersphere with the given equation: x1^2 + x2^2 + ... + xd^2 <= r^2
    for dot in dots:
        if sum(map(lambda x: x**2, dot)) <= r**2: #equation
            indots += 1
        
    return (indots/n)*((2*r)**d)

def hypersphere_exact(n,d, r=1): #hypersphere_exact that calculates the exact volume according to the eq from the task
    real_vol = (m.pi**(d/2))/m.gamma(d/2 +1)*(r**d)
    return real_vol
     
def main():
    n = 100000
    #d = 2
    d = 11
    t_start = pc()
    Est_v = sphere_volume(n, d)
    Exa_v= hypersphere_exact(n, d, r=1)
    print(f'Approximated volume for {d}-dimensional hypersphere: {Est_v}')
    print(f'Exact volume for {d}-dimensional hypersphere: {Exa_v}')
    t_end = pc()
    print(f'Amount of time it took for the calculations is: {t_end-t_start} seconds')


if __name__ == '__main__':
	main()
