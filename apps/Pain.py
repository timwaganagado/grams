import random

def randombool(tru=50,fal=50):
    return random.choices([True,False],[tru,fal])[0]

print("A crazy feeling")

culture_primary = ["Sapha","Voltamp","Nullic","Tulem"]

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
        if randombool(95,5):
            self.primary = random.choices(culture_primary,[35,35,10,20])[0]
        #if mainculture select specific
        if self.primary:
            self.specific = random.choice(culture_specific[self.primary])
        #culture alternate
        if randombool(10,90) or not self.primary:
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
    elif com == 2:
        generations = int(input("Amount of characters to generate: "))
        characters_all = [vortex() for x in range(generations)]
    elif com == 3:
        primary_amo = {}
        unique = []
        specific_amo = {}
        for x in characters_all:
            trup = (x.primary,x.specific,x.alternate)
            if trup not in unique:
                unique.append(trup)
                if x.primary in primary_amo:
                    primary_amo[x.primary] += 1
                else:
                    primary_amo.update({x.primary:1})
                if x.specific in specific_amo:
                    specific_amo[x.specific] += 1
                else:
                    specific_amo.update({x.specific:1})
        print(primary_amo)
        print(unique)
        print(specific_amo)
        most = 0
        for x in primary_amo:
            if primary_amo[x] > most:
                most = primary_amo[x]
        for x in primary_amo:
            if primary_amo[x] == most:
                print(f"most common primary culture {x}, with {primary_amo[x]}")
    else:
        active = False
