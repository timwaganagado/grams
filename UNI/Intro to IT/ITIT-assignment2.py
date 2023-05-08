import tkinter
from tkinter import *

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Stage 2 Astronaut Mass Calculator")
        self.main_window.configure(bg='grey')
        
        self.planets = {"Mercury":0.378,"Venus":0.907,"Moon":0.166,"Mars":0.377,"Io":0.1835,"Europa":0.1335,"Ganymede":0.1448,"Callisto":0.1264}
        
        f = Frame(self.main_window)
        f.grid(row="0",column="0",pady=10,padx=40)
        tkinter.Label(f,text="Destinatin",font=(25)).pack(side="top")
        
        f = Frame(self.main_window)
        f.grid(row="1",column="0",pady=10,padx=40)
        scrollbar = Scrollbar(f)
        scrollbar.pack( side ="right", fill = Y )
        self.mylist = Listbox(f, yscrollcommand = scrollbar.set )
        for line,x in enumerate(self.planets):
           self.mylist.insert(END, f"{x}")
        self.mylist.pack( side = LEFT, fill = BOTH )
        scrollbar.config( command = self.mylist.yview )
        self.mylist.bind("<<ListboxSelect>>", self.callback)
        
        f = Frame(self.main_window)
        f.grid(row="2",column="0",pady=20)
        self.label = tkinter.Label(f,text="")
        self.label.pack(side="top")
        
        f = Frame(self.main_window)
        f.grid(row="3",column="0",pady=20)
        tkinter.Button(f,text="Calculate",command=self.showinformation).pack(side="left")
        tkinter.Button(f,text="Exit",command=self.main_window.destroy).pack(side="left")
        
        
        f = Frame(self.main_window)
        f.grid(row="0",column="1")
        tkinter.Label(f,text="Max Tool Weights",font=(25)).pack(side="top")
        
        f = Frame(self.main_window)
        f.grid(row="1",column="1")
        tkinter.Label(f,text="Crew: 100 kg",font=(10)).pack(side="top",pady=10)
        
        f = Frame(self.main_window)
        f.grid(row="2",column="1")
        tkinter.Label(f,text="Specalist: 150 kg",font=(10)).pack(side="top",pady=10)
        
        f = Frame(self.main_window)
        f.grid(row="0",column="2")
        tkinter.Label(f,text="Tool Weights",font=(25)).pack(side="top")
        
        f = Frame(self.main_window)
        f.grid(row="1",column="2")
        self.crew = [tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar()]
        for x,y in enumerate(self.crew):
            tkinter.Entry(f,textvariable= self.crew[x]).pack(side="top")
        
        f = Frame(self.main_window)
        f.grid(row="2",column="2")
        self.specalist = [tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar()]
        for x,y in enumerate(self.specalist):
            tkinter.Entry(f,textvariable= self.specalist[x]).pack(side="top")
        
        
        f = Frame(self.main_window)
        f.grid(row="0",column="3")
        tkinter.Label(f,text="Available",font=(25)).pack(side="top")
        self.crewlist = []
        self.speclist = []
        
        f = Frame(self.main_window)
        f.grid(row="1",column="3")
        for x in range(3):
            new = tkinter.Label(f,text="")
            self.crewlist.append(new)
            new.pack(side="top")
        
        f = Frame(self.main_window)
        f.grid(row="2",column="3")
        for x in range(3):
            new = tkinter.Label(f,text="")
            self.speclist.append(new)
            new.pack(side="top")
            
        f = Frame(self.main_window)
        f.grid(row="0",column="4",padx=30)
        tkinter.Label(f,text="Calculations",font=(25)).pack(side="top")
        
        
        f = Frame(self.main_window)
        f.grid(row="1",column="4",padx=30)
        self.tAM = tkinter.Label(f,text="Total Average Mass: ",font=(15))
        self.tAM.pack(side="top",pady=10)
        self.aAM = tkinter.Label(f,text="Average Available Mass: ",font=(15))
        self.aAM.pack(side="top",pady=10)
        self.aAMP = tkinter.Label(f,text="Average Available Mass on planet: ",font=(15))
        self.aAMP.pack(side="top",pady=10)

        

        
        tkinter.mainloop()
        
    def showinformation(self):
        try: # most errors come from the tkinter libarary so errors are dealt with such
            totalMass = 0
            totalAvailable = 0
            averageOnPlanet = 0
            for x,y in enumerate(self.crew):
                new = y.get()
                totalMass += new
                available = 100 - new
                totalAvailable += available

                self.crewlist[x].config(text=f"{available} Kg")
            for x,y in enumerate(self.specalist):
                new = y.get()
                totalMass += new
                available = 150 - new
                totalAvailable += available
                averageOnPlanet += 150 - new * self.planets[self.mylist.get(self.mylist.curselection())]
                self.speclist[x].config(text=f"{available} Kg")

            self.tAM.config(text=f"Total Average Mass: {totalMass}")
            totalAvailable/=6
            self.aAM.config(text=f"Average Available Mass: {round(totalAvailable,5)}")

            averageOnPlanet/=6
            self.aAMP.config(text=f"Average Available Mass on planet: {round(averageOnPlanet,5)}")
            
        except tkinter.TclError as err:
            self.label.configure(text=f"try selecting a planet or \n inputing a number into weights")

    def callback(self,event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            self.label.configure(text=f"Mass multiplier for {data} is {self.planets[data]}")
        else:
            self.label.configure(text="")
    
MyGUI()