
budget = float(input())
pricePerFlourKg = float(input())
priceForEggs = pricePerFlourKg * 0.75
pricePerMilkLitre = pricePerFlourKg * 1.25 
numberOfLoaves = 0
numberOfEggs = 0
pricePerLoaf = priceForEggs + pricePerFlourKg + pricePerMilkLitre * 0.25
while True:
    if (budget - pricePerLoaf) > 0:
        budget -= pricePerLoaf
    else:
        print(f"You made {numberOfLoaves} loaves of Easter bread! Now you have {numberOfEggs} eggs and {budget:.2f}BGN left.")
        break
    numberOfLoaves += 1
    numberOfEggs += 3
    if numberOfLoaves % 3 == 0:
        numberOfEggs -= numberOfLoaves - 2
    

