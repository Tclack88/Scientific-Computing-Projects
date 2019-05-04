#!/usr/bin/env python3

# PURPOSE: Simulate photon collection and plot histogram. Overlay a poisson distibution

import numpy as np
from numpy.random import random
from matplotlib.pyplot import *
from scipy.special import factorial



N = 1000
p = .002


def Poisson(n):
	mu = N*p
	sigma = np.sqrt(mu)
	return (mu**n)*(np.exp(-mu))/factorial(n)

						# Poisson Distribution definition


def PhotCount(p):
	count = 0
	for i in random(1000):
		if i <= .002:
			count += 1
	return count

						# generate 1000 random number between 0 and 1
						# if a number < .002 (tantamount to the probability)
						# it gets appended to a list called "count"
counts = []
trials = []
for i in range(N):
	count =  PhotCount(p)
	counts.append(count)
	trials.append(i)


trials = np.asarray(trials)
counts = np.asarray(counts)

						# call that 1000 counts 1000 times, each time appending
						# the output (and trial number index) to lists
						# convert the lists to arrays for ease of graphing


x = np.linspace(0,np.max(counts)+2,100)

						# Establish many x values for the Poisson graph to
						# appear smooth				

width = 1
thebins = np.arange(counts.min(), counts.max() + width + 1, width) - 0.5

						# This correction undoes a problem inherent with the
						# hist() method. Namely, the bins lower edge is closed
						# and upper edge is open... except for the last bin 
						# which is closed at the top. This has the effect of
						# sorting values into bins they don't belong to and
						# leaving gaps. Setting bins to the above corrects this
						# by placing everything to a have interval, 
						# (eg. 1 --> 1.5), all values are correctly sorted down

fig, ax = subplots()
ax.hist(counts,thebins)
ax.plot(x,1000*Poisson(x),label="Predicted Poisson overlay")
ax.legend()
title("photon detection simulation")
xlabel("Occurence of photon counts in 1000 trials")
ylabel("Number of Photon Counts")
fig.show()

input("Showing plot. Press <enter> to exit.\n (Plot not saved automatically)")


