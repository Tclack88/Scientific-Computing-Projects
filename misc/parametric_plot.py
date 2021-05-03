#Two ways of performing a 2D parametric plot
"""
#with sympy
from sympy import * 
from sympy.plotting import plot_parametric
t = symbols('t')
x = t - 3*sin(t)
#y = t - 3*sin(t) 
y = 4 - 3*cos(t)

plot_parametric(x,y,(t,0,10))
plt.show()
"""
# With matplotlib?
import matplotlib.pyplot as plt
import numpy as np
theta = np.linspace(0,10,100)
x = theta - 3*np.sin(theta)
y = 4 - 3*np.cos(theta)
plt.plot(x,y)
plt.show()
