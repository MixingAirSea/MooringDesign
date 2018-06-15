from __future__ import division
from numpy import *
from scipy import *
from matplotlib.pyplot import *
from math import *
from pylab import *
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

# Constants
w = 0.4  # weight per unit length (g*m/L)
x_0 = 5  # position with zero y tension

# make these smaller to increase the resolution
dW, da = 0.05, 0.05

# generate 2 2d grids for the x & y bounds
W, a = np.mgrid[slice(6, 16 + da, da),
                slice(1, 10 + dW, dW)]

L = a * sinh((W - x_0) / a) - a * sinh(-x_0 / a)
D = a * cosh((W - x_0) / a) - a * cosh(-x_0 / a)
T_y = w * (a * sinh((W - x_0) / a))

# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.
L = L[:-1, :-1]
D = D[:-1, :-1]
T_y = T_y[:-1, :-1]
levels1 = MaxNLocator(nbins=35).tick_values(0, 50)
levels2 = MaxNLocator(nbins=25).tick_values(-10, 10)
levels3 = MaxNLocator(nbins=35).tick_values(0, 8)


# pick the desired colormap, sensible levels, and define a normalization
# instance which takes data values and translates those into levels.
cmap = plt.get_cmap('PiYG')
norm = BoundaryNorm(levels1, ncolors=cmap.N, clip=True)

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)

cf = ax0.contourf(W[:-1, :-1] + dW / 2.,
                  a[:-1, :-1] + da / 2., L, levels=levels1,
                  cmap=cmap)
fig.colorbar(cf, ax=ax0)
ax0.set_title('L (length of string)')
ax0.set_xlabel('W (x distance)')
ax0.set_ylabel('a (T_x/weight density)')


# contours are *point* based plots, so convert our bound into point
# centers
cf = ax1.contourf(W[:-1, :-1] + dW / 2.,
                  a[:-1, :-1] + da / 2., D, levels=levels2,
                  cmap=cmap)
fig.colorbar(cf, ax=ax1)
ax1.set_title('D (y-distance)')
ax1.set_xlabel('W (x distance)')
ax1.set_ylabel('a (T_x/weight density)')

cf = ax2.contourf(W[:-1, :-1] + dW / 2.,
                  a[:-1, :-1] + da / 2., T_y, levels=levels3,
                  cmap=cmap)
fig.colorbar(cf, ax=ax2)
ax2.set_title('T_y (y-component of tension)')
ax2.set_xlabel('W (x distance)')
ax2.set_ylabel('a (T_x/weight density)')

# adjust spacing between subplots so `ax1` title and `ax0` tick labels
# don't overlap
fig.tight_layout()

plt.show()