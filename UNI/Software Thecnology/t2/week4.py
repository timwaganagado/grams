import tkinter as tk
from tkinter import *

class MyGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("ST1 Book Calculator")
        self.amountOfBooks = tk.IntVar(self.main_window)
        f = Frame(self.main_window)
        f.pack(padx = 10)
        tk.Label(f,text=f"Enter the number of books purchased:").pack(side="left")
        tk.Entry(f,textvariable= self.amountOfBooks).pack(side="left")

        f = Frame(self.main_window)
        f.pack(padx=10)
        tk.Button(f,text="Calculate Points",command=self.showinformation).pack(side="left")
        tk.Button(f,text="Quit",command=self.main_window.destroy).pack(side="left")
        tk.mainloop()
    def showinformation(self):
        total = 0
        books = self.amountOfBooks.get()
        if books >= 8:
            total = 60
        elif books >= 6:
            total = 30
        elif books >= 4:
            total = 15
        elif books >= 2:
            total = 5
        tk.Label(self.main_window,text=f"Books purchased: {books}").pack()
        tk.Label(self.main_window,text=f"Total income: {total}").pack()
MyGUI()