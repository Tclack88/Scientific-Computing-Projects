#!/usr/bin/env python3

# PURPOSE: Determine and plot error in calculating pi using MonteCarloMethod

from numpy.random import uniform
from numpy import sqrt
from matplotlib.pyplot import *




N = 100000

						# largish number of my choosing input is not specified
x = uniform(0,2,N)
y = uniform(0,2,N)

						# Much of the rest of this follows from the previous
						# problem where the code was described, what differs
						# here is I created two lists, 'subcount' and 'subtotal'
count = 0

subcount = []
subtotal = []

for i in range(1,N):
	x_dist = x[i]-1
	y_dist = y[i]-1
	dist = sqrt(x_dist**2 + y_dist**2)
	if dist <= 1:
		count += 1
	if i % 10 == 0:
		subcount.append(count)
		subtotal.append(i)

						# Much of this code logic was described in part a. 
						# What differs here is every 10 samples, the count and 
						# total samples are appended to a list

subcount = np.asarray(subcount)
subtotal = np.asarray(subtotal)

pi_approx = 4*subcount/subtotal
pi_err = abs(100*(pi_approx-np.pi)/np.pi)
print("\nThe first few and last few errors:\n\n",pi_err)					
						# Turn the aforementioned lists into arrays for speed
						# of calculations. For each of those elements, find
						# pi (the approximation) and compare that to the actual
						# value. Place these errors into an array to be plotted

fig,ax = subplots()
title('Error Calculating Pi with Monte Carlo with Varying Sample Size' )
xlabel('Number of samples')
ylabel('Percent Error(%)')
ax.plot(subtotal,pi_err)
fig.show()
	
						# Notice the plot with BEAUTIFUL titles and axes labels



input("\nShowing plot (figure will not automatically be saved)\n" \
		"              press <enter> to exit")
