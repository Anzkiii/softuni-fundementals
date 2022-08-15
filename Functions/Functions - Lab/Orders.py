
product = input()
quantity = int(input())

def order_calculation(product, quantity):
    if product == "coffee":
        return float(1.50 * quantity)
    elif product == "coke":
        return float(1.40 * quantity)
    elif product == "water":
        return float(1.00 * quantity)
    elif product == "snacks":
        return float(2.00 * quantity)

print(f"{order_calculation(product, quantity):.2f}")