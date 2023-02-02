# To run, make sure Python 3.x.x is installed, and navigate to the directory
# that "requriredLibraries.txt" is found. Open a terminal in that directory and run:
# pip install -r requirements.txt
# to run, from command line perform "python keenan_holsapple_random_number_generator.py"

# Project 1.1- Generating a random number.
# User inputs total random numbers generated
# is charted using matplotlib


#required libraries for implementation
import random
import numpy as np
import tkinter as tk
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


#gui declarations
root = tk.Tk()
window = root.winfo_height
root.geometry("650x600")

root.title("Random Number Generator")
titleLabel = tk.Label(root, text="Project 1.1: Random Number Generator", font=("Segoe UI", 24, "bold")).place(x=10,y=15)
label1 = tk.Label(root, text="Enter amount of random numbers to be generated: ").place(x=30,y=100)

#TODO: manage textbox properties, only allow valid entries, enable enter key upon submission
textBox=Text(root, height=1, width=10)
textBox.tag_configure("right", justify='right')
textBox.place(x=325, y=100)

#initializing matlab plot on defined canvas
fig = Figure(figsize= (7,4), dpi = 100)
canvas = FigureCanvasTkAgg(fig, master=root)

#execution of program on 'Generate' button
submitbtn = tk.Button(text='Generate', width=20, height=2, master=root, command=lambda: get_random_numbers(fig, canvas)).place(x=425, y=87)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
#generation of numbers and graph
def get_random_numbers(fig, canvas): 

    #clears previous existing plot
    fig.clear()

    #casting integer from string, gets the input from user textbox
    threshold = int(textBox.get(1.0, END))

    # defining arrays and sets, will increment to 10 in 2d array
    dataArr = np.empty((threshold ), dtype=object)
    valueArr = [0] * 10
    xArr = [0,1,2,3,4,5,6,7,8,9]

    #defining count variable in loop
    i = 0
    j = 0
    elementSearch = 0
    #generating random numbers and assigning to single array
    while(i < threshold):

        #random number declaration for integer 0-9 at equal probability
        randomNum = random.randint(0,9)

        #assigning arr valeus
        dataArr[i] = randomNum

        #while loop increment
        i = i + 1

    #traverses all elements in array
    while(elementSearch < 10):

        #nested loop, will analyze array and count how many times each element occurs
        while(j < threshold):

            #condition for comparison between current and searching 
            if elementSearch == dataArr[j]:
                valueArr[elementSearch] = valueArr[elementSearch] + 1

            #increments seconary while loop
            j = j + 1

        
        #performed after nested loop
        elementSearch = elementSearch + 1

        #resents j counter
        j = 0

    #matlab plot, embedded into tkinter gui


    plt = fig.add_subplot(111)

    plt.plot(xArr, valueArr, 'o')
    plt.set_xlabel("Numbers Available in Generation (0-9)")
    plt.set_ylabel("Times Number was Generated")

    #predefining y scale
    plt.set_ylim([-5, (max(valueArr) + (max(valueArr) * .1))])
    
    plt.set_title("Chart of " + str(threshold) + " Numbers Generated (0-9)")
    
    #draw physical bounds of matlab plot
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM)

    canvas.get_tk_widget().pack(side=tk.BOTTOM)

#runs tkinter gui
root.mainloop()