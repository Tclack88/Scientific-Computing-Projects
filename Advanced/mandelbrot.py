#!/usr/bin/python3

# PURPOSE: generate a mandelbrot set. Parameters can be changed to specify the regions
# uncomment the regions below (~line30) to vary parametes and explore different regions

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

X = 512
Y = 384


IT = 80
					# Interations

LIM = 2

					# Chosen because no complex number with a real or imaginary
					# part greater than 2 can be apart of the set. If we are
					# are squaring a complex number (which involves subtraction
					# of any negative part from squaring the imaginary number)
					# any complex number outside of the circle of radius 2 is
					# unbounded

pvals = np.zeros((X,Y), dtype='uint')


for i in range(X):
	for j in range(Y):
#		c = complex(4*(i-X/2)/(X),4*(j-Y/2)/(Y))
#		c = complex(-1+.5*(i-X/3)/X,.3+.5*(j-Y/2)/Y)
		c = complex(-.8+.2*(i-X/4)/X,.15+.2*(j-Y/4)/Y)					
					# Uncommont the c's above for different regions

		z = 0 + 0j
		print (i)
		for n in range(IT):
			z = z**2 + c
			if abs(z) >= LIM:
				pvals[i,j] = n
				break
			
					# the first two "foor loops" establish each complex number						# c to be tested for "Mandelbrotness"
					# In the last "for loop", each of these c's are iterated
					# then if the size exceeds a limit, it is colored:::
					#
					# the color of each point represents how quickly the values
					# reach the escape points. Since 255 is the max character						# value that can be assigned, we choose 250 as a nice round
					# upper limit. Black of course fails to escape before
					# the limit and gradually brighter colors are used for
					# points that escape

plotarr = np.flipud(pvals.transpose())

f1, ax1 = plt.subplots()

picture = ax1.imshow(plotarr, interpolation='none', cmap='copper')
ax1.axis('off')
f1.show()
					# The rest of the above is discussed in a different problem
					# except cmap, which just controls the colormap used
					# to display the values; it's a dictionary that maps
					# numbers to colors

im = Image.fromarray(plotarr, 'RGB')
im.save('Mandelbrot.ps')

					# Create an image to save as a post script file

input("\nPress <Enter> to exit...\n")                                             
