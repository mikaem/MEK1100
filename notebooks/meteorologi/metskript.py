import numpy as np 
import pylab as plt

# transpose nedenfor tilpasser datasett som var lagret for bruk i Matlab
# slik at de kan brukes i Python

p = np.transpose(np.loadtxt('trykkfelt.dat'))
u = np.transpose(np.loadtxt('vindfelt_u.dat'))
v = np.transpose(np.loadtxt('vindfelt_v.dat'))

print (p.shape)
print (u.shape)
print (v.shape)

Nx, Ny = p.shape

isobarer = np.arange(980, 1025, 5)
x = np.linspace(0,1600,Nx)
y = np.linspace(0,1600,Ny)
xx, yy = np.meshgrid(x,y, indexing='ij')
CS = plt.contour(xx,yy,p, isobarer)
plt.clabel(CS, inline=1, fontsize=10, fmt='%1.0f', colors='k')


plt.figure()
plt.quiver(xx,yy,u,v)

l = np.sqrt(u**2 + v**2)
l_max = l.max()
print ('max vindhastighet ', l_max)

dudx = np.gradient(u, axis=0)
dvdy = np.gradient(v, axis=1)
div = dudx + dvdy
plt.figure()
isobarer = np.array([-9,-4,-3,-2,-1,0,1,2])
CS = plt.contour(xx,yy,div,10)
plt.clabel(CS, inline=1, fontsize=10, fmt='%1.0f', colors='k')

dudy = np.gradient(u, axis=1)
dvdx = np.gradient(v, axis=0)
curlz = dvdx - dudy
plt.figure()
CS = plt.contour(xx,yy,curlz)
plt.clabel(CS, inline=1, fontsize=10, fmt='%1.0f', colors='k')
plt.show()
