from talent import Talent

talentTestList = []

run = True
while run:
    print("Exit: 0\nsee Talents: 1\nadd Talent: 2\nChange value: 3\n")
    option = int(input(""))
    if option == 0:
        run = False
    if option == 1:
        print("=== Printing Talent Objects ===")
        for x in talentTestList:
            print("=============================")
            x.toString()
    if option == 2:
        adding = True
        while adding:
            name = input("Name: ")
            tal_id = input("ID: ")
            cat = input("catagorey: ")
            talentTestList.append(Talent(name,tal_id,cat))
            print(f"\nadded {talentTestList[-1].show_name()}")
            add = int(input("\nadd another: 1 \nstop adding: 2\n"))
            if add == 2:
                adding = False
    if option == 3:
        changing = True
        if len(talentTestList) == 0:
            print("no Talents")
            changing = False
        while changing:
            select = int(input("select though index: 1\nselect through name (case sensetive): 2\n"))
            if select == 1:
                print([x.show_name() for x in talentTestList])
                select = int(input("index\n"))
            if select == 2:
                serach = True
                while serach:
                    name = input("name (case sensitive)\n")
                    for y,x in enumerate(talentTestList):
                        if x.show_name() == name:
                            select = y
                            serach = False
                    if serach == True:
                        print("name not in list")
            
            print("change name: 1\nchange ID: 2\nchange cat: 3")
            value = int(input())
            if value == 1:
                name = input("name: ")
                talentTestList[select].mut_name(name)
            if value == 2:
                name = input("id: ")
                talentTestList[select].mut_id(name)
            if value == 3:
                name = input("cat: ")
                talentTestList[select].mut_cat(name)

            change = int(input("change another: 1\nstop changing: 2\n"))
            if change == 2:
                changing = False
    print()