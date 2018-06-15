from __future__ import division
from numpy import *
from scipy import *
from matplotlib.pyplot import *
from math import *
from pylab import *

# Constants
w = 0.4  # weight per unit length (g*m/L)
D = 1  # y distance
W = 1  # x distance
r = 10  # range for D and W
aD_list = []
aW_list = []
D_list = []
W_list = []


# Function of a, a = T_x/weight linear density
def f(a):
    return cosh(W / a) - (D + a) / a

# find how a changes as D increases
while D <= r:
    D = D + 0.1
    D_list.append(D)

    # Make a guess for a
    a = 1
    a_plus = 0.01
    a_minus = 100
    k = 1e-7  # k<<1

    # Bisection Algorithm
    while (f(a) < -k or f(a) > k):
        if f(a) > k:
            a_plus = a
            a = (a_plus + a_minus) / 2
        elif f(a) < -k:
            a_minus = a
            a = (a_plus + a_minus) / 2
    aD_list.append(a)

# find how a changes as W increases
while W <= r:
    W = W + 0.1
    W_list.append(W)

    # Make a guess for a
    a = 1
    a_plus = 0.01
    a_minus = 100
    k = 1e-7  # k<<1

    # Bisection Algorithm
    while (f(a) < -k or f(a) > k):
        if f(a) > k:
            a_plus = a
            a = (a_plus + a_minus) / 2
        elif f(a) < -k:
            a_minus = a
            a = (a_plus + a_minus) / 2
    aW_list.append(a)

aD = asarray(aD_list)
aW = asarray(aW_list)
D = asarray(D_list)
W = asarray(W_list)


# Tension
T_xD = w * aD
T_yD = w * cosh(1 / aD)
T_xW = w * aW
T_yW = w * sinh(W / aW)

#Graph
figure()
f1 = plot(D, T_xD, c='r', label='Length_y vs Tension_x',
linestyle='--', linewidth=2)
f2 = plot(D, T_yD, c='b', label='Length_y vs Tension_y',
linestyle='--', linewidth=2)
f3 = plot(W, T_xW, c='r', label='Length_x vs Tension_x')
f4 = plot(W, T_yW, c='b', label='Length_x vs Tension_y')
xlabel('Chain Length')
ylabel('Tension')
title('Chain Length vs Tension')
legend(loc='upper left')
show()



