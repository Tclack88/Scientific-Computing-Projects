#!/usr/bin/python3

import matplotlib.pyplot as plt

import numpy as np


angles = np.linspace(0,np.pi*5,100)

						# define my range of inputs, 100 equally spaced
						# divisons from 0 to 5pi radians (recall 1 pi radian
						# is a half cycle)

sine = [np.sin(angle) for angle in angles]
cosine = [np.cos(angle) for angle in angles]

						# assign variable name to each function being plotted

plt.plot(angles,sine)
plt.plot(angles,cosine)

						# plots angles in the "x-axis" and sine and cosine 
						# respectively in the "y-axis"

plt.legend(['Sine','Cosine'])

						# Just something extra. It wasn't asked but I thought
						# it would be nice to have a legend. The order must
						# math with the plt.plot order above

plt.title('Sine and Cosine over 2.5 cycles')
plt.xlabel('angle(radians)')
plt.show()
						
						# assigns a title, a label for the "x-axis" and puts
						# all this into a single graph
