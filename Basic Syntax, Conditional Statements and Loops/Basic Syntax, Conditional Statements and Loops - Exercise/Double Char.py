while True:
    word = input()
    if word == "End":
        break
    if word != "SoftUni":
        for letter in word:
            print(letter * 2, end="")
        print()
    