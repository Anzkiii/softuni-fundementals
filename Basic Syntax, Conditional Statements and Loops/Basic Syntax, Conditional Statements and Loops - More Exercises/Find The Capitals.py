
someString = input()
someStringIndexes = []
for index, letter in enumerate(someString):
    if letter.isupper():
        someStringIndexes.append(index)

print(someStringIndexes)
