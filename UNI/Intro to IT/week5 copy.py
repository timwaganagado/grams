import re
import tkinter
tofrom = input("translate: ")
if "y" in tofrom:
    tofrom = True
else:
    tofrom = False

def dicto():
    translate = {}
    with open("UNI/Intro to IT/translate.txt") as f:
        lines = f.readlines()
        for x in lines:
            currentline = x.strip()
            for pos,l in enumerate(currentline):
                if l == ":":
                    normalword = currentline[:pos]
                    translatedword = currentline[pos+1:]
                    if tofrom:
                        translate.update({normalword:translatedword})
                    else:
                        translate.update({translatedword:normalword})
        f.close
    return translate

pattern = "[^a-zA-Z]"

def clear(word):
    word = re.sub(pattern,'',word)   
    return(word)

def addword(translated):
    translatingword = target[lastposition:pos]
    clearedword = clear(translatingword)
    try:
        translated += translate[clearedword]
        for x in translatingword:
            if clear(x) == "":
                translated += f"{x}"
        translated += " "
    except:
        notaword.append(clearedword)
        translated += translatingword + " "
    return translated

translate = dicto()

class MyGUI:
    def __init__(self):
        pass
lastposition = 0
translated = ""
notaword = []
for pos,x in enumerate(target):
    if x == " ":
        translated = addword(translated)
        lastposition = pos+1
pos += 1
translated = addword(translated)
        
print(translated)
if notaword:
    print(f"we are missing some translations for these words", end = " ")
    [print(x+",",end=" ") for x in notaword]