while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    N = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            k = x - i - j
            if k <= n and k > j:
                N += 1

    print(N)
