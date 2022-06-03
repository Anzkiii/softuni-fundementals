
num = int(input())
n = 0
ls = []
for i in range(1, num + 1):
    if (num / i) - int(num / i) == 0:
        ls.append("True")
    else:
        ls.append("False")
    
if "True" in ls[1:-1]:
    print("False")
else:
    print("True")


