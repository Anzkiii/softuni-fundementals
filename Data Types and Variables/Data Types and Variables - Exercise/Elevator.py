from math import floor
people = int(input())
capacity = int(input())
x = people / capacity
if people % capacity != 0:
    print(floor(x) + 1)
else:
    print(floor(x))

