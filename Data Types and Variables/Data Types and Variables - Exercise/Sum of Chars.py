
n = int(input())
sum = 0
for i in range(0, n):
    letter = input()
    sum += ord(letter)
print(f"The sum equals: {sum}")