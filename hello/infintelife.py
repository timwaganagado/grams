import random
p = 0 
o = 0
while p < 100:
    e = 100
    # print(f'person {p+1}')
    y = 1
    l = random.randint(1,e)
    while l != 1 :
        l = random.randint(1,e)
        y += 1
    # print(f'years lived {y} years')
    p += 1
    if o < y:
        o = y
print(f'Oldest Age {o}')