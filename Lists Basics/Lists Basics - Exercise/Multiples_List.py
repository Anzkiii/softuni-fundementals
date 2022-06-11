
factor = int(input())
count = int(input())

lst = []

for i in range(0, factor*count + 1, factor):
    lst.append(i)
if lst[0] == 0:
    lst.pop(0)
print(lst)
    