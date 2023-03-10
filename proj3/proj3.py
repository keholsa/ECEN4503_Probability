# Keenan Holsappel
# Project 3
# ECEN 4503

# A pair of random vairables (x,y) have uniform distribution over the unit circle
# Joint PDF is f_x,y(x,y) = 1/x for x^2 + y^2 < 1 and f_x,y (x,y) - 0 otherwise
# Generate large number of sampels fo this pair of random vairables
# THREE OUTPUTS 
# Figure 1: 2D-histogram of sample (x,y) and the analytical joint pdf
# Figure 2: 2D-histogram of samples x and analytical marginal PDF of x
# Figure 3: 1D-histogram of sampels x falling in the region -0.01<y<0.01 and the analytical conditional pdf of x given y=0

import random
import math
import matplotlib.pyplot as plt




# defining sample count
numSamples = 100000


# initializing variables
randomXArr = [0] * (numSamples + 1)
randomYArr = [0] * (numSamples + 1)
jointPDFArr = [0] * (numSamples + 1)
marginalXArr = [0] * (numSamples + 1)
marginalYArr = [0] * (numSamples + 1)
samplesYArr = [0] * (numSamples + 1)
conditionalSamplesArr = [0] * (numSamples + 1)

# generating the joint PDF balue
def generate_JointPDF(numSamples):

    i = 0
    while(i < numSamples): 
        # defining random numbers
        randomX = random.uniform(-1.25,1.25)
        randomXArr[i] = randomX

        randomY = random.uniform(-1.25,1.25)
        randomYArr[i] = randomY

        # evaluating expression
        conditionalVal = randomX**2 + randomY**2

        # conditional expression based on rules
        if(conditionalVal < 1):
            jointPDF = 1 / math.pi
            jointPDFArr[i] = jointPDF
        else:
            jointPDF = 0
            jointPDFArr[i] = jointPDF
        
        i += 1

    return randomXArr, randomYArr, jointPDFArr 

# marginal pdf function for x
def marginal_pdf_X(numSamples, randomXArr):

    i = 0
    while(i < numSamples):

        # condition -1<=x<=1
        if(randomXArr[i] >= -1 and randomXArr[i] <= 1):

            # marginal eq
            marginalXArr[i] = (2 * math.sqrt(1-randomXArr[i])) / math.pi
        else:
            marginalXArr[i] = 0
        
        i += 1

    return marginalXArr


# determien conditional pdf
def conditional_pdf_y(numSamples, randomYArr, jointPDFArr):

    i = 0


    # finding marginal pdf for y random values
    marginalYArr = marginal_pdf_X(numSamples, randomYArr)


    while(i < numSamples):

        # conditional requirements for random variable                                         
        if(randomYArr[i] >= -.01 and randomYArr[i] <= .01):
     
            # assigns samples based on if condition is satisfied
            samplesYArr[i] = randomYArr[i]


            # cannot divide by zero, limit
            if(marginalYArr[i] == 0):
                conditionalSamplesArr[i] = 0
            else:
                
                # perfoming function to find conditional pdf
                conditionalSamplesArr[i] = jointPDFArr[i] / marginalYArr[i]

        i += 1


    return samplesYArr, conditionalSamplesArr



        





#plot figure 1
randomXArr, randomYArr, jointPDFArr = generate_JointPDF(numSamples)
plt.hist2d(randomXArr, randomYArr, weights=jointPDFArr, bins=(100,100), cmap='Blues')
plt.colorbar()
plt.show()

#plot figure 2
marginalXArr = marginal_pdf_X(numSamples, randomXArr)
plt.hist(marginalXArr, weights=randomXArr, bins=50)
plt.show()
    

#plot figure 3
samplesYArr, conditionalSamplesArr = conditional_pdf_y(numSamples, randomYArr, jointPDFArr)
plt.hist(samplesYArr, weights=conditionalSamplesArr, bins=50)
plt.show()

