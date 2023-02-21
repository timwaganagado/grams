import tkinter as tk

def newpop():
    return births+immagrants-deaths
totalsecondsinayear = 60*60*24*365
births = totalsecondsinayear/7
deaths = totalsecondsinayear/13
immagrants = totalsecondsinayear/45

class MyGUI:
    def __init__(self):
        currentpop = 25690000
        self.main_window =tk.Tk()
        self.main_window.title("Week 2")
        self.main_window.geometry("500x100")
        for x in range(5):
            currentpop += int(newpop())
            tk.Label(self.main_window,text= f"{round(currentpop/1000000,2)} Million",width=10).grid(row=0,column=x)
            tk.Label(self.main_window,text= f"year {x+1}",width=10).grid(row=1,column=x)
        tk.mainloop()
mygui = MyGUI()
