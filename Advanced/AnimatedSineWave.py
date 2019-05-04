#!/usr/bin/python3

# PURPOSE: animated sine wave generation

import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


class Scope(object):
			# a class is a blueprint that is used to create objects
			# Here we are defining a class called "Scope" and having it take on
			# the methods and attributes already assigned to the class "object"
			#
 			# each of these "definitions" that follow which call "self" in the 
			# arguments are "instance methods". This allows instance methods to
			# to access the attributes and modify an object's state

	def __init__(self, ax, maxt=2, dt=0.02):
		self.ax = ax
		self.dt = dt
		self.maxt = maxt
		self.tdata = np.array([])
		self.ydata = np.array([])
		self.t0 = time.perf_counter()
		self.line = Line2D(self.tdata, self.ydata)
		self.ax.add_line(self.line)
		self.ax.set_ylim(-1.5, 1.5)
		self.ax.set_xlim(0, self.maxt)

			# each class calls an __init__method which is a "constructor" for				# the class which blueprints the beginning attributes to an object
			# that is "instantiated" from the class

	def update(self, data):
		t,y = data
		self.tdata = np.append(self.tdata, t)
		self.ydata = np.append(self.ydata, y)
		self.ydata = self.ydata[self.tdata > (t-self.maxt)]
		self.tdata = self.tdata[self.tdata > (t-self.maxt)]
		self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt) #scrolls t
#		self.ax.figure.canvas.draw()
		self.line.set_data(self.tdata, self.ydata)
		return self.line,
		
			# this is a mutator method
			# removing the canvas.draw() allows for a smoothing looking graph 
			# the figure isn't being redrawn each time


	def emitter(self, p=0.1):
		while True:
			t = time.perf_counter() - self.t0
			w = np.pi
			v = np.sin(w*t)
			yield t, v
			            
			# this is a generator function (indicated by the 'yield'). This
			# creates an iterator. Each time it's called, it resumes where it
			# left off. In this case it yields t,v. Each time it gets called it
			# updates t (which consequently updates v)

if __name__ == '__main__':
			# the above returns true if the program is run directly from a
			# python interpreter... which is true. We might as well change this
			# to a "while True" statement for the same effect
	dt = 0.01
	fig, ax = plt.subplots()
	scope = Scope(ax, maxt=10, dt=dt)
	ani = animation.FuncAnimation(fig, scope.update, scope.emitter, interval=dt*1002.,blit=True)

			# maxt is the window width, dt is the data sample separation
			# pass a figure object to the update function (which generates each
			# new frame)
			# FuncAnimation passes the figure object to the scope.emmiter first
			# then runs scope.update to change frame
			# Blitting tells the animation whether or not to draw only the
			# pixels that change or the entire figure each time
			
	plt.figure()
	ax.set_xticklabels([""])
	fig.show()

input("press <ENTER> to exit")

			# Removing Canvas.draw() made the sine wave look very smooth, but
			# this had the undesired effect of not allowing the t-axis to
			# scroll, so set_xticklabels here hides the fact that the numbers 
			# don't update (credit Austin Taylor for finding this)
