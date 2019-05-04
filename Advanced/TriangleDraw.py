#!/usr/bin/env python3

# PURPOSE: Draw a triangle
# NOTE: Doesn't always work, due to some matplotlib draw function error

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
import time

X = 512
Y = 512

									# choose the boundary size

pvals = np.zeros((X,Y,3), dtype='uint8')
pvals = pvals +255
									
									# Establish an array that is X by Y by 3
									# units. (3 is for supporting spaces for 
									# each of the 3 primary colors, RGB
									# Adding 255 to everything sets the 
									# background to white

plotarr = np.flipud(pvals.transpose(1,0,2))

									# Makes a new variable the effect of
									# transposing (exchanging x and y) then
									# flipping top to bottom will establish
									# the x and y axes as we are familiar with
									
f1, ax1 = plt.subplots()

									# plt.subplots() returns a tuple, these
									# are handed off to the variables f1
									# and ax1 

picture = ax1.imshow(plotarr, interpolation='none')
ax1.axis('off')
f1.show()

									# The variable picture is assigned to
									# .imshow operates on our transposed grid
									# (details, doesn't matter) returning pixel
									# coordinates. Interpolation alters pixels
									# that gives a visual effect to bordering
									# pixel sets. "None" gives no effect, so
									# the image appears blocky


for i in range (50,400):
	m = 3/4
	pvals[i:400,50:int(i*m),0:2] = 0

for i in range (70,380):
	m = 3/4
	pvals[i:380,70:int(i*m)-25,:] = 255

									# I made two triangles, a blue one then a 
									# white one on top of it. By specifying a
									# slope of 3/4, that sets the requred 3-4-5
									# triangle
									# In the beginning, I set ALL pvals "color
									# coordinates" to 255 givig white all over.
									#
									# So here in the first triangle, I
									# set the first two to 0 so only the last
									# "color coordinate" is set all way. The
									# last one is blue (RGB). In the second
									# for loop here, I set all the "color
									# coordinates" to their max value, 
									# returning white

picture.set_data(plotarr)
ax1.draw_artist(picture)
f1.canvas.blit(ax1.bbox)
									# These functions are necessary for the
									# configuration and display of all this


im = Image.fromarray(plotarr, 'RGB')
im.save('Triangle.tif')

input("\nPress <Enter> to exit...\n")

									# Without this last "input", the image
									# would disappear immediately


