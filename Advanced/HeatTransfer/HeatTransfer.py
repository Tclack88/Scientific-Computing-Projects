#!/usr/bin/env python3

# PURPSE: plot a best fit exponential curve to data retrieved prior from heat transfer apparatus

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys
import warnings

warnings.simplefilter('ignore')

				# My code works, but I get an "overflow error" message
				# displayed, likely due to hitting some exponential limit while
				# iterating... so this suppresses that

datafile = sys.argv[1]

DatCol = np.loadtxt(datafile)

DatArr = DatCol.T


t = np.linspace(0, len(DatArr), len(DatArr))
y = DatArr


f1, ax1 = plt.subplots()
ax1.plot(t,y,linestyle='dotted',label='raw data')
plt.legend()
f1.show()



def func(t,a, b,c):
	return a*np.exp(-b*t)+c

				# define an exponential function to fit the raw data, but these
				# variables a,b,c are yet to be determined

popt,pcov = curve_fit(func, t, y)
print("\n Exponential a*exp(-bt)+c\n")
print('a ='+str(popt[0]))
print('b ='+str(popt[1]))
print('c ='+str(popt[2]))
print("\ntime constant(1/b) = "+str(1/popt[1]))
ExpLabel = 'exp fit --->  time constant ='+str(1/popt[1])
ax1.plot(t,func(t,*popt),label=ExpLabel)
ax1.legend()
f1.show()

				# curve_fit returns a tuple, the first, 'popt', are its chosen
				# best fit values. The second, 'pcov' (which will not be called 
				# here) are its error. Returned information of the best fit
				# values as well as the time constant and plotted the two on
				# top of each other

input("\nShowing plot. Press <Enter> to exit...\n")

