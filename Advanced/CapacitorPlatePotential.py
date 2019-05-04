#!/usr/bin/env python3

# PURPOSE: Visualize potential (voltage) between capacitor plates of different
# configurations. Uncomment each configuration to see

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


"""
# Configuration 1
N = 500
GS = 200
Clength = GS/3
Cwidth = GS/20
Cgap = GS/20
V = 5
"""

# Configuration 2
N = 500
GS = 200
Clength = GS/1.5
Cwidth = GS/20
Cgap = GS/40
V = 5

"""
# Configuration 3
N = 500
GS = 200
Clength = GS/7
Cwidth = GS/3
Cgap = GS/20
V = 5
"""


					# N - number of iterations
					# GS - grid size
					# Clength/Cwidth/Cgap - Capacitor length, width, gap
					# V - voltage


pvals = np.zeros((GS,GS), dtype = 'float')



FS = .5*(GS-2*Cwidth-Cgap)
					# FS = Freespace, i.e. the length extending from a plate
					# all the way to the end (achieved by taking the grid size
					# subtracting the thickness of both capacitors and the gap
def resetbounds():

	pvals[int(.5*(GS-Clength)):int(.5*(GS+Clength)), \
						int(FS):int((FS)+Cwidth)] = -V

	pvals[int(.5*(GS-Clength)):int(.5*(GS+Clength)), \
			int(FS+Cwidth+Cgap):int(FS+2*Cwidth+Cgap)] = V

					# resets the "plate pixels" to the chosen voltage
	pvals[:,0] = 0
	pvals[:,GS-1] = 0
	pvals[0,:] = 0
	pvals[GS-1,:] = 0
					# resets the edges to 0


resetbounds()

for it in range(N):
	a = np.roll(pvals,1,axis =1)
	b = np.roll(pvals,-1,axis = 1)
	c = np.roll(pvals,1, axis = 0)
	d = np.roll(pvals,-1,axis = 0)
	pvals = (a+b+c+d)/4
	resetbounds()
	if it % (N//10) ==0:
		print((100*it//N),"% complete")

### The following is original attempt, before Lipman went over rolling arrays
### in class. It took a little longer because of slicing. but it functioned
### I'm keeping it here for posterity and my own reference

"""
for it in range(N):
	for i in range(1,GS-1):
		pvals[i,1:GS-1] = (pvals[i+1,1:GS-1] + pvals[i-1,1:GS-1] \
					+ pvals[i,0:GS-2] + pvals[i,2:GS])/4
		resetbounds()

	if it % (N//10) ==0:
		print((100*it//N),"% complete")
"""


plotarr = np.flipud(pvals.transpose(1,0))

f,ax= plt.subplots()

picture = ax.imshow(plotarr,interpolation='none', cmap='afmhot')
ax.axis('off')
plt.title("Color mapping of Voltage between two capacitor plates")
f.show()

im = Image.fromarray(plotarr, 'RGB')
input("100% complete \n showing plot (plot not automatically saved)" \
		"\n press <enter> to exit")
