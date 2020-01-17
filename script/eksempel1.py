import numpy as np 
import sympy as sp 
from sympy.vector import CoordSys3D
import matplotlib.pyplot as plt

v0,a,t = sp.symbols('v0,a,t')
N = CoordSys3D('N')

g = 9.81

x = v0*sp.cos(a)*t 
z = v0*sp.sin(a)*t - 0.5*g*t**2
r = x*N.i + z*N.k
v = sp.diff(r, t)

# Velg parametere for v0 og vinkel a
d = {'v0': 10, 'a': np.pi/4}

x = x.subs(d)
z = z.subs(d)
r = r.subs(d)
v = v.subs(d)

x = sp.lambdify(t, x)
z = sp.lambdify(t, z)

t_end = 2*d['v0']*np.sin(d['a'])/g*1.1
t0 = np.linspace(0, t_end, 100)

x0 = x(t0)
z0 = z(t0)

# plot for all domain 
plt.plot(x0, z0, 'b')
plt.ylim(1.1*z0.min(), 2*z0.max())

def plot_r(t):
    plt.plot(x(t), z(t), 'ob')
    vt = v.subs({'t': t})
    dx, dz = float(vt.coeff(N.i)), float(vt.coeff(N.k))
    plt.arrow(x(t), z(t), 0.5*dx, 0.5*dz, shape='full', width=0.05)
    vt = v.subs({'t': 0})
    dx, dz = float(vt.coeff(N.i)), float(vt.coeff(N.k))
    plt.arrow(0, 0, 0.5*dx, 0.5*dz, shape='full', width=0.05)
        
    plt.show()

if __name__ == '__main__':
    plot_r(0.5)