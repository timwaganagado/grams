import random
def genlist():
    test = []
    for x in range(random.randint(3,10)):
        test.append(random.randint(0,15))
    return test

test = genlist()
print(test)


def bubblesort(test):
    test = list(test)
    for y in range(len(test)-1,0,-1):
        print(f"Pass {len(test) - y}: {test}") 
        for x in range(y):
            if test[x] > test[x+1]:
                temp = test[x+1]
                test[x+1] = test[x]
                test[x] = temp
                print(f"  Swap {test[x+1]} and {test[x]} -> {test}")
    return test

bubble = bubblesort(test)
print(bubble)

