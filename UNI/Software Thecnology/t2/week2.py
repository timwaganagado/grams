import tkinter as tk

class MyGUI:
    def __init__(self):
        self.main_window =tk.Tk()
        self.main_window.title("Week 2")
        self.main_window.geometry("500x100")
        tk.Label(self.main_window,text= f"===Welcome Program===").pack()
        tk.Label(self.main_window,text= f"Welcome to Python").pack()
        tk.Label(self.main_window,text= f"Welcome to Computer Science").pack()
        tk.Label(self.main_window,text= f"Programming is fun").pack()
        tk.mainloop()
mygui = MyGUI()  