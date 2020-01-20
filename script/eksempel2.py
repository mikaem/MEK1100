import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

h0 = 2277. # Hoyden av toppen av fjellet (m)
R = 4.     # Maal for radius av fjellet (km)
t = np.linspace(-10, 10, 21)
x, y = np.meshgrid(t, t, indexing="ij") # Grid for x- og y-verdiene (km) 
h = h0/(1+(x**2+y**2)/R**2)        # Beregn hoyden h (m)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
#surf = ax.plot_surface(x, y, h, cmap=plt.cm.jet, linewidth=0, antialiased=False) 
surf = ax.plot_surface(x, y, h, color='b', linewidth=1) 
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel("x") 
ax.set_ylabel("y") 
ax.set_zlabel("h") 
#plt.show()

plt.figure()
plt.contour(x, y, h)
plt.figure()
plt.contourf(x, y, h, 100)
plt.show()