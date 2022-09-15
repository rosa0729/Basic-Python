while True:
    a, b, c = input().split()
    a, c = int(a), int(c)
    if b == "+":
        print(a+c)
    elif b == "-":
        print(a-c)
    elif b == "*":
        print(a*c)
    elif b == "/":
        print(a//c)
    elif b == "?":
        break
