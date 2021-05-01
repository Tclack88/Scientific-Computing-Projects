import numpy as np
import matplotlib.pyplot as plt


#x = np.linspace(1,0,50000)[:-2]
x = [5]
for _ in range(180):
    x.append(x[-1]/1.2)

x = np.array(x[:-2])
y = (1+x)**(1/x)
z = (1-x)**(1/x)
print(f"for x={x[-2]}, y={y[-2]}")
print(f"for x={x[-2]}, z={z[-2]}")

plt.plot(x,y)
plt.show()
