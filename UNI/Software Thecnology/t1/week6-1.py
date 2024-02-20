import tkinter
from tkinter import *

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("ST1 Seat Calculator")
        self.first = []
        self.texts = ["Class A seats:","Class B seats:","Class C seats:"]
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
        tkinter.mainloop()
    def showinformation(self):
        total = 0
        cost = 20
        for x in self.first:
            total += x.get() * cost
            cost -= 5

        tkinter.Label(self.main_window,text=f"Total income: {total}").pack()
MyGUI()