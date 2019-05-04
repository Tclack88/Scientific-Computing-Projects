#!/usr/bin/env python3

# PURPOSE: Area of a circle approximation using Monte Carlo method, and approximate pi with this

from numpy.random import uniform
from numpy import sqrt
from matplotlib.pyplot import *



N = input("We shall approximate the area of a circle of radius 1\n" \
			"Give me a number of points (the larger the more accurate): ")

while N.isdigit() == False:
	N = input("Please enter a valid input (integer): ")

N = int(N)

					# error check for valid input

x = uniform(0,2,N)
y = uniform(0,2,N)

					# uniform (a numpy function) generates a set of	points
					# (size N here) over the specified range (0-2 in this case)

count = 0

for i in range(N):
	x_dist = x[i]-1
	y_dist = y[i]-1
	dist = sqrt(x_dist**2 + y_dist**2)
	if dist <= 1:
		count += 1

					# Distance formula very simple. If it turns out that the
					# point lies within the circle (i.e. net distance from its
					# center at (1,1), is less than 1, it gets added to the 
					# total count


fig, ax = subplots()
circle = Circle((1,1),radius=1,fill=False,lw=1)
ax.plot(x,y,color="b",linestyle="none",marker=',')
ax.add_artist(circle)
ax.set_aspect(1)
title("Mikayla Smells")
fig.show()

					# I decided to plot this for visualization purposes
					# Circle() is a matplotlib.pyplot function. It was very
					# convenient and self working to import
					# to avoid getting a "squashed circle" I had to set the							# aspect ratio to 1

print("The area of this circle is approximately:",str(4*count/N),"pi radians\n")

print("Since the are of a circle is pi*R^2 and R =1," \
		" pi is approximately:\n             ",str(4*count/N))

					# the ratio of points in the circle to total points
					# is the same as the ratio of the area of the circle to
					# the total area (4)

input("\nShowing plot (figure will not automatically be saved)\n" \
		"              press <enter> to exit")
