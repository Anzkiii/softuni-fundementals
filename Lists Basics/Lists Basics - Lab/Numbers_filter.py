
iterator = int(input())
lst = []
for i in range(iterator):
    num = int(input())
    lst.append(num)
command = input()
commandLst = []
if command == "even":
    for i in lst:
        if i % 2 == 0:
            commandLst.append(i)
elif command == "odd":
    for i in lst:
        if i % 2 != 0:
            commandLst.append(i)
elif command == "negative":
    for i in lst:
        if i < 0:
            commandLst.append(i)
elif command == "positive":
    for i in lst:
        if i >= 0:
            commandLst.append(i)
print(commandLst)

