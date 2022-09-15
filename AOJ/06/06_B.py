n = int(input())
cards = list()
mark = ["S", "H", "C", "D"]
for i in range(n):
    a, b = input().split()
    b = int(b)
    if a == "S":
        cards.append(0 + b)
    elif a == "H":
        cards.append(13 + b)
    elif a == "C":
        cards.append(26 + b)
    elif a == "D":
        cards.append(39 + b)
for i in range(1, 53):
    if not (i in cards):
        print(mark[(i - 1) // 13], (i-1) % 13 + 1)
