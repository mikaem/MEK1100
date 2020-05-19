import numpy as np
import matplotlib.pyplot as plt

w = 1
v0 = 0.1
r = np.linspace(0, 1, 100)[:, None]
theta = -w/v0*r + np.linspace(-2, 2, 5)[None, :]
plt.plot(r*np.cos(theta), r*np.sin(theta))
plt.show()
