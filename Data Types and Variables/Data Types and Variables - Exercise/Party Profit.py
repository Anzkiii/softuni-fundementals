from sys import exit
groupSize = int(input())
days = int(input())
if groupSize < 1 or days < 1 or groupSize > 100 or days > 100:
    exit()

coins = 0
for i in range(days, 0, -1):
    coins += 50
    coins -= 2 * groupSize
    if i % 5 == 0 and i % 3 == 0:
        coins += 20 * groupSize
        coins  -= 2 * groupSize
    elif i % 5 == 0:
        coins += 20 * groupSize
    if i % 3 == 0:
        coins -= 3 * groupSize
    if i % 10 == 0:
        groupSize -= 2
    if i % 15 == 0:
        groupSize += 5
        
print(f"{groupSize} companions received {round(coins/groupSize)} coins each.")

