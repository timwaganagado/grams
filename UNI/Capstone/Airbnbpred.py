import tkinter as tk
from tkinter import *

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

import joblib
model = joblib.load(dir_path+"/Airbnb_LR.pkl")

class MyGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Predict Airbnb log price")
        self.vars = ["amount of amenities","Acomadates","Bathrooms","Number of reviews","Reviews score","Bedrooms","Beds"]
        self.var = []
        for x,y in enumerate(self.vars):
            self.var.append(tk.IntVar(self.main_window))
            f = Frame(self.main_window)
            f.pack(padx = 10)
            tk.Label(f,text=f"{y}").pack(side="left")
            tk.Entry(f,textvariable= self.var[x]).pack(side="left")

        f = Frame(self.main_window)
        f.pack(padx=10)
        tk.Button(f,text="Calculate Points",command=self.showinformation).pack(side="left")
        tk.Button(f,text="Quit",command=self.main_window.destroy).pack(side="left")
        tk.mainloop()
    def showinformation(self):
        amenities = self.var[0].get()
        acomadates = self.var[1].get()
        bathrooms = self.var[2].get()
        numberofreviews = self.var[3].get()
        reviewsscore = self.var[4].get()
        bedrooms = self.var[5].get()
        beds = self.var[6].get()
        predicted_value = model.predict([[0,1,amenities,acomadates,bathrooms,4,1,1,3,1,1,80,0,33,-118,numberofreviews,reviewsscore,bedrooms,beds]])
        tk.Label(self.main_window,text=f"Predicted log price: {predicted_value}").pack()
MyGUI()