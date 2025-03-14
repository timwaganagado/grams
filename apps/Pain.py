import random

def randombool():
    return random.choice([True,False])

print("A crazy feeling")

culture_primary = ["Sapha","Voltamp","Nullic","Tulem",None]

culture_specific = {"Sapha":["Phoenix","Ashen","Tormec","Adiaplatic"],"Voltamp":["Aeroman","Ferroat"],"Nullic":["nullic"],"Tulem":["tulem"]}

culture_alternate = ["Weaver","Sound","Craft"]

class vortex():
    def __init__(self):
        self.primary = None
        self.specific = None
        self.alternate = None
        self.create_culture()
    def create_culture(self):
        #mainculture
        self.primary = random.choice(culture_primary)
        #if mainculture select specific
        if self.primary:
            self.specific = random.choice(culture_specific[self.primary])
        #culture alternate
        if randombool() or not self.primary:
            self.alternate = random.choice(culture_alternate)
    def show_vortex(self):
        if self.primary:
            print(f"{self.primary}\n{self.specific}")
        if self.alternate:
            print(self.alternate)


active = True

def seperateline():
    print("__________________________________")

while active:
    seperateline()
    com = int(input("0 | Quit\n1 | Create New Vortex\n"))
    if com == 1:
        new = vortex()
        new.show_vortex()
    else:
        active = False
