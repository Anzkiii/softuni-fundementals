coffee_cups = 0
while True:
    event = input()
    if event == "CODING" or event == "DOG" or event == "CAT" or event == "MOVIE":
        coffee_cups += 2
    elif event == "coding" or event == "dog" or event == "cat" or event == "movie":
        coffee_cups += 1 
    elif event == "END":
        break
if coffee_cups > 5:
    print("You need extra sleep")
else:
    print(coffee_cups)