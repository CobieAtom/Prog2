import matplotlib.pyplot as plt
import numpy as np

"""
Solutions to module 4
Review date:
"""

student = "Rozalin Ghanim"
reviewer = ""


def approximate_pi(n):

    side = 1  # Längden av kvdarat
    r = side/2  # Radie av cirkel, in the square
    inx = []  # x-koor inuti cirkeln 
    iny = []  # y-koor inuti cirkeln
    outx = []  # x-koor utanför cirkeln
    outy = []  # y-koor utanför cirkeln

    # Genererar olika slumpmässiga punkter i kvaradten
    x = np.random.rand(n) * side
    y = np.random.rand(n) * side

    # avstånd mellan varje punkt från origo
    dist = np.sqrt((x-0.5)**2 + (y-0.5)**2)

    # punkter inut ska vara lika eller mindre än cirkels radie
    inx = x[dist <= r]
    iny = y[dist <= r]

    # punkter utanför ska vara större än radien
    outx = x[dist > r]
    outy = y[dist > r]

    # uppskatta pi som förhållandet av antalet punkter i cirkel till total antal punkter 
    approx_pi_ = 4 * len(inx) / n

    # plotta pinkterna
    plt.figure(figsize=(8, 8))
    plt.scatter(inx, iny, color='dodgerblue', s=5)
    plt.scatter(outx, outy, color='purple', s=5)

    # Plotta cirkeln och kvadrat
    circle = plt.Circle((-1, 1), r/2, color='gray', fill=False, linewidth=2)
    plt.gca().add_artist(circle)
    
    plt.xlim(0, side)
    plt.ylim(0, side)
    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.title(f'MC Simulation for Estimating π with {n} points', fontsize = 17)
    plt.xlabel('x')
    plt.ylabel('y')
    #plt.legend()
    plt.grid(True)
    #plt.show()

    return approx_pi_

def main():
    lst = [1000, 10000, 100000]
    nlst = []
    for n in lst:
        Value_of_pi = approximate_pi(n)
        nlst.append(Value_of_pi)
        print(f"Estimated π with {n} points: {Value_of_pi}")
    return sorted(nlst)
if __name__ == '__main__':
    main()

