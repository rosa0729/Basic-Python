x = str(input())
y = str(input())
x += x
ans = "No"
for i in range(len(x)//2):
    if x[i] == y[0]:
        for n in range(len(y)):
            if x[i+n] != y[n]:
                break
            if n == len(y)-1:
                ans = "Yes"
print(ans)
