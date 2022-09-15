x = 0
a, b, c = map(int, input().split())
while a <= b:
    if c % a == 0:
        x = x + 1
    a = a+1
print(x)
