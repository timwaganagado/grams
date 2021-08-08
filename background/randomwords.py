import random
text = ''
num = 0
while num != 10:
    for x in range(random.randint(1,6)):
        text += random.choices(['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'],[1,6,57,37,35,9,19,38,37,16,43,29,17,9,13,15,1,6,28,1,1,23,5,11,34,15])[0]
    text += ' '
    num+=1
print(text)