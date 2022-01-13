import time
import random
word = input('secret message ')
fin = ''
for i in range(0,len(word),1):
    for l in range(0,4):
        print(fin, end='')
        print(chr(random.randint(33,126)),end='\r')
        time.sleep(0.05)
    fin = fin + word[i]
    print(fin, end='\r')
    time.sleep(0.05)
print(fin)
