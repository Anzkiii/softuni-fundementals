
key = int(input())
n = int(input())
finalStr = ""
for i in range(n):
    strInput = input()
    finalStr += chr(ord(strInput) + key)
print(finalStr)

