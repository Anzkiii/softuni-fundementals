
n = int(input())
numsList = []
specialNum = 0
for i in range(1, n + 1):
    stringI = str(i)
    for k in stringI:
        numsList.append(k)
    for j in numsList:
        specialNum += int(j)
    if specialNum == 5 or specialNum == 7 or specialNum == 11:
        print(f"{i} -> True")
        numsList = []
        specialNum = 0
    else:
        print(f"{i} -> False")
        numsList = []
        specialNum = 0