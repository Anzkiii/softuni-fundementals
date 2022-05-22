divisor = int(input())
boundary = int(input())
n = 1
num_list = []
while True:
    n += 1
    if n % divisor == 0:
        if n <= boundary:
            if n > 0:
                num_list.append(n)
        else:
            break
                
print(num_list[-1])

