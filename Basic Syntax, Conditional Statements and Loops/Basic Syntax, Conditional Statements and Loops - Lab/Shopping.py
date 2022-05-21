budget = int(input())
total_budget = 0
while True:
    prices = input()
    if prices.isdigit():
        prices = int(prices)    
    if prices == "End":
        print("You bought everything needed.")
        break
    else:
        total_budget += prices
        if total_budget > budget:
            print("You went in overdraft!")
            break
