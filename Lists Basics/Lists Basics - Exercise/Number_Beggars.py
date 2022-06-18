#This took me longer then it should have, im leaving a note here just bc of how proud i am this actually works ;-;
intString = [int(x) for x in input().split(", ")]
countBeggars = int(input())
finLst = [0] * countBeggars
ind = 0
for index, value in enumerate(intString):
    try:
        finLst[ind] += value
    except IndexError: 
        ind = 0
        finLst[ind] += value
    ind += 1
print(finLst)

