import random
guesses = 0
answer = []
for x in range(0,3):
    answer.append(random.choice(['1','2','3','4','5']))
finnished = False
while finnished != True:
    attempt = input("numbero bitte: ")
    string = ''
    for x in range(0,len(attempt)):
        if attempt[x] == answer[x]:
            string += '+'
        else:
            string += 'x'
    print(string)
    if string == '+++':
        finnished = True
        win = True
    else:
        guesses += 1
        if guesses >= 5:
            finnished = True
            win = False
if win:
    print('you win')
else:
    print('try again')