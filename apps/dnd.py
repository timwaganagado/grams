import tkinter
from tkinter import *
import random

class Ent:
    def __init__(self,name):
        self.name = name

def donothing():
    print("0")
    return 0

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

class hp:
    def __init__(self,target,frame):
        self.target = target
        self.f = target.create_frame(frame)
        f = self.f
        allignment = "player"
        tkinter.Label(f,text=f"{allignment}").pack(side="left")

        self.hp = tkinter.IntVar(f)
        self.hplabel = tkinter.Label(f,text=f"Hp: {self.hp.get()}")
        self.hplabel.pack(side="left")
        tkinter.Entry(f,textvariable= self.hp).pack(side="left")
        tkinter.Button(f,text="Max hp",command=self.updatelabel).pack(side="left")

        self.name = tkinter.IntVar(f)
        tkinter.Entry(f,textvariable= self.name).pack(side="left")

        self.inita = tkinter.IntVar(f)
        self.initalabel = tkinter.Label(f,text=f"init: {self.hp.get()}")
        self.initalabel.pack(side="left")
        tkinter.Entry(f,textvariable= self.inita).pack(side="left")
        tkinter.Button(f,text="init",command=self.updateinita).pack(side="left")

        self.remove = tkinter.IntVar(f)
        tkinter.Entry(f,textvariable= self.remove).pack(side="left")
        tkinter.Button(f,text="Damage",command=self.removehp).pack(side="left")

        self.add = tkinter.IntVar(f)
        tkinter.Entry(f,textvariable= self.add).pack(side="left")
        tkinter.Button(f,text="Heal",command=self.addhp).pack(side="left")

        tkinter.Button(f,text="dead",command=self.clearframes).pack(padx=10,side="left")


    def updatelabel(self):
        self.hplabel["text"] = f"Hp: {self.hp.get()}"
    
    def updateinita(self):
        self.initalabel["text"] = f"init: {self.inita.get()}"
    
    def removehp(self):
        self.hp.set(self.hp.get() - self.remove.get())
        self.updatelabel()
    
    def addhp(self):
        self.hp.set(self.hp.get() - self.add.get())
        self.updatelabel()

    def clearframes(self):
        for widget in self.f.winfo_children():
            widget.destroy()
        self.playerframe.pack_forget()
        self.target.ent.remove(self)

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Dnd")
        menubar = Menu(self.main_window)
        menubar.add_command(label="Players", command=self.playeradd)
        menubar.add_command(label="Enemies", command=self.enemyadd)
        self.main_window.config(menu=menubar)
        
        
        self.downframe = self.create_frame(self.main_window)
        
        self.controlframe = self.create_frame(self.downframe,"left")
       
        f = self.create_frame(self.controlframe)
        tkinter.Label(f,text=f"burton Dnd").pack()

        f = self.create_frame(self.controlframe)
        tkinter.Button(f,text="Players", command=self.playeradd).pack()
        tkinter.Button(f,text="Enemies", command=self.enemyadd).pack()
        tkinter.Button(f,text="roll init",command=self.rollinit).pack()

        self.entframe = self.create_frame(self.downframe,"left")
        tkinter.Label(self.entframe,text=f"Players").pack()

        self.eneframe = self.create_frame(self.main_window,"left")
        f = self.create_frame(self.eneframe)
        tkinter.Label(f,text=f"enemies").pack(side='left')
        tkinter.Button(f,text="Clear",command=self.clearframes).pack(side='left')
        
        self.eneframe = self.create_frame(self.eneframe,"left")

        self.ent = []
        tkinter.mainloop()

        
    def create_frame(self,target,side="top"):
        frame = Frame(target)
        frame.pack(padx=5,side=side)
        return frame
    
    def clearframes(self):
        for widget in self.eneframe.winfo_children():
            widget.destroy()
        self.ent = []

    def rollinit(self):
        for x in self.ent:
            x.inita.set(random.randint(1,20))
            x.updateinita()

    def playeradd(self):
        
        hp(self,self.entframe)
    
    def enemyadd(self):
        self.ent.append(hp(self,self.eneframe))
        
    


MyGUI()