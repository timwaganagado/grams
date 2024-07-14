import tkinter
from tkinter import *

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("ST1 Carb Calculator")
        self.first = []
        self.texts = ["Enter fat grams: ","Enter carb grams: "]
        for y,x in enumerate(self.texts):
            f = Frame(self.main_window)
            f.pack(padx=10)
            b1 = tkinter.Label(f,text=f"{x}")
            self.first.append(tkinter.IntVar(self.main_window))
            b2 = tkinter.Entry(f,textvariable= self.first[y])
            b1.pack(side="left")
            b2.pack(side="left")
        f = Frame(self.main_window)
        f.pack(padx=10)
        tkinter.Button(f,text="Calculate Sum",command=self.showinformation).pack(side="left")
        tkinter.Button(f,text="Remove calculations",command=self.calculations).pack(side="left")
        tkinter.mainloop()
    def calculations(self):
        self.first = []
    def showinformation(self):
        tkinter.Label(self.main_window,text=f"Calories from fat: {self.first[0].get()*3.9}").pack()
        tkinter.Label(self.main_window,text=f"Calories from carbs: {self.first[1].get()*4}").pack()
MyGUI()