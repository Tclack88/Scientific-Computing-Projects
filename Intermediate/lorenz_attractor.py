#!/usr/bin/env python3

# plot of a lorentz attractor as apart of a solution to a nonlinear dynamics problem
# strogatz

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def lorenz(x,y,z,r, a=10, b=8/3):
	x_dot = a*(y-x)
	y_dot = r*x-y-x*z
	z_dot = x*y-b*z
	return x_dot, y_dot, z_dot

# Setup step size, number of iterations, and initial values.  Make 3 separate 
# lists for the x,y and z values. First entry is the initial values
# NOTE: with a stepsize of .01, there needs to be 5000 steps to get to t = 50

dt = 0.01
N = 5000
r = 24.5
xvals=[0]
yvals=[10]
zvals=[13] 

# By derivative definition: x(t) = x(t-1) + x_dot * dt
# Use for loop to append to lists 
for i in range(1,N):
	x_dot, y_dot, z_dot = lorenz(xvals[i-1], yvals[i-1], zvals[i-1], r)
	xvals.append(xvals[i-1] + x_dot * dt)
	yvals.append(yvals[i-1] + y_dot * dt)
	zvals.append(zvals[i-1] + z_dot * dt)

# Convert lists into arrays for ease of plotting
xvals = np.asarray(xvals)
yvals = np.asarray(yvals)
zvals = np.asarray(zvals)


fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xvals, yvals, zvals, linewidth=0.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Lorenz Equations Strogatz 9.3.4 for r = 24.5")

plt.show()
