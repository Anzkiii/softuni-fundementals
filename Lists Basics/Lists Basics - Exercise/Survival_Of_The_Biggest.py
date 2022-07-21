import sys
lst = [int(x) for x in input().split(" ")]
nums_to_remove = int(input())
small_num = sys.maxsize
for i in range(nums_to_remove):
    for i in lst:
        if i < small_num: small_num = i
    lst.remove(small_num)
    small_num = sys.maxsize

for i in range(len(lst) - 1):
    lst[i] = f"{lst[i]},"

print(*lst)

