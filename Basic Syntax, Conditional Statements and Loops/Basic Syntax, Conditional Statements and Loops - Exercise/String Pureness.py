
n = int(input())

for i in range(n):
    string_var = input()
    if "," in string_var or "." in string_var or "_" in string_var:
        print(f"{string_var} is not pure!")
    else:
        print(f"{string_var} is pure.")
