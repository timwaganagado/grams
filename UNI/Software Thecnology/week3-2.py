import tkinter



class MyGUI:
    def __init__(self):
        self.main_window =tkinter.Tk()
        self.main_window.title("Week 3 - Problem 2")
        
        self.var_sale = tkinter.StringVar(self.main_window)
        
        tkinter.Label(self.main_window,text="Projected Sales").grid(row=0,column=0,padx=5,pady=5)
        tkinter.Entry(self.main_window,textvariable=self.var_sale).grid(row=0,column=1,padx=5,pady=5)
        
        tkinter.Button(self.main_window,text="Calculate",command=self.showinformation).grid(row=1,column=0,padx=5,pady=5)
        
        self.label_name = tkinter.Label(self.main_window)
        self.label_name.grid(row=2,column=0,padx=5,pady=5)
        
        tkinter.mainloop()
    def showinformation(self):
        self.label_name.config(text=f"Profit: {int(self.var_sale.get())*0.23}")
        
        
MyGUI = MyGUI()