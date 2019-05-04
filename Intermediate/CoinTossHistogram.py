#!/usr/bin/env python3

# PURPOSE: Simulate 1000 instances of 100 coin tosses. Plot as a histogram

import numpy as np
from numpy.random import uniform 
from matplotlib.pyplot import *


def HundToss():
	count = 0
	Round = uniform(0,1,100)
	for i in Round:
		if i >= .5:
			count += 1
	return count

		    # Simulate 100 coin tosses by generating an array with 100
		    # entries varying between 0-1. Arbitrarily decide heads is
		    # when entry is > .5  'count' is the total number of heads


HeadsPerRound = []

TotRounds = 1000

for j in range(TotRounds):
	a = HundToss()
	HeadsPerRound.append(a)

y = np.asarray(HeadsPerRound)

		    # look at 1000 instances of the 100 coin tosses. Append
		    # the number of occurences of heads to a list, turn that
		    # list into an arrat (for easy manipulation and graphing)


N = 100
p = .5
q = 1 - p
sigma = np.sqrt(N*p*q)
mu = N*p

def G(x):
	const = 1/(sigma*np.sqrt(2*np.pi))
	expnumer = -1*(x-mu)**2
	expdenom = 2*sigma**2
	G = const*np.exp(expnumer/expdenom)
	return G


		    # The above just sets up the Gaussian distribution for our
		    # scenario of flipping some number of coins 
		    # (given in the problem set, blindly applied it here)
	
x = np.linspace(0,N,10*N)

		    # establish x-data for plotting G(x), it of course should
		    # span N (the number of coin tosses per round, because we
		    # could have the unlikely scenario where all coins return
		    # heads, giving 100 as an output)


fig,ax = subplots()
ax.hist(y,bins=100)
ax.plot(x,TotRounds*G(x))
xlabel('Occurence of Heads in 100 coin flips')
ylabel('Number of Occurence')
fig.show()

		    # plot the histogram and Gaussian. I had 2 options here:
		    # 1. Normalizing the histogram (with normed=True)
		    # but this didn't give my desired y-axis (total occurences)
		    # 2.G is normalized already, so inflating it by multiplying
		    # by the number of rounds (1000). This is what I went with
		    # NOTE: I had to increase the bin size, might as well make 
		    # it match the number of coin flips. Otherwise, the bins in
		    # the center cluster and artificially enlarge, making it
		    # appear the peak of the mean is larger than it actually is


input("Showing Plot. Press <Enter> to stop (Plot will not automatically save)")

