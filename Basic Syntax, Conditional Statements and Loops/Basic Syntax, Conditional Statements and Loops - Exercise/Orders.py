
n = int(input())
totalPrice = 0
for i in range(n):
    capsulePrice = float(input())
    days = int(input())
    capsulesNeeded = int(input())
    if capsulePrice < 0.01 or capsulePrice > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsulesNeeded < 1 or capsulesNeeded > 2000:
        continue
    priceForCoffee = (capsulesNeeded * days) * capsulePrice
    totalPrice += priceForCoffee
    print(f"The price for the coffee is: ${priceForCoffee:.2f}")
print(f"Total: ${totalPrice:.2f}")