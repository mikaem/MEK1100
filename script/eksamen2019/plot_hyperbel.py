import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 1000)[:, None]
C = np.linspace(-1, 1, 5)[None, :]
plt.plot(x, -C/5/x, '--')
plt.plot(x, np.sqrt(2*C/10+x**2), x, -np.sqrt(2*C/10+x**2))
plt.axis([-1, 1, -1, 1])
#plt.show()
