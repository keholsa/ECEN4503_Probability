# Keenan Holsapple
# ECEN 4503
# Project 4
# 3/22/23

# to run:
# python keenan_holsapple_proj_4.py

# ------Expectation------
# Five drones are at five marked positions. If all of them take off and distribute to the 
# marked positions, what is the expected number of drones in their original position?
# What about 10 drones? (Add iterations as input parameter)

import numpy as np

# number of trials generating output
numTrials = 1000
probability = 1 / numTrials

# defining expectation dependent on number of drones
expectation_5 = (1 / 5)  * 100
expectation_10 = (1 / 10) * 100

# drone function with number of trains, 
def drone(numTrials, probability, numDrones):

    # initializing increment
    i = 0

    # initialzing total sum of arrays generated
    totalSumDroneArr = 0

    while(i < numTrials):

        # generates random binary array of drones
        drones = np.random.binomial(n=1, p=probability, size=numTrials)

        # finds sum of full array
        dronArrSumVal = sum(drones)


        # total sum of array
        totalSumDroneArr = totalSumDroneArr + dronArrSumVal


        # loop increment
        i += 1

    # finds mean of total array sum overall and multiplies it by 100 to get percentage value
    mean = totalSumDroneArr / (numTrials * numDrones * .01)

    return mean


# defining percent error function
def analyticalError(actual, expected):
    
    # difference between expected and actual value
    difference = np.abs(actual - expected)

    # rounded error before percentage
    quotient = np.round((difference / expected), decimals=3)

    # returns with percentage
    return quotient * 100


# implementing functions with 5 drones
generated_probability_5 = drone(numTrials, probability, 5)
error_5 = analyticalError(generated_probability_5, expectation_5)

# implementing functions with 10 drones
generated_probability_10 = drone(numTrials, probability, 10)
error_10 = analyticalError(generated_probability_10, expectation_10)


# line outputs
print("")
print("On 1000 iterations...")

# five drone output
print("")
print("The probability of a drone (of five) landing in the same spot as before is: " + str(generated_probability_5) + "%")
print("The expected probaility of a drone (of five) landing in the same spot is: " + str(expectation_5) + "%")
print("Analyitcal Error of expected probability is: " + str(error_5) + "%")

# ten drone output
print("")
print("The probability of a drone (of ten) landing in the same spot as before is:" + str(generated_probability_10) + "%")
print("The expected probaility of a drone landing in the same spot is: " + str(expectation_10) + "%")
print("Analyitcal Error of expected probability is: " + str(error_10) + "%")
print("")
