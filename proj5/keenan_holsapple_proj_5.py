# Keenan Holsapple
# ECEN 4503
# Project 5
# 3/31/23

# to run:
# 1. python keenan_holsapple_proj_5.py
# 2. enter desired number of iterations
#   - higher the better in displaying uniform distribution as to validate Z_PDF

# ------Expectation------
# SIGNAL QUANTIZATION
# X is uniform random variable over (0, 100). Form new random variable Y by rounding
# X to nearest integer. Form roundoff error to Z = X - Y (quantization noise)
# a) find analytical PDF of Z along with mean squared value E[Z^2] (quantization noise power)
# b) create a histogram for the random variable Z and compare it with PDF found analytically in a)
# c) Find the sample average of Z^2 and compare it with a)
#
# submit code, plots, and results


import random
import matplotlib.pyplot as plt
import numpy as np


#----------FUNCTIONS DEFINED-------------------

# function for generating x, y, and z as random numbers
def generate_random_numbers(iterations):

    # initialize arrays and count
    i = 0
    XArr = [0] * (iterations + 1)
    YArr = [0] * (iterations + 1)
    ZArr = [0] * (iterations + 1)

    while(i < iterations):

        # specifying X as uniform between 0 and 100
        X = random.uniform(0, 100)
        XArr[i] = X
        
        
        # specifying Y as rounded value of X
        Y = round(X)
        YArr[i] = Y
        
        
        # specifying Z as quantization noise
        Z = X - Y
        ZArr[i] = Z
        
        # increment
        i += 1

    return XArr, YArr, ZArr

# function defining analytical PDF and returns array of based on conditional answer
def analytical_PDF_Z(Z, iterations):

    # initializing count and array
    i = 0
    z_pdfArr = [0] * (iterations + 1)

    # while loop that generates Z pdf array on size of array
    while(i < iterations):

        # uniform distribution, states validity betweeon options 0 and 1
        if Z[i] >= 0 and Z[i] <= 1:
            
            # domain of possible placement
            z_pdfArr[i] = .5

        else:

            # domain of possible placement
            z_pdfArr[i] = -.5

        # increment
        i += 1

    return z_pdfArr

# specifying QNP as an integer
def quantization_noise_power(Z, iterations):

    # initializing sum and count
    i = 0
    ZSum = 0
    
    # while less then desired count
    while(i < iterations):

        # E[Z^2] as sum
        ZSum = (Z[i] ** 2) + ZSum

        #increment
        i += 1

    # 1/n * sum(z^2)
    QNP  = (1 / iterations) * (ZSum)

    return QNP

# defining sample average as integer
def sample_average(Z, iterations):

    # initializing variables
    i = 0
    ZSum = 0

    # sum of z^2 over iterations
    while(i < iterations):
        ZSum = (Z[i]**2) + ZSum
        i += 1

    # sample average is equal to sum / numCount 
    sampleAverage =  ZSum / iterations

    return sampleAverage

# percent error calculation for sample average and QNP
def percent_error(actual, theoretical):
   
    difference = actual - theoretical
    quotient = difference / theoretical

    percent_error = quotient * 100

    return percent_error


# taking in desired number of iterations from user
iterations = input("How many iterations?: ")
iterations = int(iterations)

#---------Calling functions-------------------

# getting random numbers as arrays
X, Y, Z = generate_random_numbers(iterations)

# getting analytical PDF as array
Z_PDF = analytical_PDF_Z(Z, iterations)

# getting quantization noise power as integer
QNP = quantization_noise_power(Z, iterations)

# getting sample average as integer
sampleAverage = sample_average(Z, iterations)

# getting percent error as integer
percentError = percent_error(sampleAverage, QNP)

print("")

# print statements for comparison (Part C)
print("Quantization Noise Power: " + str(QNP))
print("Sample Average of Z squared: " + str(sampleAverage))
print("Percent Error: " + str(percentError) + "%")
print("These evnetually come to share the same function, while they are different concepts. Percent error should always be 0%")

print("")

# creating plots in one frame for comparison
fig, axs = plt.subplots(2,2, figsize = (10,10))

# histogram of random variable Z
axs[0,0].hist(Z, bins=100)
axs[0,0].set_title("Histogram of Random Variable Z")
axs[0,0].set_xlabel("Possible Value for Z")
axs[0,0].set_ylabel("Number of Occurrences at Value")

# histograom of analytical PDF for random variable Z
axs[0,1].hist(Z_PDF, bins=100)
axs[0,1].set_title("Histogram of Analytical PDF for Z")
axs[0,1].set_xlabel("Possible Value for Z")
axs[0,1].set_ylabel("Number of Occurrences at Value")


# mix of two graphs onto one for comparison of boundary in uniform scale
axs[1,0].hist(Z, alpha=.5 ,bins=100)
axs[1,0].hist(Z_PDF, alpha=.5, bins=100)
axs[1,0].set_title("Comparison Between Plots 1 and 2")
axs[1,0].set_xlabel("Possible Value for Z")
axs[1,0].set_ylabel("Number of Occurrences at Value")



# removes 4th subplot since not necessary
fig.delaxes(axs[1,1])

fig.suptitle("PDF is shown in Z Histogram Creating Boundary")

# displays plot
plt.show()


    

