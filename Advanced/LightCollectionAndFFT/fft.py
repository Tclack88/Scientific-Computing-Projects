#!/usr/bin/python3

import numpy as np
import sys 
import matplotlib.pyplot as plt
from scipy import signal

datafile = sys.argv[1]

DatCol = np.loadtxt(datafile)

DatArr = DatCol.T

		# this program operates by typing in it's name followed by a data file
		# so the second argument [1] is that data file.From there, np.loadtxt
		# outputs an array. Since we only have one number string per line this
		# returns a column vector. We need a row vector, so we transpose it 


t = np.linspace(0, len(DatArr)-1, len(DatArr))
y = DatArr
y = signal.detrend(y,type='linear')
f1, ax1 = plt.subplots()
ax1.plot(t,y)
f1.show()

			# This just sets a t axis length (rather then making it fixed
			# I based it on the data length so if data was collected for a
			# longer time, this will adjust to that) and a y-axis
			# I had to ad signal.detrend of the data in y to remove the 
			# 'pink noise'(zero-frequency DC component of the power spectrum)
			# the plot is shown

ft = np.fft.fft(y,n=16*len(DatArr))
ftnorm = abs(ft)
ps = ftnorm**2

print (ft)
print(ftnorm)
print(ps)


xvals = np.fft.fftfreq(len(ps), 1.0/len(DatArr))
f2, ax2 = plt.subplots()
ax2.plot(xvals,ps)
ax2.set_xlim(0,int(np.max(xvals)))
plt.title("Mikayla Smells")
f2.show()

			# np.fft performs a discrete fourier transform of the data, 
			# returning peaks representing relative heights of separate
			# component frequencies. The power spectrum just by definition
			# is the norm squared of a Fourier Transform
			# the arguments of fft:
			#  operates on data y. n = 16*len(DatArr) (the example given takes
			#  the number of sample points and multiplies it by 16. This seems
			#  to be a good aribitray choice, so I kept it)
			# xvals is the cycles/sec, here the fftfreq arguments mean there
			# are len(ps): window length for xvals axis with 1/len(DatArr) (or
			# 1/920 in this case) set as the sample spacing.
			# xvals is a frequency range, so I have the length set to that
            # max value so it adjusts dynamically to any input
			# show the plot and keep it open with input

peak = np.argmax(ps)
print("Peak Frequency:",xvals[peak])

			# argmax returns the index number of an array element that is the
			# max. I invoke this index of the xvals (frequency) to return that
			# frequency associated with the largest value peak

input("\nShowing plot and power spectrum. Press <Enter> to exit...\n")

