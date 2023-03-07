import tkinter

class MyGUI:
    def __init__(self):
        self.main_window =tkinter.Tk()
        self.main_window.title("Week 3 - Problem 1")
        
        self.var_name = tkinter.StringVar(self.main_window)
        self.var_address = tkinter.StringVar(self.main_window)
        self.var_suburb = tkinter.StringVar(self.main_window)
        self.var_state = tkinter.StringVar(self.main_window)
        self.var_postcode = tkinter.StringVar(self.main_window)
        self.var_number = tkinter.StringVar(self.main_window)
        self.var_course = tkinter.StringVar(self.main_window)
        
        tkinter.Label(self.main_window,text="Student Name").grid(row=0,column=0,padx=5,pady=5)
        tkinter.Entry(self.main_window,textvariable=self.var_name).grid(row=0,column=3,padx=5,pady=5)
        
        tkinter.Label(self.main_window,text="Student Adress").grid(row=1,column=0,padx=5,pady=5)
        tkinter.Entry(self.main_window,textvariable=self.var_address).grid(row=1,column=3,padx=5,pady=5)
        
        tkinter.Label(self.main_window,text="Suburb").grid(row=2,column=0,padx=5,pady=5)
        tkinter.Entry(self.main_window,textvariable=self.var_suburb).grid(row=2,column=3,padx=5,pady=5)
        
        tkinter.Label(self.main_window,text="State").grid(row=3,column=0,padx=5,pady=5)
        tkinter.Entry(self.main_window,textvariable=self.var_state).grid(row=3,column=3,padx=5,pady=5)
        
        tkinter.Label(self.main_window,text="Post Code").grid(row=4,column=0,padx=5,pady=5)
        tkinter.Entry(self.main_window,textvariable=self.var_postcode).grid(row=4,column=3,padx=5,pady=5)
        
        tkinter.Label(self.main_window,text="Phone number").grid(row=5,column=0,padx=5,pady=5)
        tkinter.Entry(self.main_window,textvariable=self.var_number).grid(row=5,column=3,padx=5,pady=5)
        
        tkinter.Label(self.main_window,text="Course").grid(row=6,column=0,padx=5,pady=5)
        tkinter.Entry(self.main_window,textvariable=self.var_course).grid(row=6,column=3,padx=5,pady=5)
        
        tkinter.Button(self.main_window,text="Show Information",command=self.showinformation).grid(row=7,column=2,padx=5,pady=5)
        
        self.label_name = tkinter.Label(self.main_window)
        self.label_name.grid(row=8,column=2,padx=5,pady=5)
        
        self.label_addr = tkinter.Label(self.main_window)
        self.label_addr.grid(row=9,column=2,padx=5,pady=5)
        
        self.label_sbrb = tkinter.Label(self.main_window)
        self.label_sbrb.grid(row=10,column=2,padx=5,pady=5)
        
        self.label_stte = tkinter.Label(self.main_window)
        self.label_stte.grid(row=11,column=2,padx=5,pady=5)
        
        self.label_ptcd = tkinter.Label(self.main_window)
        self.label_ptcd.grid(row=12,column=2,padx=5,pady=5)
        
        self.label_phnn = tkinter.Label(self.main_window)
        self.label_phnn.grid(row=13,column=2,padx=5,pady=5)
        
        self.label_crse = tkinter.Label(self.main_window)
        self.label_crse.grid(row=14,column=2,padx=5,pady=5)
    
        
        tkinter.mainloop()
    def showinformation(self):
        self.label_name.config(text=f"Name: {self.var_name.get()}")
        self.label_addr.config(text=f"Address: {self.var_address.get()}")
        self.label_sbrb.config(text=f"Subrub: {self.var_suburb.get()}")
        self.label_stte.config(text=f"State: {self.var_state.get()}")
        self.label_ptcd.config(text=f"Post Code: {self.var_postcode.get()}")
        self.label_phnn.config(text=f"Phone Number: {self.var_number.get()}")
        self.label_crse.config(text=f"Course: {self.var_course.get()}")
        
        
MyGUI = MyGUI()