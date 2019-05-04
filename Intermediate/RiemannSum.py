#!/usr/bin/env python3

# PURPOSE: Approximate the area under a gaussian using Riemann sums, plot error
# as a function of number of rectangles used

import numpy as np
from numpy.random import uniform
from matplotlib.pyplot import *

def func(x):
	return np.exp(-x**2)

X = 5
Y = 1
SquareArea = 2*X*Y


				# Define the exponential function, X = the max x window
				# Y = max y range, SquareArea = area of plot region displayed
			
N = 15

				# Choose number of rectangles 
				# (Error drastically decreases, so too many rectangles then
				# the plot looks like a capital "L" )

SubArea = []
count = []
for i in range(2,N):
	count.append(i)
	dx = 2*X/i
	x = np.arange(-X,X,dx)
	y = func(x)
	Area = np.sum(y)*dx
	SubArea.append(Area)

				# Choose to divide the function into 2,3,...N rectangles
				# For each, define a dx interval and make an array (x) which 
				# ranges from -X to X with dx set as the rectangle width
				# make an array (y) that gives the height of these rectangles
				# multiply by dx to get the total rectangle area
				# each time append it to a "SubArea" list to find intermediate
				# values of the area

print("\nArea of distribution ~",SubArea[-1])

				# the last element of the "SubArea" list contains the most
				# rectangles and thus gives the best approximatino of area

count = np.asarray(count)
SubArea = np.asarray(SubArea)

				# turn "Count" and "SubArea" lists into arrays for plotting
				# "Count" (as number of rectangles) will be plotted as x values

PercentError = 100*abs((SubArea - np.sqrt(np.pi))/np.sqrt(np.pi))

				# Make array "PercentError" to be plotted as y values
 
f2,ax2 = subplots()
ax2.plot(count,PercentError)
xlabel('Number of Rectangles')
ylabel('Percent Error (%)')
title('Error in Calculating Area as a function of Number of Rectangles' \
			'\n(Riemann Sum)')
f2.show()

input("\nPress <enter> to exit. Plot NOT automatically saved")

