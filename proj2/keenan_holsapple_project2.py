# Keenan Holsapple
# ECEN 4503
# Project 2

# To execute, run "Python keenan_holsapple_project2.py"
# The execution should reveal the histograms with the PDFs detailed

#PROJECT2 ASSIGNMENT
# Create a Gaussian distributed random value of X and repeat to form a new random value for Y.
# Form a random value of Z and theta.
# Repeat to create a large number of iterations for Z and theta
# Find analytical distributions among what we leanred in the lectures that seem to fit your estimated PFDs
#TLDR: Plot sample distributions and analytical distributions (along with names and parameters); histogram

import numpy as np
import random
import matplotlib.pyplot as plt

# defining parameters for nomral function
# X~N(0,1) and Y~N(0,1)
variance = 1
mean = 0


# initializing count variable
i = 0

#initializing arrays with empty sets
xArr = [0] * 10001
yArr = [0] * 10001
zArr = [0] * 10001
thetaArr = [0] * 10001
xrandArr = [0] * 10001
yrandArr = [0] * 10001

while (i < 10000):

    # creating random variable for x
    xrand = random.uniform(-5, 5)

    # storing random variable generated into array
    xrandArr[i] = xrand

    # normal equation for x
    x = (np.exp((-1/2) * ((xrand - mean) / variance)**2)) / (variance * np.sqrt(2 * np.pi)) 

    # generating random value for y
    yrand = random.uniform(-5, 5)

    # storing y value into array
    yrandArr[i] = yrand

    # normal equation for y
    y = (np.exp((-1/2) * ((yrand - mean) / variance)**2)) / (variance * np.sqrt(2 * np.pi))  
    

    # defining z with x and y values
    z = np.sqrt((x**2 + y**2))

    # storing normal values into array
    xArr[i] = x
    yArr[i] = y

    # defining theta with provided equation
    if(x >= 0):
        theta = np.arctan((y/x))
    if(x < 0):
        theta = np.arctan((y/x)) + np.pi

    # storing values of z and theta into array
    zArr[i] = z
    thetaArr[i] = theta

    # incrementing for loop
    i += 1


# Generating plots with PDFs on domain of -5 and 5
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10,10))

# x normal plot
# plt.scatter(xrandArr, xArr)
axs[0,0].scatter(xrandArr, xArr)
axs[0,0].set_title("Random Value X PDF")
axs[0,0].set_ylabel("Normal Variable X Value Generated")
axs[0,0].set_xlabel("Possible Generated Values (-5/5)")

axs[0,1].scatter(yrandArr, yArr)
axs[0,1].set_title("Random Value Y PDF")
axs[0,1].set_ylabel("Normal Variable Y Values Generated")
axs[0,1].set_xlabel("Possible Generated Values (-5/5)")


axs[1,0].scatter(xrandArr, zArr)
axs[1,0].set_title("Random Value Z PDF")
axs[1,0].set_ylabel("Normal Variable Z Values Generated")
axs[1,0].set_xlabel("Possible Generated Values (-5/5)")

axs[1,1].scatter(xrandArr, thetaArr)
axs[1,1].set_title("Random Value Theta PDF")
axs[1,1].set_ylabel("Normal Variable Theta Values Generated")
axs[1,1].set_xlabel("Possible Generated Values (-5/5)")

plt.show()


