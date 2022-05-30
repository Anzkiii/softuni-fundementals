
beach_string = input()
points = 0
sand = beach_string.upper().count("SAND")
water = beach_string.upper().count("WATER")
fish = beach_string.upper().count("FISH")
sun = beach_string.upper().count("SUN")

print(sand + water + fish + sun)

