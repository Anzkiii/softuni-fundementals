
numOfSnowballs = int(input())
someNum = 0
for i in range(0 , numOfSnowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    calculation = round((weight / time) ** quality)
    if calculation > someNum:
        someNum = calculation
        value = [weight, time, calculation, quality]
print(f"{value[0]} : {value[1]} = {value[2]} ({value[3]})")
