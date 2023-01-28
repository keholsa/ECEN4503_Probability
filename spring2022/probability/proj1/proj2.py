import tkinter as tk
from tkinter import *

root = tk.Tk()
window = root.winfo_height
root.geometry("700x400")
root.title("Monty Hall Problem")

titleLabel = tk.Label(root, text="Project 1.2: Monty Hall Problem", font=("Segoe UI", 24, "bold")).place(x=120,y=15)

label1 = tk.Label(root, text="Select a Door:", font=("Segoe UI", 14)).place(x=285, y=85)

firstDoorBtn = tk.Button(text="Door #1" ,width=25, height=4)
firstDoorBtn.place(x=50, y=140)
secondDoorBtn = tk.Button(text="Door #2", width=25, height=4)
secondDoorBtn.place(x=250, y=140)
thirdDoorBtn = tk.Button(text = "Door #3", width=25, height=4)
thirdDoorBtn.place(x=450, y=140)

firstDoorLbl = tk.Label(text="?", borderwidth=2, relief="solid", width=25, height=4)
firstDoorLbl.place(x=50, y=250)
secondDoorLbl = tk.Label(text="?", borderwidth=2, relief="solid", width=25, height=4)
secondDoorLbl.place(x=250, y=250)
thirdDoorLbl = tk.Label(text="?", borderwidth=2, relief="solid", width=25, height=4)
thirdDoorLbl.place(x=450, y=250)

#TODO: Add functional Label: "Monty Reveals a goat behind " + doorNumber + ". Choose a door once again to end the game"

#TODO: write function with actual math, include parameters for all three door labels
root.mainloop()










