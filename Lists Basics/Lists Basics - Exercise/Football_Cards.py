
A = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
B = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
A_left = []
B_left = []
playerCardsLst = input().split(" ")

for i in playerCardsLst:
    if "A" in i and i[2:] not in A_left:
        A.remove(i[2:])
        A_left.append(i[2:]) 
    elif "B" in i and i[2:] not in B_left:
        B_left.append(i[2:]) 
        B.remove(i[2:])
if len(A) < 7 or len(B) < 7:
    print(f"Team A - {len(A)}; Team B - {len(B)}\nGame was terminated")
else:
    print(f"Team A - {len(A)}; Team B - {len(B)}")
