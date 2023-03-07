import random
def play(statmanet):
    if "y" in statmanet or statmanet == '':
        return True
    return False
playing = True
print(f"{'Welcome to Guess the number':=^31}")
print(f"{'With a twist':=^31}")
while playing:
    guessed = False
    answer = random.randint(1,100)
    guesses = 0
    while not guessed:
        guesses += 1
        check = False
        while not check:
            guess = input("Guess a number: ")
            try:
                guess = int(guess)
                check = True
            except :
                pass
        
        match [guess < answer,guess == answer]:
            case [True,False]:
                print("Higher")
            case [_,True]:
                print(f"Got It, the number was {answer}")
                guessed = True
            case [False,False]:
                print("Lower")
        
        if random.choices([True,False],[1,4])[0]:
            move = random.randint(-99,99)
            while 0 > (answer+move) or (answer+move) > 100:
                move = random.randint(-99,99)
            answer += move
            
            match [move<0,move>0]:
                case [True,False]:
                    print("Oh no, the answer moved down")
                case [False,True]:
                    print("Oh o, the answer moved up")
    print(f"It took you {guesses} guesses, well done.")
    playing = play(input("Again?: "))
print("See you again!")