import random
d1 = {'open':'the door is open','close':'the door is close'}
d2 = ['open','close']
c = random.choice(d2)
print(c)
print(d1[c])