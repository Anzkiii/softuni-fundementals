
year = int(input())

yearSet = {None}
for i in str(year):
    yearSet.update(i)
while True:

    if len(yearSet) == len(str(year)) + 1:
        print(year)
        break
    
    year += 1
    yearSet = {None}
    for i in str(year):
        yearSet.update(i)
    
    
        
    

