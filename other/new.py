import csv
import statistics as stats

def test():
    with open('other/test.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')

def averageage():
    with open("other/username.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ';')
        totalage = 0
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                totalage += int(row[4])
            line_count += 1
        print(f'Average age : {int(totalage/(line_count-1))}')

def medianage():
    with open("other/username.csv") as csv_file:
        csv_reader = csv.reader(csv_file,delimiter = ";")
        ages = []
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                ages.append(row[4])
            line_count += 1
        print(f'Medain age : {int(stats.median(ages))}')
        
def maxage():
    with open("other/username.csv") as csv_file:
        csv_reader = csv.reader(csv_file,delimiter = ";")
        age = 0
        name = 0
        line_count = 0
        for row in csv_reader:
            cur_age = row[4]
            if line_count != 0:
                if int(cur_age) > age:
                    age = int(cur_age)
                    name = row[2]
            line_count += 1
        print(f'Oldest age : {name} {age}') 

def minage():
    with open("other/username.csv") as csv_file:
        csv_reader = csv.reader(csv_file,delimiter = ";")
        age = 100
        name = 0
        line_count = 0
        for row in csv_reader:
            cur_age = row[4]
            if line_count != 0:
                if int(cur_age) < age:
                    age = int(cur_age)
                    name = row[2]
            line_count += 1

        print(f'Youngest age : {name} {age}') 
        
        
if __name__ == "__main__":
    #test()
    #write out to txt e.g
    #Average age = x
    averageage()
    
    #Median age = x
    medianage()
    
    #<name> has the maximum age
    maxage()
    #<name> has the min name
    minage()
    #function to get average
    #
    #function to get max
    #
    #function to get min
    #
    #function to get median