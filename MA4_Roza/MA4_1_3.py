
"""
Solutions to module 4
Review date:
"""

student = "Rozalin Ghanim"
reviewer = ""

import math as m
import random as r
import numpy 
import matplotlib.pyplot as plt
import concurrent.futures as future
from time import sleep as pause
from time import perf_counter as pc


#Vectorizing with numpy goes much more faster
def sphere_volume(n, d, r=1): #nonparallised vol
    #r = 1
    dots = numpy.random.uniform(-r, r, (n, d))  # Generating all points at once
    indots = numpy.sum(numpy.sum(dots**2, axis=1) <= r**2)  # Vectorized check for all points
    return (indots/n)*((2*r)**d)
'''
#For loop makes it really slow
def sphere_volume(n, d): #nonparallised vol
    indots = 0 
    r = 1
    dots = [[numpy.random.uniform(-r,r) for _ in range(d)] for _ in range(n)] #generates d random coor 
    #Dot inside the hypersphere with the given equation: x1^2 + x2^2 + ... + xd^2 <= r^2
    for dot in dots:
        if sum(map(lambda x: x**2, dot)) <= r**2: #for each point it checks if it is inside with equation
            indots += 1
        
    return (indots/n)*((2*r)**d) #returns the hypersphere volume throigh the proportion of points * volume of cube
'''
def hypersphere_exact(n,d, r=1): #hypersphere_exact that calculates the exact volume according to the eq from the task
    real_vol = (m.pi**(d/2))/m.gamma(d/2 +1)*(r**d)
    return real_vol


# parallel code - parallelize the volume and runs iterations of the regular sphere function in parallel with ProcessPoolExecutor
def sphere_volume_parallel1(n,d,np): #The number of parallel processes
    with future.ThreadPoolExecutor(max_workers=10) as ex:
        res = list(ex.map(sphere_volume, [n for x in range(np)], [d for x in range(np)])) # for each process n*np, d*np #maps the sphere_colume function into a list, not iterable otherwise
    average = sum(res)/len(res) #each results are collected and the average is taken
    return average


# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    each_proc = n // np #by splitting dots into the number of process, the load of work gers minimzed
    with future.ThreadPoolExecutor(max_workers=10) as ex:
        res = list(ex.map(sphere_volume, [each_proc]*np, [d]*np)) 
    
    average = sum(res)/len(res) #each results are collected and the average is taken
    return average 

def main():
    
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11

    t1_start = pc()

    # FIRST NORMAL Sphere_volume
    for y in range (10):
        volume = sphere_volume(n,d)

    t1_end = pc()
    print(f" First volume of hypersphere is {volume} ")
    print(f"calculations took {t1_end-t1_start:.4f} seconds")


    t2_start = pc()
    n = 1000000
    d = 11
    np = 4
    #SECOND sphere_volume_parallel1

    second_volume = sphere_volume_parallel1(n, d, np)
    t2_end = pc()
    print(f" Second volume of hypersphere is {second_volume} units ")
    print(f"Calculations took {t2_end-t2_start:.4f} seconds")

    t3_start = pc()
    n = 1000000
    d = 11
    np = 4

    #Third sphere_volume_parallel1

    third_volume = sphere_volume_parallel1(n, d, np)
    t3_end = pc()
    print(f" Third volume of hypersphere is {third_volume} units ")
    print(f"calculations took {t3_end-t3_start:.4f} seconds")

    verification = hypersphere_exact(n, d)
    print(f'Actual volume of the hypersphere:{verification} units')


if __name__ == '__main__':
	main()
