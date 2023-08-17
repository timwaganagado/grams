import time
import csv
with open("numders.csv","w",newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Start","Times"])
    for x in range(999,2000):
        start = x
        new = x
        times = 0
        listofnews = []
        print("starting number:",new)
        while round(new) != 1:
            times += 1
            if new % 2 == 1:
                new = new * 3 +1
            else:
                new /= 2 
            print(times,new,end="\r")
            listofnews.append(new)
    
    #for x,y in enumerate(listofnews):
    #    print(x,y,end=", " )
    #print(end="\n")
        print("It took",times,"times to reach a point in which it repeats")
        writer.writerow([start,times])

