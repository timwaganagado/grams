import tkinter as tk



class MyGUI:
    def __init__(self):
        currentpop = 25690000
        self.main_window =tk.Tk()
        self.main_window.title("Week 2")
        self.main_window.geometry("500x100")

        tk.Label(self.main_window,text= f"Million",height=5,width=50).pack(side="left")
        tk.Entry(self.main_window,width=50).pack(side="left")
        tk.Label(self.main_window,text= f"year 1",width=50).pack(side="left")
        tk.mainloop()
mygui = MyGUI()
