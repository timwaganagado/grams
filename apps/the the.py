import random

inp = input("the the: ")
word = ''
randword = []
step = -1
for x in inp:
    step += 1
    if x == ' ':        
        randword.append(word)
        word = ''
        save = step
    else:
        word += x
word = ''
for x in range(save,len(inp)):
    if inp[x] != ' ':
        word += inp[x]
randword.append(word)



while inp != ' ':
    funny = ''
    for x in range(0,random.randint(4,7)):
        funny += random.choice(randword) + ' '
    funny = funny[:-1]

    print(funny)
    inp = input('again')