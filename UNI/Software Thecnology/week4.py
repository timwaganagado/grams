import tkinter
from tkinter import *

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("ST1 Quiz Mark Calculator")
        self.first = [tkinter.IntVar(self.main_window),tkinter.IntVar(self.main_window),tkinter.IntVar(self.main_window),tkinter.IntVar(self.main_window)]
        for x in range(4):
            f = Frame(self.main_window)
            f.pack(padx=10)
            b1 = tkinter.Label(f,text=f"Enter quiz {x+1} marks(out of 10)")
            b2 = tkinter.Entry(f,textvariable= self.first[x])
            b1.pack(side="left")
            b2.pack(side="left")
        f = Frame(self.main_window)
        f.pack(padx=10)
        tkinter.Button(f,text="Calculate Sum",command=self.showinformation).pack(side="left")
        tkinter.mainloop()
    def showinformation(self):
        print(f"The quiz marks for STI unit is {self.first[0].get()+self.first[1].get()+self.first[2].get()+self.first[3].get()}")
MyGUI()