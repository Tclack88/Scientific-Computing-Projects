#!/usr/bin/env python3

# PURPOSE: Plot x,y data with error bars
# original intention was to find wind speed as a function of time of day out of curiosity

USAGE="""
usage: windplot.py datafile

       datafile is a 3-column text file containing numbers x,y,yerr.
       Data will be plotted with error bars of length 2*yerr.
       Use on wind.dat for example
"""
							# this is a statement to be printed in the event
							# of an error stated below
import sys
import os
							# This imports various useful functions, the most
							# important being accessing the file itself

if len(sys.argv) != 2:
   sys.stderr.write(USAGE)
   print('', file=sys.stderr)
   exit(1)
							# sys.argv is a list of all the arguments the user
							# has just typed into the command line. So if that
							# is not equal to 2, the user either didn't give								# a data file for this program to operate on, or
							# chose more than one file, which this program is								# not designed to handle. If this happens, then:
							# 
							# sys.stderr.write(MESSAGE) this accesses the
							# standard error and writes whatever the program
							# writer wants to the standard error
							# (i.e. Overwrites the default message)
							# (NOTE: Standard error exists as a log file in the								# system, so that's where this message is going. So
							# I suppose the advantage of going through all this
							# instead of returning "print (Message) exit(1)" is								# that we actually get the error put in a log file
							# for later review)
							#
							# I honestly can't figure out for sure what the
							# print statement is doing. It looks like it is
							# printing " " (a space) to the standard ouput, 								# (which by default gives a new line) and
							# something to the standard error. But I don't
							# know if it's just placing a space to the file
							# standard error, or if it's placing all the above
							# errors there...please let me know in the feedback.
							# the stderr log file. The script is then exited
						 
datafile = sys.argv[1]

							# Sets a variable to the 2nd argument of the user 
							# input ([1] since python begins count at 0

if not os.access(datafile, os.F_OK):
   sys.stderr.write('\nData file "%s" does not exist or cannot be read.\n'
                    % datafile)
   sys.stderr.write(USAGE)
   print('',file=sys.stderr)
   exit(1)
							# The parameter os.F_OK checks if the file actually
							# exists. If not, it will create a standard error
							# entry in the log (as described above).
			

import numpy as np
import matplotlib.pyplot as plt

drows = np.loadtxt(datafile)
wdat = drows.T
							# numpy.loadtxt(datafile) well... it loads data
							# from a text file
							# .T will transpose the data. So our 3 columns
							# are interprted as 3 rows
#
# compute plot margins
#
xmar = int(abs((wdat[0][-1] - wdat[0][0])/6))
ymar = int(abs(max(wdat[1])/4))
							# Set a margin length to be set at the ends of the
							# plot (so the data isn't squished at the edges)
							#
							# abs is absolute value. So for xmar, we are taking
							# the difference betwen our last row and first row
							# and dividing by 6 to get total margin length (4)
							# (wdat[0][-1] can be thought of as "from the first
							# [0] of wdat go to the last [-1] entry" ... etc.)

f1, ax1 = plt.subplots()
ax1.plot(wdat[0], wdat[1], 'o')
ax1.set_xlim(wdat[0][0]-xmar, wdat[0][-1]+xmar)
ax1.set_ylim(0,max(wdat[1])+ymar)
ax1.errorbar(wdat[0],wdat[1],yerr=wdat[2],fmt=' ')

							# f1,  defines a figure box (to be called later)
							# plt.subplots selects sub regions of the plot, the
							# axes for example. 
							#
							# plot(a,b,'o') will plot row 1 and row 2 (which
							# have previously been transposed from our columns)
							# with 'o' representing the style of the plot points
							# (other options include 'x' or '.'. 
							# '3' and '4' give kickass looking airplane points)
							# 
							# set_xlim and set_ylim set the bounds which are
							# of course the end points of our data plus our
							# margines defined above
							#
							# errorbar syntax goes:
							# errobar(x-values,y_values, + other stuff)
							# this other stuff is optionally included, but
							# must take an exact form. Order doesn't seem to								# matter. 'xerr', 'yerr', are self explanatory
							# (I'm not sure if the provided error data is
							# "plus or minus the given value". I'll default
							# to no, but all I would do is add "2*" in front)
							# fmt= defines the format. A blank space gives
							# lines along the error direction 

plt.xlabel("Time of day (hour)")
plt.ylabel("Wind Speed(Knots)")
plt.title ("Wind Speed as a Function of Time of Day")
							# These are standard commands for labeling the
							# axes and title
f1.show()
							# the command that actually displays the plot
							# in a separate window

input("\nPress <Enter> to exit...\n")
							# Without this, the plot is generated then 
							# immediately vanishes... this just keeps the
							# program running and viewable

