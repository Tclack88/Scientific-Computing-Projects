#!/usr/bin/env python3

# created to visualize a logistic map for a problem in non-linear dynamics. Very Pretty
# strogatz problem 6

import numpy as np
from matplotlib.pyplot import *

def logmap(r,x):
	xn = r*(1-x**2)*x
	return xn


rlist = np.linspace(0,3,400)
xdata = []
rdata = []

# Must run the logistic map many times (about 300) to allow the values
# to settle to its eventual behavior. (that's the reason for the 1st 'for loop'
# Then, it gets run again and that behavior is plotted

for r in rlist:
	for i in range(300):
		x = .7
		x = logmap(r,x)
	
	
	for i in range(300):
		x = logmap(r,x)
		rdata.append(r)
		xdata.append(x)


fig,ax = subplots()
plot(rdata,xdata,'k.',marker=',',markersize=.3)
title('Logistic cubic map for r = .7')
fig.show()

input("<enter>")
