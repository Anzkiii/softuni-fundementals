
n = int(input())
left = 0
right = 0
brackBool = False
for i in range(n):
    strInp = input()
    for i in strInp:
        if i == "(" and not brackBool:
            left += 1
            brackBool = True
        if i == ")" and brackBool:
            right += 1
            brackBool = False
if left == right:
    print("BALANCED")
else:
    print("UNBALANCED")

