#!/usr/bin/python3

# PURPOSE: draw a flower using postscript specifying the number of petals a user gives

petals = input("I'm gonna draw you a flower!" \
				"How many petals do you want?(keep it under 15) ")
while petals.isdigit() is False or int(petals) > 15:
	petals = input("Don't be ridiculous! Please give the proper input: ") 

petals = int(petals)
						# All the standard stuff here, checking that
						# the input is valid.
import os
						# Need this to run linux commands in order to create
						# and display the necessary files


os.system(' echo """%!PS\
\n/leaf % xscale yscale angle petal\
\n   {\
\n   /leafcol [ .5 1 .5 ] def\
\n   /ep1 [ 0 0 ] def\
\n   /ep2 [ 0 100 ] def\
\n   /cp1 [ 55 65 ] def\
\n   /cp2 [ 10 95 ] def\
\n   /ap {aload pop} def\
\n   gsave\
\n   leafcol ap setrgbcolor\
\n   0 setlinewidth\
\n   rotate % use angle from stack\
\n   scale % use xscale and yscale from stack\
\n\
\n   ep1 ap moveto\
\n   cp1 ap cp2 ap ep2 ap curveto\
\n   cp2 ap exch neg exch\
\n   cp1 ap exch neg exch\
\n   ep1 ap curveto closepath fill\
\n\
\n   grestore\
\n   } def\
\n\
\ngsave\
\n   306 350 translate\
\n\
\n   1 2 80 leaf\
\n   1 2 280 leaf\
\ngrestore\
\n/stem\
\n   {\
\n   /stemcol [ .5 .2 .2 ] def\
\n   /ep1 [ 0 0 ] def\
\n   /ep2 [ 0 100 ] def\
\n   /cp1 [ 55 65 ] def\
\n   /cp2 [ 10 95 ] def\
\n   /ap {aload pop} def\
\n   gsave\
\n   stemcol ap setrgbcolor\
\n   0 setlinewidth\
\n   rotate\
\n   scale\
\n\
\n   ep1 ap moveto\
\n   cp1 ap cp2 ap ep2 ap curveto\
\n   cp2 ap exch neg exch\
\n   cp1 ap exch neg exch\
\n   ep1 ap curveto closepath fill\
\n\
\n   grestore\
\n   } def\
\n\
\ngsave\
\n   306 500 translate\
\n\
\n   .2 4 180 stem\
\ngrestore\
\n\
\n\
\n/petal\
\n {\
\n   /petalcol [ .2 .5 .8 ] def\
\n   /ep1 [ 0 0 ] def\
\n   /ep2 [ 0 100 ] def\
\n   /cp1 [ 55 65 ] def\
\n   /cp2 [ 10 95 ] def\
\n   /ap {aload pop} def\
\n   gsave\
\n   petalcol ap setrgbcolor\
\n   0 setlinewidth\
\n   rotate\
\n   scale\
\n\
\n   ep1 ap moveto\
\n   cp1 ap cp2 ap ep2 ap curveto\
\n   cp2 ap exch neg exch\
\n   cp1 ap exch neg exch\
\n   ep1 ap curveto closepath fill\
\n\
\n   grestore\
\n  } def\
\n\
\ngsave\
\n   306 500 translate""" >| YourFlower.ps')
							# I don't know post script, not do I know if it's
							# a class requirement. But I manipulated the code
							# in the example and found out what changes petal
							# thickness, length and translation. So I made
							# what I needed to get something that looks like a
							# stem and some leaves.... in other words:
							# I can't much explain the above code. sorry :/
							#
							# This copies that string to a file called
							# YourFlower.ps. If it doesn't exist already,
							# it will be created. If it already exists, then
							# Austin Taylor found that ">|" will add all of 
							# that string and overwrite any existng content
							# (credit given where crdit is due)

for i in range(petals):
	newline = "echo "+".5 2 "+str(15+(360/petals)*i)+" petal"+" >> YourFlower.ps"
	os.system(newline)
							# Divides 360 degrees into n (the number of petals
							# asked for) parts. Properly spaces those out and
							# adds the syntax for PostScript files. I had to
							# be clever and define the new variable "newline"
							# because os.system takes string argurments, but
							# I couldn't break the string 

os.system('echo "grestore\nshowpage" >> YourFlower.ps')

							# The syntax for ending the PostScript File

os.system('echo "\nI saved this file here under YourFlower.ps\n" ')
os.system('gv YourFlower.ps')
							# Display with gv command
