

num = 66

def evenorodd(test:str):
    string = str(test)
    if string[-1] == "1" or string[-1] == "3" or string[-1] == "5" or string[-1] == "7" or string[-1] == "9":
        return False
    else:
        return True

print(evenorodd(44))
print(evenorodd())