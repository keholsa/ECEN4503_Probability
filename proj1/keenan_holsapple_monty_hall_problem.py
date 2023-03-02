# To run, make sure Python 3.x.x is installed, and navigate to the directory
# that "requriredLibraries.txt" is found. Open a terminal in that directory and run:
# pip install -r requirements.txt
# to run, from command line perform "python keenan_holsapple_monty_hall_problem.py"

# Project 1.2 - Performing the Monty Hall Game
# Click on "New Game" -> Select a Door -> Select another Door -> Click on "New Game" to play again!
# Code written with Tkinter GUI and rearranges the initial three component array of {Car, Goat, Goat}
# then assigns each element to a label before the game starts

#required libraries for implementaiton
import tkinter as tk
from tkinter import *
import random
from array import *

# Root and window declaration
root = tk.Tk()
window = root.winfo_height
root.geometry("700x400")
root.title("Monty Hall Problem")
titleLabel = tk.Label(root, text="Project 1.2: Monty Hall Problem", font=("Segoe UI", 24, "bold")).place(x=120,y=15)

# randomizes 100000 times, viewable in console lien
def proofFunc():

    #declaring variables
    componentArr = ["Car", "Goat", "Goat"]
    proofArr = [[None for j in range(3)] for i in range(10000)]
    randomInt = 0
    goatCount = 0
    carCount = 0
    win = 0
 
    i = 0
    j = 0
    #loop performs game 10000 times
    while i < 10000: 

        #performs same game mechanic of randomizing predefined array
        random.shuffle(componentArr)
        #bot picks numbers 0-2 to determine which element will be picked
        randomInt = random.randint(0,2)
        
        #nested loop to assign values to double array
        while j < 3:
            proofArr[i][j] = componentArr[j]
            if(proofArr[i][j] == "Goat"):
                goatCount += 1
            if(proofArr[i][j] == "Car"):
                carCount += 1

            #conditional statements that determine if the computer won
            if(randomInt == 0):
                if(proofArr[i][0] == "Car"):
                    win += 1
            if(randomInt == 1):
                if(proofArr[i][1] == "Car"):
                    win += 1
            if(randomInt == 2):
                if(proofArr[i][2] == "Car"):
                    win += 1
            j += 1
        j = 0
        i += 1
    
    #to line statements
    print("Goats generated: " + str(goatCount))
    print("Cars generated: " + str(carCount))
    print("Number of wins: " + str(win))
    print("Probability of guessing correctly: " + str( 100 * (win / 10000)) + "%")



# Function that rebuilds form with newly managed inputs from user.
# Reason for this is because Tkinter does not allow passing of variables without volatile global variables.
# Not actual recursion just named it that because it just helped with the building process mentally
def recursiveFunc(componentArr, lbl1, lbl2, lbl3, doorNumber):

    #initializing labels
    firstDoorLbl = tk.Label(text=lbl1, borderwidth=2, relief="solid", width=25, height=4)
    firstDoorLbl.place(x=50, y=250)
    secondDoorLbl = tk.Label(text=lbl2, borderwidth=2, relief="solid", width=25, height=4)
    secondDoorLbl.place(x=250, y=250)
    thirdDoorLbl = tk.Label(text=lbl3, borderwidth=2, relief="solid", width=25, height=4)
    thirdDoorLbl.place(x=450, y=250)
    
    #initializing count variables for while loop
    i = 0
    secondDoorVal = 0

    while(i <= 2):

        # Determines at which position and if the user has selected a "Goat" icon to show the other option
        if(componentArr[i] == "Goat" and i != doorNumber):
            
            # assigning door number that will be shown to current element
            secondDoorVal = i

            # case switch that displays to screen
            if secondDoorVal == 0:
                firstDoorLbl = tk.Label(text="Goat", borderwidth=2, relief="solid", width=25, height=4)
                firstDoorLbl.place(x=50, y=250)
                break
            if secondDoorVal == 1:
                secondDoorLbl = tk.Label(text="Goat", borderwidth=2, relief="solid", width=25, height=4)
                secondDoorLbl.place(x=250, y=250)
                break 
            if secondDoorVal == 2:               
                thirdDoorLbl = tk.Label(text="Goat", borderwidth=2, relief="solid", width=25, height=4)
                thirdDoorLbl.place(x=450, y=250)    
                break

        # continues loop unless broken by found value
        i = i + 1


    # redeclaring initial label
    label1 = tk.Label(root, text="Select a Door:", font=("Segoe UI", 14)).place(x=285, y=85)

    # final commit to screen, displays full array to each assigned label
    def reveal(sol1, sol2, sol3):
        firstDoorLbl.config(text=sol1)
        secondDoorLbl.config(text=sol2)
        thirdDoorLbl.config(text=sol3)

    # redeclaring initial buttons
    firstDoorBtn = tk.Button(text="Door #1",width=25, height=4, command=lambda:reveal(componentArr[0], componentArr[1], componentArr[2]))
    firstDoorBtn.place(x=50, y=140)
    secondDoorBtn = tk.Button(text="Door #2", width=25, height=4, command=lambda:reveal(componentArr[0], componentArr[1], componentArr[2]))
    secondDoorBtn.place(x=250, y=140)
    thirdDoorBtn = tk.Button(text="Door #3", width=25, height=4, command=lambda:reveal(componentArr[0], componentArr[1], componentArr[2]))
    thirdDoorBtn.place(x=450, y=140)

# function that occurs when pressing start, builds random array here
def startFunc():
 
    #initialize array with elements for game
    componentArr = ["Car", "Goat", "Goat"]
    
    #randomize array with random function
    random.shuffle(componentArr)

    #build labels
    firstDoorLbl = tk.Label(text="?", borderwidth=2, relief="solid", width=25, height=4)
    firstDoorLbl.place(x=50, y=250)
    secondDoorLbl = tk.Label(text="?", borderwidth=2, relief="solid", width=25, height=4)
    secondDoorLbl.place(x=250, y=250)
    thirdDoorLbl = tk.Label(text="?", borderwidth=2, relief="solid", width=25, height=4)
    thirdDoorLbl.place(x=450, y=250)

    # button execution that will call the next recursive funtion with parameters that display
    # user selection
    def btnFirstDoorAssign(value, fullArr):
        recursiveFunc(fullArr, "Selected", "?", "?", 0)

    def btnSecondDoorAssign(value, fullArr):
        recursiveFunc(fullArr, "?", "Selected", "?", 1)

    def btnThirdDoorAssign(value, fullArr):
        recursiveFunc(fullArr, "?", "?", "Selected", 2)

    # declaring initial label and buttons
    label1 = tk.Label(root, text="Select a Door:", font=("Segoe UI", 14)).place(x=285, y=85)
    firstDoorBtn = tk.Button(text="Door #1" ,width=25, height=4, command=lambda:btnFirstDoorAssign(componentArr[0], componentArr))
    firstDoorBtn.place(x=50, y=140)
    secondDoorBtn = tk.Button(text="Door #2", width=25, height=4, command=lambda:btnSecondDoorAssign(componentArr[1], componentArr))
    secondDoorBtn.place(x=250, y=140)
    thirdDoorBtn = tk.Button(text = "Door #3", width=25, height=4, command=lambda:btnThirdDoorAssign(componentArr[2], componentArr))
    thirdDoorBtn.place(x=450, y=140)

# button declaration for start button
btnStart = tk.Button(root, text="New Game", command=startFunc, width=25, height=2).place(x=150, y=330)
btnProof = tk.Button(root, text="Proof", command=proofFunc, width=25, height=2).place(x=300, y=330)
# running loop for tkinter gui
root.mainloop()










