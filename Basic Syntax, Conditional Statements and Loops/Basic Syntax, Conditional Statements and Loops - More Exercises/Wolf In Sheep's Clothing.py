
animals = input()
animals_list = animals.split(", ")
sheep = 0
if animals_list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    sheep_count = 0
    for i in range(0, len(animals_list)):
        if animals_list[i] == "wolf":
            wolf_index = i
        else:
            sheep_count += 1
    for i in range(0, len(animals_list)):
        if animals_list[i] == "wolf":
            print(f"Oi! Sheep number {len(animals_list) - 1 - i}! You are about to be eaten by a wolf!")






