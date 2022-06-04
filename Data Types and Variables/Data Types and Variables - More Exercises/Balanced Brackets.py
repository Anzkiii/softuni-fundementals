
n = int(input())
left = 0
right = 0
brackBool = False
for i in range(n):
    strInp = input()
    for i in strInp:
        if i == "(":
            left += 1
            if not brackBool:
                brackBool = True
        if i == ")":
            right += 1
            if brackBool:
                brackBool = False
if left == right:
    print("BALANCED")
else:
    print("UNBALANCED")

