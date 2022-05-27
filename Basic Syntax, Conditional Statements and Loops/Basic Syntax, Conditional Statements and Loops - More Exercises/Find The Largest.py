
numbers = input()
numbers_list = list(numbers)
numbers_list.sort(reverse=True)
for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])
for i in numbers_list:
    print(i, end="")
    
     

