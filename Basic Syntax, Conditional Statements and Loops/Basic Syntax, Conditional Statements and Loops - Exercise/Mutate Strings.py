
string1 = input()
string2 = input()

for i in range(len(string1)):
    if string1[i] != string2[i]:
        str1 = list(string1)
        str1[i] = string2[i]
        string1 = ""
        for value in str1:
            string1 += value
        print(string1)
