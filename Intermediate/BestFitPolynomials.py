#!/usr/bin/env python3

# PURPOSE: Generate a random number of points (user input) and plot several best fit
# polynomial lines

from numpy import *
from numpy.random import uniform
from matplotlib.pyplot import *


N = input("How many points do you want to make? (Range: 4 < N < 16): ")

while N.isdigit() == False or int(N) >= 16 or int(N) <= 4 :
	N = input("Please enter a valid input, an integer (3 < N < 16): ")

N = int(N) 	

				# This while loop is used to check against malicious input
				# I've found that digits above 15 that polyfit doesn't work 
				# perfectly (though it still does some decent approximations)
				# and input should be above 3 becuase the N-3 polynomial term
				# disappears


x = uniform(0,100,N)
y = uniform(0,100,N)

				#  sudo randomly generated points

p1 = polyfit(x,y,1)
p2 = polyfit(x,y,N-3)
p3 = polyfit(x,y,N-1)

				# polyfit is a numpy function whose output is an array of 
				# polynomial coefficients (size specified by last arguement)
	


xp = linspace(0,100,100)
figure, ax = subplots()
ax.plot(x,y,color='blue',marker='o',linestyle='None')
ax.plot(xp,polyval(p1,xp),'r-')
ax.plot(xp,polyval(p2,xp),'g-')
ax.plot(xp,polyval(p3,xp),'m:')

				# polyval is a numpy function and plot is a matplotlib.pyplot
				#  function (since I imported *, this isn't immediately obvious)
				# polyval takes two inputs: p,x with p being an array of
				#  polynomial coefficients and x being an array of x points
				#  to evaluate them at
				# xp is a new set of x points, 100 in this case. So when we
				#  evaluate the polynomial at 100 points, the polynomial looks
				#  much smoother than the crude 4 < N < 16 points from the input


ylim([0,100])
title("Various Polynomial Curve Fits to Randomly Generated Points")
xlabel("Random X coordinate (unitless)")
ylabel("Random Y coordinate (unitless)")
figure.show()
				# ylim() and show() are matplotlib.pyplot functions
				# plot() automatically scales the points, making it very
				#  difficult to see, so I restrict this here
				# give a title and display

input("\nShowing Plot (Plot not saved automatically) press <enter> to exit ")
