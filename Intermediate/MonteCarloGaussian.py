#!/usr/bin/env python3

# PURPOSE: Approximate area of a Gaussian using MonteCarlo method. Compute error
# NOTE: Should compare this to RiemanSum.py

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
			

x = np.linspace(-X,X,100)
y = func(x)
								

N= 10000
xpoints = uniform(-X,X,N)
ypoints = uniform(0,Y,N)

				# x,y are for plotting the exponential function
				# xpoints,ypoints are the random scatterplot points

count = 0
subcount = []
subtotal = []
for i in range(1,N):
	if ypoints[i] <= func(xpoints[i]):
		count += 1
	if count % 10 == 0:
		subcount.append(count)
		subtotal.append(i)
subcount = np.asarray(subcount)
subtotal = np.asarray(subtotal)

				# for each set in xpoints,ypoints, if that y value is less than
				# or equal to the func, then it contributes to the area and is
				# counted. Every 10 I append the total points evaluated to the
				# "subtotal" list and the counts to the "subcount" list, which
				# I turn into an array to determine the area approximation at
				# each of these 10 additional counts


print("\nArea of distribution ~",count*SquareArea/N,'\n')

				# Area is ratio of points under curve (count) to total points
				# generated (N) times the total area (SquareArea)

fig1,ax1 = subplots()
ax1.plot(xpoints,ypoints,linestyle='none',marker=',')
ax1.plot(x,y,color='k')
xlabel("Smells (Note this isn't a required plot)")
ylabel('Mikayla')
title('Integration using Monte Carlo simulation')
fig1.show()

				# Extra Plot for sake of visualization


AreaApprox = subcount*SquareArea/subtotal
AreaError = 100*abs((AreaApprox - np.sqrt(np.pi))/np.sqrt(np.pi))

				# Math on array to make new array of the area calculation
				# at every 10 points plotted, then determining percent error

fig2,ax2 = subplots()
ax2.plot(subtotal,AreaError)
xlabel('Number of Points Sampled')
ylabel('Percent difference from True value(%)')
title('Fractional Error as a Function of Number of Points (Monte Carlo)')
fig2.show()



input("Press <enter> to exit (plots will NOT automatically save)")




