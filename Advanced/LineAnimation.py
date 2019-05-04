#!/usr/bin/python3

# PURPOSE: generate an animated line drawing based on value from multithreading

import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import threading

		# All comments on the functionality of class were described in a		# previous problem and will not be re-described here

class Scope(object):

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

	def update(self, data):
		t,y = data
		self.tdata = np.append(self.tdata, t)
		self.ydata = np.append(self.ydata, y)
		self.ydata = self.ydata[self.tdata > (t-self.maxt)]
		self.tdata = self.tdata[self.tdata > (t-self.maxt)]
		self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt) 
                                            # scrolls t
		self.ax.set_ylim(self.ydata.min()-10, self.ydata.max()+10) 
                                            # scrolls y
		self.line.set_data(self.tdata, self.ydata)
		return self.line,
		

	def emitter(self):
		while True:
			t = time.perf_counter() - self.t0
			yield t, a
			            
	    # this is a generator function (indicated by the 'yield'). This
	    # creates an iterator. Each time it's called, it resumes where it
	    # left off. In this case it yields t,a. Each time it gets called it
	    # updates t (which consequently updates a). a here is a global
	    # variable called below

def InputThread():
	while True:
		global a
		b = input("Give me a number: ")
		try:
			b = float(b)
		except ValueError:
			print("Not a valid input. Try again.")
		else: a = float(b)

	    # ensures input is either a float or integer. I use b instead of
	    # a so the global variable 'a' isn't changed into a string while
	    # the programming is running (which of course results in an error)


if __name__ == '__main__':
	

	thr = threading.Thread(target = InputThread)
	thr.start()
		

	a = "Mikayla Smells"
	while type(a) == str:
		time.sleep(.001)

	    # Why the above while loop is necessary:
	    # After the threading process begins, the program would continue
	    # and try to execute what follows below, but the scope.emitter
	    # depends on the variable 'a' which isn't defined until the user
	    # inputs it in the thread above. An error message would display
	    # if the user didn't operate fast enough

	dt = 0.01
	fig, ax = plt.subplots()
	scope = Scope(ax, maxt=10, dt=dt)
	ani = animation.FuncAnimation(fig, scope.update, scope.emitter, interval=dt*1002.,blit=False)

	plt.figure()
	fig.show()






#  1. spawn a single thread with no arguments
# 2. change what the thread does to prompt the user for an input
# 3. store the input as a global variable
# 4. plot the value of that global variable (by accessing it from the 
#   'main thread')
