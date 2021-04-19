import matplotlib.pyplot as plt
import numpy as np

a,b = 4,1

o = np.linspace(0,10,100)
#o = np.linspace(0,20,3000)

x = (a-b)*np.cos(o) + b*np.cos(o*(a-b)/b)
y = (a-b)*np.sin(o) - b*np.sin(o*(a-b)/b)

plt.plot(x,y)
plt.show()
