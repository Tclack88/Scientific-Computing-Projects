#!/usr/bin/python3

# PURPOSE: make a basic 3d plot (function specified below)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def z(x,y):
	z = np.cos(x)*np.sin(y)
	return z
		
							# defines the function given in the problem and
							# assigns that to the single variable 'z'

x = np.linspace(-2.5*np.pi,2.5*np.pi,100)
y = np.linspace(-2.5*np.pi,2.5*np.pi,100)

							# Set an equal range across the origin for the
							# x and y axes. Total is 2.5 radians in 100 
							# divisions

x,y = np.meshgrid(x,y)

							# establishes the grid base for the plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

							# Create a figure object. 
							# 111 refers to a 1x1x1 grid

ax.plot_surface(x,y,z(x,y), cmap = 'binary')

							# Here the actual plotting command along with 
							# a very boring color mapping choice

ax.set_xlabel('x(radians)')
ax.set_ylabel('y(radians)')
ax.set_zlabel('z')
plt.title("Mikayla Smells")

plt.show()

							# display the plot of course
