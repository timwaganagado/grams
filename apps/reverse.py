test = input("")
result = ""
for x in range(len(test)-1,-1,-1):
    temp = test[x]
    result += temp
print(result)