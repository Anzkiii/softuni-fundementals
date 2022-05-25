
quantity = int(input())
days = int(input())
total = 0
spirit = 0
ornamentSet = 2
treeSkirt = 5
treeGarland = 3
treeLights = 15
days_left = 0
while True:
    days_left += 1
    days -= 1
    if days_left % 2 == 0:
        total += ornamentSet * quantity
        spirit += 5
    if days_left % 3 == 0:
        total += (treeSkirt * quantity) + (treeGarland * quantity)
        spirit += 13
    if days_left % 5 == 0:
        total += treeLights * quantity
        spirit += 17
    if days_left % 10 == 0:
        spirit -= 20
        total += treeSkirt + treeGarland + treeLights
    if days_left % 11 == 0:
        quantity += 2
    if days < 1 and days_left % 10 == 0:
        spirit -= 30
        break
    if days == 0:
        break

print(f"Total cost: {total}\nTotal spirit: {spirit}")
#This one gives 50/100 , ill be fixing that a bit in the future
