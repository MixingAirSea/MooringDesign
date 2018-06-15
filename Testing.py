from __future__ import division
from numpy import *
from scipy import *
from matplotlib.pyplot import *
from math import *
from pylab import *

#constants
n = 2  # initial number of points
L = 10  # ending point (length is constant)
L_0 = 0  # starting point

# Create Lists
dx_list = []
RMS_dy = []  # RMS list of dy
RMS_ddy = []  # RMS of actual ddy
RMS_dy_act = []  # RMS of d1_dy minus dy
RMS_ddy_act = []  # RMS of d1_ddy minus ddy


# creating a function to differentiate y
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


# creating a function to 2nd differentiate y
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


# Create values of y' and y'' for different dx values
while (n <= 200):
    n = n + 1  # increase number of points on the line-(length is constant)
    dx = (L - L_0) / n  # changes between each point in x

    X = dx / L  # make dx unitless for graphing
    dx_list.append(X)

    # generating x values
    x = linspace(L_0, L, n)

    # generating y values
    A = 5  # amplitude
    y = A * sin(x / L)
    y = reshape(y, (n, 1))  # y values becomes a nx1 matrix

    #First differentive of y using d1
    dy = diff(y)
    dy = squeeze(asarray(dy))  # converts matrix into an array

    #Actual 1st derivative of func_y
    dy_actual = A / L * cos(x / L)

    #Second differentive of y using d2
    ddy = d_diff(y)
    ddy = squeeze(asarray(ddy))  # converts matrix into an array

    #Actual 2nd derivative of func_y
    ddy_actual = -A / L ** 2 * sin(x / L)

    #Calculating RMS
    RMSdy = sqrt(mean(dy ** 2))
    RMSddy = sqrt(mean(ddy ** 2))
    RMSdyact = sqrt(mean((dy_actual - dy) ** 2))
    RMSddyact = sqrt(mean((ddy_actual - ddy) ** 2))
    RMS_dy.append(RMSdy)
    RMS_ddy.append(RMSddy)
    RMS_dy_act.append(RMSdyact)
    RMS_ddy_act.append(RMSddyact)

#Convert list into arrays
dx_arr = asarray(dx_list)

RMS_dy_arr = asarray(RMS_dy)
RMS_ddy_arr = asarray(RMS_ddy)
RMS_dy_act_arr = asarray(RMS_dy_act)
RMS_ddy_act_arr = asarray(RMS_ddy_act)

dy_RMS = RMS_dy_act_arr / RMS_dy_arr
ddy_RMS = RMS_ddy_act_arr / RMS_ddy_arr

#Graphing
figure()
# plotting RMS vs dx for first derivative
d1_err = plot(dx_list, dy_RMS, c='r', label='First Derivative')
# plotting RMS vs dx for second derivative
d2_err = plot(dx_list, ddy_RMS, c='b', label='Second Derivative')

legend(loc='upper left')
plt.xlabel('dx/L')
plt.ylabel('RMS(Dy-dy)/RMS(dy)')
plt.title('RMS of Discrete Derivatives vs dx')
semilogy()  # logscale the y axis

show()