
n = int(input())
word = input()
wordLst = []
for i in range(n):
    someString = input()
    wordLst.append(someString)
filteredLst = []
for i in wordLst:
    if word in i:
        filteredLst.append(i)
print(wordLst,"\n",filteredLst)