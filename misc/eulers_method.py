#!/usr/bin/env python3

from numpy import exp

# Use Euler's methd, stepsize h = .1 t find apprximate values at:
# t = .1, .2, .3, .4, .5
# y' + 2y = 2 - e^-4t   y(0) = 1

######  Specific to the problem
init_cond = (0,1) # Inital conditions, tuple

def y_prime(ty):
    return 2 - exp(-4*ty[0]) - 2 * ty[1]
######  ^^^^^^^^^^^^^^^^^^^^^^^



# General method:

def eulers_method(init_cond, h = .1, num_steps = 4):
    ty_pairs = [init_cond]  # initialize a list of (t,y) tuples
                            # beginning with initial condition
    for step in range(num_steps):
        t, y = ty_pairs[-1][0], ty_pairs[-1][1]
        next_t = t + h
        y_change = y_prime(ty_pairs[-1])
        next_y = y + y_change * h
        ty_pairs.append((next_t, next_y))
    
    return ty_pairs

ty_pairs = eulers_method(init_cond)

print(ty_pairs)
 
