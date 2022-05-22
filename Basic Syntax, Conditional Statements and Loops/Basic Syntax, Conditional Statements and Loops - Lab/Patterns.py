
rows = int(input())

for i in range(rows):
    for k in range(i+1):
        print("*", end="")
    print("")
for i in range(rows - 1, 0, -1):
    for k in range(0, i):
        print("*", end="")
    print("")
