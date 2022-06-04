
n = int(input())
lst = []
for i in range(n):
    num = int(input())
    lst.append(num)
positivesSum = 0
negativeSum = 0
posLst = []
negLst = []
for i in lst:
    if i >= 0:
        positivesSum += 1
        posLst.append(i)
    else:
        negativeSum += i
        negLst.append(i)
print(posLst,"\n",negLst)
print(f"Count of positives: {positivesSum}\nSum of negatives: {negativeSum}")