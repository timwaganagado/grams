import random
import time
def attackindex(i,aohp,e_p):
    if i == 0:
        e_p = random.randint(1,3)
        e_a = 1
    if i == 1:
        print('Enemy miss')
        aohp = aohp
        e_a = 0
    if i == 2:
        print('Enemy hit')
        aohp = aohp - 1 
        e_a = 0
    if i == 3:
        print('Enemy put you on fire')
        aohp = aohp - 2
        e_a = 0
    time.sleep(1)
    return aohp , e_p , e_a