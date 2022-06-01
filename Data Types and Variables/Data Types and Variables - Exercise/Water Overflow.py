
capacity = 255
n = int(input())
currentLitres = 0

for i in range(0,n):
    waterLitres = int(input())
    if (capacity - waterLitres) >= 0: 
        currentLitres += waterLitres
        capacity -= waterLitres
    else:
        print("Insufficient capacity!")

print(currentLitres)