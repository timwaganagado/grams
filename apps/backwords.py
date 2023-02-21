word = input("word or sentence to make backwards: ")
letters = []
for x in word:
    letters.append(x)
new = ""
for x in range(len(letters)):
    new += letters.pop()
print(new)