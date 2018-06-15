from __future__ import division
from numpy import *
from scipy import *
from matplotlib.pyplot import *
from math import *
from pylab import *

n = 100  # number of points
dx = 0.1  # change in x
w = 0.4  # weight per unit length


# First Derivative Function
def diff(a):
    # D1: creating a nxn matrix to calculate 1st derivative of y
    d1 = [[0 for i in range(n)] for j in range(n)]
    # first row is different
    d1[0][0] = -3
    d1[0][1] = 4
    d1[0][2] = -1
    # last row is different
    d1[n - 1][n - 3] = 1
    d1[n - 1][n - 2] = -4
    d1[n - 1][n - 1] = 3
    # creating the rows in between 1st row and last row
    for i in range(n - 2):
        d1[i + 1][i] = -1
        d1[i + 1][i + 2] = 1
    return 1 / (2 * dx) * matmul(d1, a)  # matmul=matrix multiplication


# Second Derivative Function
def d_diff(a):
    # D2: creating a nxn matrix to calculate second derivative of y
    d2 = [[0 for i in range(n)] for j in range(n)]
    # first row is different
    d2[0][0] = 1
    d2[0][1] = -2
    d2[0][2] = 1
    # last row is different
    d2[n - 1][n - 3] = 1
    d2[n - 1][n - 2] = -2
    d2[n - 1][n - 1] = 1
    # creating the rows in between 1st row and last row
    for i in range(n - 2):
        d2[i + 1][i] = 1
        d2[i + 1][i + 1] = -2
        d2[i + 1][i + 2] = 1
    return 1 / (dx ** 2) * matmul(d2, a)  # matmul=matrix multiplication