import tkinter
from tkinter import *

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("ST1 week 5 - 1")
        self.first = []
        self.second = tkinter.IntVar(self.main_window)
        f = Frame(self.main_window)
        f.pack(padx=10)
        b1 = tkinter.Label(f,text=f"Ammount of laps")
        b2 = tkinter.Entry(f,textvariable= self.second)
        b1.pack(side="left")
        b2.pack(side="left")
        f = Frame(self.main_window)
        f.pack(padx=10)
        tkinter.Button(f,text="Show Laps",command=self.showlaps).pack(side="left")
        tkinter.mainloop()
    def showlaps(self):
        for x in range(self.second.get()):
            f = Frame(self.main_window)
            f.pack(padx=10)
            self.first.append(tkinter.IntVar(self.main_window))
            b1 = tkinter.Label(f,text=f"Lap {x+1} time:")
            b2 = tkinter.Entry(f,textvariable= self.first[x])
            b1.pack(side="left")
            b2.pack(side="left")
        f = Frame(self.main_window)
        f.pack(padx=10)
        tkinter.Button(f,text="Calculate Times",command=self.showinformation).pack(side="left")
    def showinformation(self):
        a = 0
        s = float("inf")
        l = 0
        for x in self.first:
            t = x.get()
            a+=t
            if t < s:
                print(t)
                s = int(t)
                print(s)
            if t > l:
                l = t
        a /= len(self.first)
        tkinter.Label(self.main_window,text=f"Average lap time: {a}").pack()
        tkinter.Label(self.main_window,text=f"Shortest lap time: {s}").pack()
        tkinter.Label(self.main_window,text=f"Longest lap time: {l}").pack()
        
        
MyGUI()