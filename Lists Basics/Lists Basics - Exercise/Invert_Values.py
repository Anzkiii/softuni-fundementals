
numList = input().strip().split(" ")
for i in range(len(numList)):
    numList[i] = int(numList[i])
for index, value in enumerate(numList):
    numList[index] = -value
print(numList)